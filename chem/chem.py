import pandas as pd
from typing import Union

if __name__ == "__main__":
    from parse_formula import parse_formula
else:
    from .parse_formula import parse_formula


class Chem:
    def __init__(self):
        self.AVOGADRO = 6.022e23;
        self.elements_df = self.__init_elements_df()

    def __check_nan_value(self, parameter, msg, method_name):
        """Checks if the parameter is a Nan value"""

        if pd.isna(parameter):
            raise ValueError(f"\n {msg}  -> at {method_name}")

    def __check_for_element(self, element, method_name):
        """Checks if the element is in the data frame"""

        if element not in self.elements_df["Element"].values:
            raise ValueError(f"\n no such element -> chem.{method_name}")

    def __calculate_compound_molarmass(self, compound: str) -> float:
        """Calculates molar_mass of compound"""

        molar_mass = 0.0

        compound_dict = parse_formula(compound)  # { "H": 2, "O": 1 , "coefficient": 1 }

        coefficient = compound_dict.pop("coefficent")  # remove coefficients

        for key in compound_dict.keys():
            self.__check_for_element(key, "__calculate_compound_molarmass")

        for key in compound_dict.keys():
            molar_mass += self.elements_df.loc[self.elements_df["Element"] == key]["MolarMass"].values[0] * compound_dict[key]

        return molar_mass * coefficient

    def __init_elements_df(self):
        """Initializes the data frame"""

        try:
            # fix path 
            df = pd.read_csv("chem/data.csv")
            return df
        except FileNotFoundError:
            raise FileNotFoundError("failed to load data -> the file is missing.")
        except Exception as e:
            raise Exception(f"failed to load data --> {e}")

    def fahr_to_c(self, f: Union[int, float]) -> float:
        """
        # Converts Fahrenheit to celsius
        
        chem = Chem()
        chem.fahr_to_c(32.0) # returns 0.0
        """

        if not isinstance(f, (int, float)):
            raise ValueError("\n fahr_to_c() -> f must be a number")
        
        return (f - 32.0) / 1.8

    def c_to_fahr(self, c: Union[int, float]) -> float:
        """
        # Converts celsius to fahrenheit
        
        chem = Chem()
        chem.c_to_fahr(0): # returns 32.0
        """

        if not isinstance(c, (int, float)):
            raise ValueError("\n c_to_fahr() -> c must be a number")

        return (c * 9.0 / 5.0) + 32.0

    def get_atomic_number(self, element: str) -> float:
        """
        # Returns the atomic number based on the element symbol or name

        chem = Chem()
        chem.get_atomic_number('He') # returns 2
        chem.get_atomic_number('Lithium') # returns 3
        """

        field = "Element" if len(element) <= 2 else "Name"

        self.__check_for_element(element, "get_atomic_number")

        atomic_number = self.elements_df[self.elements_df[field] == element]["AtomicNumber"].values[0]

        error_message = f"no atomic number found for element {element}"
        method_name = f"chem.get_atomic_number()"
        self.__check_nan_value(atomic_number, error_message, method_name)

        return atomic_number

    def atoms_to_mass(self, quantity: int, chemical: str) -> float:
        """
        # Takes the number of elementary elements (atoms or compounds), returns the mass of in grams

        chem = Chem()
        chem.atoms_to_mass(2.35e24, "Cu1") # returns ~ 248
        """

        molar_mass = self.get_compound_molarmass(chemical)

        return (quantity * molar_mass) / self.AVOGADRO

    def get_element_density(self, element: str) -> float:
        """
        chem = Chem()
        chem.get_element_density("He") # returns ~ 0.0001785
        """

        self.__check_for_element(element, "get_element_density")

        # Accesses data
        density = self.elements_df.loc[self.elements_df["Element"] == element]["Density"].values[0]

        # checks for Nan
        error_message = f"no density found for element {element}"
        method_name = f"chem.get_element_density()"
        self.__check_nan_value(density, error_message, method_name)

        return density

    def get_element_molarmass(self, element: str) -> float:
        """
        # Calculates molar_mass of element
        
        chem = Chem()
        chem.get_element_molarmass('He') # returns ~ 4.0
        """

        self.__check_for_element(element, "get_element_molarmass")
        # if element not in self.elements_df["Element"].values:
        #   raise ValueError("\nno such element -> at chem.get_element_molar_mass")

        return self.elements_df.loc[self.elements_df["Element"] == element]["MolarMass"].values[0]

    def get_elementary_elements(self, compound: str, element_g: Union[int, float]) -> float:
        """
        # Calculates the number of elementary elements in a compound
        
        chem = Chem()
        chem.get_elementary_elements('c', 12.0) # returns 6.022e23
        """

        molar_mass = self.get_compound_molarmass(compound)
        return (element_g * self.AVOGADRO) / molar_mass

    def get_compound_molarmass(self, compound: str) -> float:
        """
        # Returns molar_mass of compound
        
        chem = Chem()
        a = []
        a.append("H_2O") # ~ 18.0
        a.append("CaCl_2") # ~ 110.98

        for i in a:
            print(chem.get_compound_molarmass(i))
        """

        return self.__calculate_compound_molarmass(compound)

    def get_group(self, element: str) -> str:
        """
        # Get group of element symbol
         
        chem = Chem()
        chem.get_group('H') # returns Nonmetal
        """

        self.__check_for_element(element, "get_group")

        group_block = self.elements_df.loc[self.elements_df["Element"] == element]["GroupBlock"].values[0]

        error_message = f"no block found for element {element}"
        method_name = f"chem.get_group()"
        self.__check_nan_value(group_block, error_message, method_name)

        return group_block

    def get_electron_configuration(self, el: str) -> str:
        """
        # Gets Electron configuration of an element
        
        chem = Chem()
        chem.get_electron_configuration("He") # returns "1s2"
        """

        self.__check_for_element(el, "get_electron_configuration")

        electron_configuration = self.elements_df.loc[
                self.elements_df["Element"] == el]["ElectronConfiguration"].values[0]

        error_message = f"no electron configuration found for element {el}"
        method_name = f"CHEM.get_electron_configuration()"
        self.__check_nan_value(electron_configuration, error_message, method_name)

        return electron_configuration

    def WALTERWHITE(self, message: str="say my name"):
        print(
            " ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n" +
            " ⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n" +
            " ⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n" +
            " ⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n" +
            " ⣿⣿⣿⣿⠿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿\n" +
            " ⣿⣿⡏⠁⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣦⣤⡄⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿\n" +
            " ⣿⣿⣷⣄⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡧⠇⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿\n" +
            " ⣿⣿⣿⣿⣿⣿⣾⣮⣭⣿⡻⣽⣒⠀⣤⣜⣭⠐⢐⣒⠢⢰⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿\n" +
            " ⣿⣿⣿⣿⣿⣿⣿⣏⣿⣿⣿⣿⣿⣿⡟⣾⣿⠂⢈⢿⣷⣞⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿\n" +
            " ⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣷⣶⣾⡿⠿⣿⠗⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n" +
            " ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⠋⠉⠑⠀⠀⢘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n" +
            " ⣿⣿⣿⣿⣿⣿⣿⡿⠟⢹⣿⣿⡇⢀⣶⣶⠴⠶⠀⠀⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n" +
            " ⣿⣿⣿⣿⣿⣿⡿⠀⠀⢸⣿⣿⠀⠀⠣⠀⠀⠀⠀⠀⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n" +
            " ⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠹⣿⣧⣀⠀⠀⠀⠀⡀⣴⠁⢘⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿\n" +
            " ⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⠗⠂⠄⠀⣴⡟⠀⠀⡃⠀⠉⠉⠟⡿⣿⣿⣿⣿\n" +
            "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠾⠛⠂⢹⠀⠀⠀⢡⠀⠀⠀⠀⠀⠙⠛⠿⢿\n\n" +
            f"{message} ")


if __name__ == "__main__":
    """
    Test the chem module.
    """
    
    c = Chem()
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

