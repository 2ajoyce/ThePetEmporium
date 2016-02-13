class Pet:
    """A Pet Class"""
    def __init__(self, attributes):
        """
        A constructor function for type Pet.
        Params:
            self Pet, Auto added when this member fuction is run
            attributes dict, a list of attributes containing:
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
        self.pType = attributes["pType"]
        self.pName = attributes["pName"]
        self.pAge = attributes["pAge"]
        self.pWeight = attributes["pWeight"]
        self.pHungry = attributes["pHungry"]
        self.pPhoto = attributes["pPhoto"]

    def feed(self):
        """Feeds the pet. The pet will stop being hungry and gain weight."""
        if self.pHungry:
            self.pHungry = False
            self.pWeight += 1
        else:
            print('Your pet is not hungry!')
