"""The Pet Emporium, A programming collaboration between Aaron and Leah"""

from flask import Flask, url_for
app = Flask(__name__)

def from_py(hello):
  def wrapper(*args, **kwargs):
    return hello(*args, **kwargs) + " From Python!"
  return wrapper

@app.route('/login')
def login():
    return "You Logged In!"
    
@app.route("/")
@from_py
def hello():
    return "Hello World! " + "<a href=" + url_for('login') + "> Login </a><br>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')


print('Welcome to The Pet Emporium!')


cat = {
    'name' : 'Triangle',
    'hungry' : True,
    'weight' : 9.5,
    'age' : 5,
    'photo' : '(=^o.o^=)__',
}

mouse = {
    'name' : 'Nibbles',
    'age' : 6,
    'weight' : 1.5,
    'hungry' : True,
    'photo' : '<:3 )~~~~',
}

pets = [cat, mouse]

print('Hello ' + cat['name'])
print(cat['photo'])
print('Hello ' + mouse['name'])
print(mouse['photo'])

def feed(pet):
    """Feeds the pet that is passed into it.  The pet will stop being hungry and gain weight."""
    if pet['hungry']:
        pet['hungry'] = False
        pet['weight'] = pet['weight'] + 1
    else:
        print('Your pet is not hungry!')

for animal in pets:
    feed(animal)
    print(animal)
