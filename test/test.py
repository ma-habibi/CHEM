from context import chem

def test():
    """
    Test the chem module.
    """
    
    c = chem.Chem()
    # write test for all the methods in Chem class
    print(c.get_atomic_number("He")) # 2
    print(c.get_element_density("He")) # 0.0001785
    print(c.get_element_molarmass("He")) # 4.002602
    print(c.get_elementary_elements("He", 4.0)) # 2.0
    print(c.get_compound_molarmass("H_2O")) # 18.01528
    print(c.get_group("He")) # Noble Gas
    print(c.get_electron_configuration("He")) # 1s2
    print(c.atoms_to_mass(2.35e24, "Cu1")) # 248.0
    print(c.fahr_to_c(32.0)) # 0.0
    print(c.c_to_fahr(0.0)) # 32.0

    # write test for all errors to be raised
    try:
        c.get_atomic_number("D")
    except ValueError as e:
        print(e)

    try:
        c.get_element_density("D")
    except ValueError as e:
        print(e)

    try:
        c.get_element_molarmass("D")
    except ValueError as e:
        print(e)

    try:
        c.get_elementary_elements("D", 4.0)
    except ValueError as e:
        print(e)

    try:
        c.get_compound_molarmass("D")
    except ValueError as e:
        print(e)

    try:
        c.get_group("D")
    except ValueError as e:
        print(e)

    try:
        c.get_electron_configuration("D")
    except ValueError as e:
        print(e)

    try:
        c.atoms_to_mass(2.35e24, "D")
    except ValueError as e:
        print(e)

    try:
        c.fahr_to_c("D")
    except ValueError as e:
        print(e)

    try:
        c.WALTERWHITE("ALL TESTS PASSED")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    test()
