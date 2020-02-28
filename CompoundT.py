## @file CompoundT.py
#  @author Yousam Asham
#  @brief An ADT for representing a chemical compound
#  @date February 2 2020

from MolecSet import *
from ChemEntity import *
from Equality import *
from ElmSet import *
from MoleculeT import *


## @brief The ADT called CompoundT
class CompoundT(ChemEntity, Equality):

    ## @brief A contructor for the CompoundT class
    #  @details Initializes and creats a new CompoundT object
    #  @param C: represents the set of MoleculeT objects that come together to
    #make a CompoundT object
    def __init__(self, C):
        self.__C = C

    ## @brief A getter method for the molecule set that makes up a CompoundT object
    def get_molec_set(self):
        return self.__C

    ## @brief This is the num_atoms method that is an abstract method in ChemEntity.py
    #  @details This method provides the quantity of a specific atom present in
    #a CompoundT object given an atom
    #  @param e represents the element that the user would like to know the
    #quantity of in the CompoundT object
    #  @return A number representing the quantity of searched element in the CompoundT object
    def num_atoms(self, e):
        count = 0
        lst = self.get_molec_set()
        for element in lst:
            if element.get_elm() == e:
                count += element.get_num()
        return count

    ## @brief This is the constit_elems method that is an abstract method in ChemEntity.py
    #  @details This method provides a list an ElmSet object that contains the
    #elem present in the current CompoundT object
    #  @return A list with the constituent elements of a CompoundT object in a ElmSet object
    def constit_elems(self):
        element_set = ElmSet([])
        lst = self.get_molec_set()
        for molecule in lst:
            elem = molecule.get_elm()
            element_set.add(elem)
        return element_set

    ## @brief This is the equals method that is an abstract method in Equality.py
    #  @details This method determines if two CompoundT objects are equal
    #  @param D represents the CompoundT object ot be compared to
    #  @return True if the CompoundT object are equal to each other, False otherwise
    def equals(self, D):
        return self.get_molec_set() == (D.get_molec_set())
