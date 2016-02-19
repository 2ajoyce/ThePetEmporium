"""The Pet Emporium, A programming collaboration between Aaron and Leah"""

import json
from app.pet import Pet


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
    main()
