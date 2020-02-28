## @file ChemEntity.py
#  @author Yousam Asham
#  @brief An interface module protoype with two subroutines
#  @date February 1 2020

from abc import ABC, abstractmethod


## @brief An Abstract Base Class called ChemEntity
#  @details Methods of this class are to implemented in other modules that need them.
class ChemEntity(ABC):

    ## @brief An abstract method called num_atoms, to be implmented in other modules
    #  @param e represents the object to be counted and hae its count returned
    #  @return The number of specific atoms as the arguement
    @abstractmethod
    def num_atoms(self, e):

        pass

    ## @brief An abstract method called constit_elems, to be implmented in other modules
    #  @return The objects that make up a specific set or sequence of objects
    @abstractmethod
    def constit_elems(self):

        pass
