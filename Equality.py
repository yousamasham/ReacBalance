## @file Equality.py
#  @author Yousam Asham
#  @brief A generic equality protoype module to test for equality of various
#types and objects in other modules
#  @date February 1 2020

from abc import ABC, abstractmethod


## @brief An Abstract Base Class called Equality
#  @details Methods of this class are to be implemented in other modules that require them.
class Equality(ABC):

    ## @brief An abstract method called Equality, to be implemented in many other modules
    #  @param comparable represent the other object to be compared to
    #  @return Boolean indicatin whether the two objects are equal or not
    @abstractmethod
    def equals(self, comparable):

        pass
