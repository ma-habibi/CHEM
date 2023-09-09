import pandas as pd
from typing import Union
from utils import parse_formula


class Chem:
    def __init__(self):
        self.AVOGADRO = 6.022e23;
        self.elements_df = self.__init_elements_df()

    def __calculate_compound_molarmass(self, compound: str) -> float:
        """Calculates molar_mass of compound"""

        molar_mass = 0.0

        compound_dict = parse_formula(compound) # { "H": 2, "O": 1 , "coefficient": 1 }

        coefficent = compound_dict.pop("coefficent") # remove coefficients

        for key in compound_dict.keys():
            molar_mass += self.elements_df.loc[self.elements_df["Element"] == key]["MolarMass"].values[0] * compound_dict[key]

        return molar_mass * coefficent

    def __init_elements_df(self):
        """Initializes the data frame"""
        
        try:
            df = pd.read_csv("./data.csv")
            return df
        except FileNotFoundError:
            raise FileNotFoundError("failed to load data -> the file is missing.")
        except Exception as e:
            raise Exception(f"failed to load data --> {e}")

    def fahr_to_c(self, f: Union[int, float]) -> float:
        """
        # Converts fahrenheit to celsius
        
        chem = Chem()
        chem.fahr_to_c(32.0) # returns 0.0
        """
        return (f - 32.0) / 1.8

    def c_to_fahr(self, c: Union[int, float]) -> float:
        """
        # Converts celsius to fahrenheit
        
        chem = Chem()
        chem.c_to_fahr(0): # returns 32.0
        """

        return (c * 9.0 / 5.0) + 32.0
   
    def get_atomic_number(self, element: str) -> float:
        """
        # Returns the atomic number based on the element symbol or name

        chem = Chem()
        chem.get_atomic_number('He') # returns 2
        chem.get_atomic_number('Lithium') # returns 3
        """

        field = "Element" if len(element) <= 2 else "Name"

        if element not in self.elements_df[field].values:  # Check for argument
            raise ValueError(f"\n no such {field} -> CHEM.get_atomic_number")

        parameter = self.elements_df[self.elements_df[field] == element]["AtomicNumber"].values[0]

        self.nan(parameter)
        #if pd.isna(parameter):  # Check for Nan
         #   raise Value(
          #      f"\n::No atomic number found for element {element}:: -> CHEM.get_atomic_number()")

        return parameter

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



        if element not in self.elements_df["Element"].values:
            raise ValueError(f"\n no such element -> chem.get_element_density")

        # Accesses data
        parameter = self.elements_df.loc[self.elements_df["Element"] == element]["Density"].values[0]

        # checks for Nan
        self.nan(parameter)
            # if pd.isna(density):  # Check for Nan
        #    raise ValueError(
         #       f"\n::No density found for element {element}:: -> chem.get_element_density()")

        return parameter

    def get_element_molarmass(self, element: str) -> float:
        """
        # Calculates molar_mass of element
        
        chem = Chem()
        chem.get_element_molarmass('He') # returns ~ 4.0
        """

        if element not in self.elements_df["Element"].values:
            raise ValueError("\nno such element -> at chem.get_element_molar_mass")

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

        if element not in self.elements_df["Element"].values:
            raise ValueError(f"\n no such element -> at chem.get_group")

        parameter = self.elements_df.loc[self.elements_df["Element"] == element]["GroupBlock"].values[0]

        self.nan(parameter)
        #if pd.isna(parameter):  # Check for Nan
         #   raise ValueError(
          #      f"\n no block found for element {el} -> at chem.get_group()")

        return parameter
    
    def get_electron_configuration(self, el: str) -> str:
        """
        # Gets Electron configuration of an element
        
        chem = Chem()
        chem.get_electron_configuration("He") # returns "1s2"
        """

        if el not in self.elements_df["Element"].values:
            raise ValueError(f"\n no such element -> chem.get_electron_configuration()")

        parameter = \
        self.elements_df.loc[self.elements_df["Element"] == el]["ElectronConfiguration"].values[0]

        self.nan(parameter)
        #if pd.isna(electron_configuration):  # Check for Nan
         #   raise ValueError(
          #      f"\n no electron configuration found for element {el} -> CHEM.get_electron_configuration()")

        return parameter

    def nan(self, parameter):
        if pd.isna(parameter):
            raise ValueError(f"\n::NAN value encountered ::")
        return parameter

    def WALTERWHITE(self) -> str:
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
            "Say My Name ")

if __name__ == "__main__":
    chem = Chem()


    #print(chem.get_group('klsajf')) # returns Nonmetal
    #print(chem.get_group('He')) # returns Nonmetal
    # a = []
    # a.append("H_2O") # ~ 18.0
    # a.append("CaCl_2") # ~ 110.98

    # for i in a:
    #     print(chem.get_compound_molarmass(i))
    # test values for get_compound_molarmass
    #print(chem.fahr_to_c(110))
    print(chem.get_element_density("He"))