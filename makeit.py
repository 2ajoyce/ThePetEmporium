"""The Pet Emporium, A programming collaboration between Aaron and Leah"""

import json


class Pet:
    """A Pet Class"""
    def __init__(self, pType, pName, pAge, pWeight, pHungry, pPhoto):
        """
        A constructor function for type Pet.
        Params:
            self Pet, Auto added when this member fuction is run
            pType String, The type of animal that this Pet is.  Ex. cat, dog
            pName String, The name of the Pet. Ex. Triangle, Nibbles
            pAge Integer, The age of the Pet. Ex. 10, 5, 13
            pWeight Float, The weight of the Pet in pounds. Ex. 10.0, 5.3
            pHungry Boolean, Indicates if the Pet is hungry. Ex. True, False
            pPhoto String, A grapical representation of a Pet. Ex. (=^o.o^=)__
        Return:
            An object of type Pet that has the atributes specified in the
            parameters.
        """
        self.pType = pType
        self.pName = pName
        self.pAge = pAge
        self.pWeight = pWeight
        self.pHungry = pHungry
        self.pPhoto = pPhoto

    def feed(self):
        """Feeds the pet. The pet will stop being hungry and gain weight."""
        if self.pHungry:
            self.pHungry = False
            self.pWeight += 1
        else:
            print('Your pet is not hungry!')

def importPets():
    """
    This function imports all pets from the pets.json file.
    After importing the pets it saves them each as type Pet
    and stores them in a list called Kennel.
    Return:
        Kennel, List, filled with type Pet
    """
    pets = json.loads(open('pets.json').read())
    Kennel = []

    for _, pet in pets.items():
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
    """
    The main function that is run when the program is run.
    """
    print('Welcome to The Pet Emporium!')
    print('Who would you like to play with?')

    kennel = importPets()

    for pet in kennel:
        print(pet.pName, pet.pPhoto)

    while True:
        print("""
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
