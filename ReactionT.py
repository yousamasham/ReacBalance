## @file ReactionT.py
#  @author Yousam Asham
#  @brief An ADT for representing a chemical reaction
#  @date February 3 2020

from ChemTypes import *
from CompoundT import *
import numpy as np


## @brief The ADT called ReactionT
class ReactionT:

    ## @brief The constructor method for ReactionT
    #  @details This method is where the actual balancing of the reaction object occurs.
    #  @param lhs represents the left hand side of the reaction to be
    #balanced, is a list of CompoundT objects
    #  @param rhs represents the right hand side of the reaction to be
    #balanced, is a list of CompoundT objects
    def __init__(self, lhs, rhs):
        self.__lhs = lhs
        self.__rhs = rhs
        self.__CoeffL = []
        self.__CoeffR = []
        index1 = 0
        index2 = -1
        count = 0
        superreac = []
        superreac.append(self.get_lhs())
        superreac.append(self.get_rhs())
        superreact = sum(superreac, [])
        elm_present = ElmSet([])
        for c in superreact:
            for m in c.get_molec_set():
                if not elm_present.member(m.get_elm()):
                    elm_present.add(m.get_elm())
        a = [[0 for x in range(len(superreact))] for x in range(elm_present.size())]
        for c in superreact:
            index2 += 1
            count += 1
            for m in c.get_molec_set():
                iterationcount = 0
                index1 = 0
                for e in elm_present.to_seq():
                    if (count > len(self.get_lhs())):
                        n = -1
                    else:
                        n = 1
                    a[index1][index2] += m.num_atoms(e) * n
                    index1 += 1
                    if iterationcount == len(elm_present.to_seq()):
                        index1 += 1
                    else:
                        iterationcount += 1
        iterationcount = 0
        rightvector = [[0] for _ in range(len(a))]
        rightvector[-1] = [1]
        if not (len(a) < len(superreact)):
            correctorrow = [0 for _ in range(len(superreact))]
            correctorrow[-1 - iterationcount] = 1
            a[-1] = correctorrow
        while(len(a) < len(superreact)):
            print(iterationcount)
            correctorrow = [0 for _ in range(len(superreact))]
            correctorrow[-1 - iterationcount] = 1
            a.append(correctorrow)
            rightvector = [[0] for _ in range(len(a))]
            rightvector[-1 - iterationcount] = [1]
            iterationcount += 1
        c = np.array(a)
        d = np.array(rightvector)
        solution = np.linalg.solve(c, d)
        sol = solution.tolist()
        iterationcount = 0
        for i in range(len(solution)):
            iterationcount += 1
            if iterationcount <= len(self.get_lhs()):
                self.get_lhs_coeff().append(sol[i][0])
            else:
                self.get_rhs_coeff().append(sol[i][0])
        if is_balanced(self.get_lhs(), self.get_rhs(), self.get_lhs_coeff(),
                                                self.get_rhs_coeff()) is False:
            raise ValueError("Unable to balance reaction!")

    ## @brief A getter method for the CompoundT list called lhs
    #  @return A list of reactants
    def get_lhs(self):
        return self.__lhs

    ## @brief A getter method for the CompoundT list called rhs
    #  @return A list of products
    def get_rhs(self):
        return self.__rhs

    ## @brief A getter method for the list of reactant coefficients of balanced
    #checmial equation
    #  @return A list of reactant coefficients
    def get_lhs_coeff(self):
        return self.__CoeffL

    ## @brief A getter method for the list of prodcut coefficients of balanced
    #chemical equation
    #  @return A list of product coefficents
    def get_rhs_coeff(self):
        return self.__CoeffR


## @brief A local funtion that checks if a reaction has been balanced or not
#  @details This local function uses other local functions to check for
#balancing.
#  @param left represents the reactants of a reaction
#  @param right represents the products of a reaction
#  @param leftc represents a sequence of the reactant coefficients
#  @param rightc represents a sequence of the product coefficents
#  @return True if chemical equation is balanced, False otherwise
def is_balanced(left, right, leftc, rightc):
    leftelem = ElmSet([])
    rightelm = ElmSet([])
    for c in left:
        for m in c.get_molec_set():
            if not leftelem.member(m.get_elm()):
                leftelem.add(m.get_elm())
    for c in right:
        for m in c.get_molec_set():
            if not rightelm.member(m.get_elm()):
                rightelm.add(m.get_elm())
    if leftelem.equals(rightelm) is False:
        return False
    for elm in leftelem.to_seq():
        if is_bal_elm(left, right, leftc, rightc, elm) is False:
            return False
    return True


## @brief A local function that checks the quantity of a specific element in
#either the reactants or the products
#  @param c represents a sequence of CompoundT
#  @param coeff represents a sequence of real numbers, the coefficients of the
#respective side of the chemical reaction in question.
#  @param elem represents the element that is being searched for
#  @return the number of atoms of an element
def n_atoms(c, coeff, elem):
    count = 0
    index = -1
    for compound in c:
        index += 1
        count += coeff[index] * compound.num_atoms(elem)
    return count


## @brief A local function that checks if an element is balanced in a chemical reaction
#  @param left represents the sequence of CompoundT that correstponds to the reactants
#  @param right represents the sequence of CompoundT that correstponds to the products
#  @param coeffl represents the sequence of real numbers corresponding to the
#coefficients of the reactants
#  @param coeffr represents the sequence of real numbers corresponding ot the
#coefficents of the products
#  @param elem represents the element in question
#  @return True if the element is balanced, False otherwise
def is_bal_elm(left, right, coeffl, coeffr, elem):
    return n_atoms(left, coeffl, elem) == n_atoms(right, coeffr, elem)


## @brief checks if a sequence of number has all positive elements
#  @param s represents the sequence of real numbers to be checked
#  @return True if all the elements are positive, False otherwise
def pos(s):
    for i in s:
        if i <= 0:
            return False
    return True
