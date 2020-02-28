## @file MoleculeT.py
#  @author Yousam Asham
#  @brief An ADT for representing a chemical molecule.
#  @date February 1 2020

from ChemTypes import *
from ChemEntity import *
from Equality import *
from ElmSet import *


## @brief The ADT called MoleculeT
class MoleculeT(ChemEntity, Equality):

    ## @brief A constructor for the MoleculeT module
    #  @details Initializes MoleculeT type objects that are made of only one
    #element but can have more than one of that kind of element
    #  @param num represents the number of atoms in the molecule
    #  @param elm represents the element the molecule object is made up of
    def __init__(self, num, elm):
        self.__num = num
        self.__elm = elm

    ## @brief A getter method for the number of elements making up the molecule object
    #  @return The number of elements
    def get_num(self):
        return self.__num

    ## @brief A getter method for the element that the MoleculeT object is made up of
    #  @return The element of type ElementT
    def get_elm(self):
        return self.__elm

    ## @brief This is the num_atoms method that is an abstract method in ChemEntity.py
    #  @details This method provides the number of atoms of a specific element
    #in a MoleculeT object
    #  @param e represents the element that we are looking for in the MoleculeT object
    #  @return The quanitity of the element in the MoleculeT object. 0 if the
    #element is not present in the MoleculeT object
    def num_atoms(self, e):
        if e == self.get_elm():
            return self.get_num()
        else:
            return 0

    ## @brief This is the constit_elems method that is an abstract method in ChemEntity.py
    #  @details This method provides the elements making up a MoleculeT object
    #  @return The element making up this MoleculeT object
    def constit_elems(self):
        return ElmSet([self.get_elm()])

    ## @brief This is the equal method that is an abstract method in Equality.py
    #  @details This method checks if two MoleculeT objects are the same, as
    #in, their contents (element and number of element) are exactly identical
    #to each other
    #  @param m represents MoleculeT object that the current set object will be compared to
    #  @return A boolean value indicating whether the MoleculeT object is equal
    #to the current MoleculeT object
    def equals(self, m):
        if m.get_elm() == self.get_elm() and m.get_num() == self.get_num():
            return True
        else:
            return False
