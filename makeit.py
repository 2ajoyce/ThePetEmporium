"""The Pet Emporium, A programming collaboration between Aaron and Leah"""

# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing
import json
from pet import Pet

# configuration
DATABASE = 'petEmporium.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route('/')
def show_pets():
    cur = g.db.execute('select type, name from pets order by id desc')
    pets = [dict(type=row[0], name=row[1]) for row in cur.fetchall()]
    return render_template('show_pets.html', pets=pets)

@app.route('/add', methods=['POST'])
def add_pet():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute(
        'insert into pets (type, name, age, weight, hungry, photo) values (?, ?)',
        [request.form['type'], request.form['name'], request.form['age'], request.form['weight'], 
        request.form['hungry'], request.form['photo']])
    g.db.commit()
    flash('New pet was successfully posted')
    return redirect(url_for('show_pets'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_pets'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_pets'))


def importPets():
    """
    This function imports all pets from the pets.json file.
    After importing the pets it saves them each as type Pet
    and stores them in a list called Kennel.
    Return:
        Kennel, List, filled with type Pet
    """
    pets = json.loads(open('pets.json').read())
    Kennel = {}
    attributes = {}

    for _, pet in pets.items():
        attributes["pType"] = pet[0]['type']
        attributes["pName"] = pet[1]['name']
        attributes["pAge"] = pet[2]['age']
        attributes["pWeight"] = pet[3]['weight']
        attributes["pHungry"] = pet[4]['hungry']
        attributes["pPhoto"] = pet[5]['photo']
        Kennel[attributes["pName"]] = Pet(attributes)
    return Kennel


# Lets user pick a pet from the list shown to interact with
def pickaPet(kennel):
    pet_name = input("Enter a name to select that pet: ")
    try:
        pet = kennel[pet_name]
        return pet
    except KeyError:
        print("There is no pet named {}.".format(pet_name))

# Greet user and ask what pet they would like to interact with
# Show list of pets with phots and names
def main():
    """
    The main function that is run when the program is run.
    """
    print('Welcome to The Pet Emporium!')
    print('Who would you like to play with?')

    kennel = importPets()

    while True:
        print("""
         *Main Menu*
        1.View Kennel
        2.Delete a Pet
        3.Look Up Pet
        4.Exit/Quit
        """)
        ans = input("What would you like to do? ")
        if ans == "1":
            print('\\\\Kennel\\\\')
            print()
            for pet in kennel:
                print(kennel[pet].pName, kennel[pet].pPhoto)
        elif ans == "2":
            print("\n Pet Deleted")
        elif ans == "3":
            pet = pickaPet(kennel)
        elif ans == "4":
            print("\n Goodbye")
            break
        elif ans != "":
            print("\n Not Valid Choice Try again")

if __name__ == '__main__':
    #  Start it
    #main()
    init_db()
    app.run()