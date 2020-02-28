## @file Set.py
#  @author Yousam Asham
#  @brief An ADT for the creation and manipulation of a set
#  @date February 1 2020

from Equality import *


## @brief The ADT called Set.
#  @details Contains the methods for the manipulation and editing of a set data
#type representation.
class Set(Equality):

    ## @brief Constructor for the Set class
    #  @details Initializes the attributes to the state variable S
    #  @param S represents the list or set to be inputted and to be made into an object
    def __init__(self, s):
        self.__S = s

    ## @brief A method to add elements to a set object
    #  @details This method can be seen as a Union operator
    #  @param e represents the element to be added
    def add(self, e):
        self.to_seq().append(e)

    ## @brief A method to remove elements from a set object
    #  @details The method also has to confirm that the current set object has
    #this element as part of its contents
    #  @param e represents the element to be removed
    #  @throws ValueError: When the element to be removed is not part of the
    #current set object to be removed from
    def rm(self, e):
        if e in self.to_seq():
            self.to_seq().remove(e)
        else:
            raise ValueError("Not found in set!")

    ## @brief A method to check if an element is a member of a set object
    #  @param e represents teh element to be checked
    #  @return A boolean value indicating whether the element is in the set object or not
    def member(self, e):
        lst = self.to_seq()
        if e in lst:
            return True
        else:
            return False

    ## @brief A method to provide the length of a set object
    #  @return The length of the set
    def size(self):
        return len(self.to_seq())

    ## @brief This is the equal method that is an abstract method in Equality.py
    #  @details This method checks if two set objects are the same, as in,
    #their contents are exactly identical
    #  @param R represents the set object that the current set object will be compared to
    #  @return A boolean value indicating whether the set object is equal to
    #the current set object
    def equals(self, R):
        if self.size() == R.size():
            lst = self.to_seq()
            count = 0
            for item in lst:
                if R.member(item):
                    count += 1
            if count == self.size():
                return True
            else:
                return False
        else:
            return False

    ## @brief A getter method for the state variable of Set
    #  @return the set as a sequence/list
    def to_seq(self):
        return self.__S
