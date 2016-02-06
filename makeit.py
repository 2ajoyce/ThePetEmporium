"""The Pet Emporium, A programming collaboration between Aaron and Leah"""

import json


class Pet:
    """A Pet Class"""
    def __init__(self, type, name, age, weight, hungry, photo):
        self.type = type
        self.name = name
        self.age = age
        self.weight = weight
        self.hungry = hungry
        self.photo = photo

    def feed(self):
        """Feeds the pet. The pet will stop being hungry and gain weight."""
        if self.hungry:
            self.hungry = False
            self.weight += 1
        else:
            print('Your pet is not hungry!')

def importPets():
    pets = json.loads(open('pets.json').read())
    Kennel = []

    for index, pet in pets.items():
        pType = pet[0]['type']
        pName = pet[1]['name']
        pAge = pet[2]['age']
        pWeight = pet[3]['weight']
        pHungry = pet[4]['hungry']
        pPhoto = pet[5]['photo']
        Kennel.append(Pet(pType, pName, pAge, pWeight, pHungry, pPhoto))
    return Kennel


# Lets user pick a pet from the list shown to interact with
def pickaPet():
    pet = input()
    return pet

# Greet user and ask what pet they would like to interact with
# Show list of pets with phots and names
def main():
    print('Welcome to The Pet Emporium!')
    print('Who would you like to play with?')

    kennel = importPets()

    for pet in kennel:
        print(pet.name, pet.photo)

    while True:
        print ("""
        1.Add a Pet
        2.Delete a Pet
        3.Look Up Pet
        4.Exit/Quit
        """)
        ans = input("What would you like to do? ") 
        if ans == "1": 
          print("\n Pet Added") 
        elif ans == "2":
          print("\n Pet Deleted") 
        elif ans == "3":
          print("\n Pet Found") 
        elif ans == "4":
          print("\n Goodbye")
          break 
        elif ans != "":
          print("\n Not Valid Choice Try again") 

if __name__ == '__main__':
    #  Start it
    main()