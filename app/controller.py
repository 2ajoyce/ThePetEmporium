'''The application URL controllers'''
from flask import request, session, g, redirect, url_for, \
     abort, render_template, flash
from . import App


@App.route('/')
def show_pets():
    cur = g.db.execute('select type, name, age, weight, hungry, photo from pets order by id desc')
    pets = [dict(type=row[0], name=row[1], age=row[2], weight=row[3], hungry=row[4], photo=row[5]) for row in cur.fetchall()]
    return render_template('show_pets.html', pets=pets)


@App.route('/add', methods=['POST'])
def add_pet():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute(
        'insert into pets (type, name, age, weight, hungry, photo) values (?, ?, ?, ?, ?, ?)',
        [request.form['type'], request.form['name'], request.form['age'], request.form['weight'],
         1 if 'hungry' in request.form else 0, request.form['photo']])
    g.db.commit()
    flash('New pet was successfully posted')
    return redirect(url_for('show_pets'))

@App.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != App.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != App.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_pets'))
    return render_template('login.html', error=error)

@App.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_pets'))