from ChemTypes import ElementT
from Set import *
from ElmSet import *
from MolecSet import *
from MoleculeT import *
from CompoundT import *
from ReactionT import *

L1 = [1, 5, 9, 7, 6, 12]
L = Set(L1)


def test_add_set():
    L.add(4)
    assert L.to_seq() == [1, 5, 9, 7, 6, 12, 4]


def test_rm_set():
    L.rm(4)
    assert L.to_seq() == [1, 5, 9, 7, 6, 12]


def test_member_set():
    assert L.member(1)


def test_size_set():
    assert L.size() == len(L1)


def test_equals_set():
    assert L.equals(Set([1, 5, 9, 7, 6, 12]))


def test_to_seq_set():
    assert L.to_seq() == [1, 5, 9, 7, 6, 12]


M1 = MoleculeT(1, ElementT.N)
M2 = MoleculeT(2, ElementT.H)
M3 = MoleculeT(3, ElementT.H)
M1Copy = MoleculeT(1, ElementT.N)


def test_get_num_moleculet():
    assert M1.get_num() == 1
    assert M3.get_num() == 3


def test_get_elm_moleculet():
    assert M1.get_elm() == ElementT.N
    assert M2.get_elm() == ElementT.H


def test_num_atoms_moleculet():
    assert M1.num_atoms(ElementT.N) == 1
    assert M2.num_atoms(ElementT.H) == 2
    assert M3.num_atoms(ElementT.P) == 0


def test_constit_elems_moleculet():
    assert M1.constit_elems().equals(ElmSet([ElementT.N]))
    assert M3.constit_elems().equals(ElmSet([ElementT.H]))


def test_equals_moleculet():
    assert not M1.equals(M2)
    assert M1.equals(M1Copy)


C1 = CompoundT([M1])
C2 = CompoundT([M2])
C3 = CompoundT([M1Copy, M3])


def test_get_molec_set_compoundt():
    assert C1.get_molec_set() == [M1]
    assert not C2.get_molec_set() == [M1]


def test_num_atoms_compoundt():
    assert C3.num_atoms(ElementT.H) == 3
    assert C1.num_atoms(ElementT.Pb) == 0
    assert C2.num_atoms(ElementT.N) == 0
    assert C1.num_atoms(ElementT.N) == 1


def test_constit_elems_compoundt():
    assert C3.constit_elems().to_seq() == [ElementT.N, ElementT.H]
    assert not C1.constit_elems().to_seq() == [ElementT.I]


def test_equals_compoundt():
    assert C3.equals(C3)
    assert not C2.equals(C1)


R1 = ReactionT([C1, C2], [C3])

C1 = CompoundT([M1])
C2 = CompoundT([M2])
C3 = CompoundT([M1Copy, M3])

'''In this testing method, I will be testing the following Reaction:
2N + H2 --> 2NH3'''


def test_balancing_reactiont1():
    assert is_balanced([C1, C2], [C3], R1.get_lhs_coeff(), R1.get_rhs_coeff())
    assert pos(R1.get_lhs_coeff())
    assert pos(R1.get_rhs_coeff())
    assert not is_balanced([C1, C2], [C3], [43, 9], R1.get_rhs_coeff())
    assert not pos([-9, 4, -8])


m1 = MoleculeT(1, ElementT.Na)
m2 = MoleculeT(1, ElementT.Cl)
m3 = MoleculeT(1, ElementT.O)
m4 = MoleculeT(1, ElementT.H)
m5 = MoleculeT(2, ElementT.H)

c1 = CompoundT([m1, m3, m4])
c2 = CompoundT([m4, m2])
c3 = CompoundT([m5, m3])
c4 = CompoundT([m1, m2])

R2 = ReactionT([c1, c2], [c3, c4])


def test_balancing_reactiont2():
    assert is_balanced([c1, c2], [c3, c4], R2.get_lhs_coeff(),
    R2.get_rhs_coeff())
