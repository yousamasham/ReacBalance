from ChemTypes import ElementT
from Set import *
from ElmSet import *
from MolecSet import *
from MoleculeT import *
from CompoundT import *
from ReactionT import *

# Chem Type Examples
e1 = ElementT.H
e2 = ElementT.He
# Set Examples - with integers
S = Set([1, -6, 4, 0, 12])

S.add(5)

S.rm(4)

print(S.member(5))
print(S.member(4))
print(S.size())

R = Set([12, -6, 0, 1, 5])

print(S.equals(R))
print(S == R)

print(str(R.to_seq()))

'''for i in R.to_seq():
    print(i)'''

# ElmSet Examples
E = ElmSet([ElementT.H, ElementT.O])
E.add(ElementT.C)
print(E == ElmSet([ElementT.H, ElementT.C, ElementT.O]))

# MoleculeT Examples
M1 = MoleculeT(1, ElementT.H)
M12 = MoleculeT(2, ElementT.H)
M2 = MoleculeT(2, ElementT.O)
M2m = MoleculeT(1, ElementT.O)
print(M1.num_atoms(ElementT.C))
print(M1.constit_elems() == ElmSet([ElementT.H]))
print(M1.equals(M2))
print(M1 == M2)

# CompoundT Examples
Cr1 = CompoundT(MolecSet([M1]))
Cr2 = CompoundT(MolecSet([M2]))
C1 = CompoundT(MolecSet([M1, M2m]))
print(C1.num_atoms(ElementT.H))
e = C1.constit_elems()
print(e.equals(ElmSet([ElementT.H, ElementT.O])))
print(C1.equals(CompoundT(MolecSet([M1]))))
C2 = CompoundT(MolecSet([M1, M2]))
T1 = MoleculeT(1, ElementT.Na)
T2 = MoleculeT(1, ElementT.Cl)
T22 = MoleculeT(2, ElementT.Cl)
A1 = MoleculeT(1, ElementT.C)
A2 = MoleculeT(2, ElementT.H)
A3 = MoleculeT(4, ElementT.H)
C1 = CompoundT(MolecSet([A1]))
C2 = CompoundT(MolecSet([A2]))
C3 = CompoundT(MolecSet([A1, A3]))
Com1 = CompoundT(MolecSet([T1, M2m, M1]))
Com2 = CompoundT(MolecSet([M1, T2]))
Com3 = CompoundT(MolecSet([M12, M2m]))
Com4 = CompoundT(MolecSet([T1, T22]))
ReactionT([C1, C2], [C3])
