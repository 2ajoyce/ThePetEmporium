"""The Pet Emporium, A programming collaboration between Aaron and Leah"""

print('Welcome to The Pet Emporium!')


cat = {
    'name' : 'Fluffy',
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
        print('The Pypet is not hungry!')

for bed in pets:
    feed(bed)
    print(bed)
