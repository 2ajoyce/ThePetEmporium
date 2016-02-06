"""The Pet Emporium, A programming collaboration between Aaron and Leah"""

import json

def feed(pet):
    """Feeds the pet that is passed into it.  The pet will stop being hungry and gain weight."""
    if pet['hungry']:
        pet['hungry'] = False
        pet['weight'] = pet['weight'] + 1
    else:
        print('Your pet is not hungry!')

def importPets():
    pets = json.loads(open('pets.json').read())
    return pets


def main():
    print('Welcome to The Pet Emporium!')

    kennel = importPets()
    print(kennel)
    
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

    for animal in pets:
        feed(animal)
        print(animal)

if __name__ == '__main__':
    #  Start it
    main()