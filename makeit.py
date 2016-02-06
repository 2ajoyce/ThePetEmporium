"""The Pet Emporium, A programming collaboration between Aaron and Leah"""

import json

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

def pickaPet():

    return pet

# Greet user and ask what pet they would like to interact with
# Show list of pets with phots and names
def main():
    print('Welcome to The Pet Emporium!')
    print('Who would you like to play with?')
    print(cat['name'], cat['photo'])
    print(mouse['name'], mouse['photo'])

    kennel = importPets()    
    pet = pickaPet()
    pets = [cat, mouse]

    for animal in pets:
        feed(animal)
        print(animal)

if __name__ == '__main__':
    #  Start it
    main()