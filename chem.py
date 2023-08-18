import pandas as pd

class Chem:
    def __init__(self):  # Constructor
        # field variables
        self.AVOGADRO = 6.022e23;
        self.elements_df = self.init_elements_df()

    # Initialize
    def init_elements_df(self):
        try:
            df = pd.read_csv("./data.csv")
            return df
        except FileNotFoundError:
            raise FileNotFoundError("::failed to load data:: -> the file is missing.")
        except Exception as e:
            raise Exception(f"::failed to load data:: --> {e}")

    # Tempreture Conversions
    def fahr_to_c(self, f):
        return (f - 32.0) / 1.8

    def c_to_fahr(self, c):
        return (c * 9.0 / 5.0) + 32.0

    # Molar Mass Calculations
    def get_element_molarmass(self, element):
        # Calculates molar_mass of element
        if element not in self.elements_df["element"].values:
            raise ValueError("\n::NO SUCH ELEMENT:: -> CHEM.get_element_molar_mass")

        return self.elements_df.loc[self.elements_df["element"] == element]["molar_mass"].values[0]

    def get_compound_molarmass(self, compound):
        # Calculates molar_mass of compound
        return self.calculate_compound_molarmass(compound, 0, 0.0)

    def get_elementary_elements(self, compound, element_g):
        # Calculates the number of elementary elements in a compound
        molar_mass = self.get_compound_molarmass(compound)
        return (element_g * self.AVOGADRO) / molar_mass

    def calculate_compound_molarmass(self, compound, i, sum_):
        if i < len(compound):
            # Get name of next element
            elementBuffer = ""
            while i < len(compound) and compound[i].isalpha():
                elementBuffer += compound[i]
                i += 1

            if len(elementBuffer) == 0:
                raise ValueError("\n::NO SUCH ELEMENT:: -> CHEM.calculate_compound_molarmass")

            # Get number of atoms
            atom_count_buffer = ""
            while i < len(compound) and compound[i].isdigit():
                # First read the number of atoms into a string
                atom_count_buffer += compound[i]
                i += 1

            if len(atom_count_buffer) == 0:
                raise ValueError(
                    "\n::YOU MUST ENTER THE NUMBER OF ATOMS, EVEN IF THERE IS ONE (eg : 'H2O1'):: -> CHEM.calculate_compound_molarmass")

            atom_count = int(atom_count_buffer)
            molarmass = self.get_element_molarmass(elementBuffer)

            # Adds the contribution of the molecule to the total molar mass of the compound
            sum_ += (atom_count * molarmass)

            # Recursively calls itself with the new index for compound to read the next molecule
            return self.calculate_compound_molarmass(compound, i, sum_)

        return sum_

    # Get GroupBlock by Element Symbol
    def get_group(self, element):
        if element not in self.elements_df["element"].values:
            raise ValueError("\n::NO SUCH ELEMENT:: -> CHEM.get_group")

        group_block = self.elements_df.loc[self.elements_df["element"] == element]["GroupBlock"].values[0]
        return group_block

    # Electron
    def get_electron_configuration(self, el):
        if el not in self.elements_df["element"].values:
            raise ValueError("\n::NO SUCH ELEMENT:: -> CHEM.get_electron_configuration()")

        electron_configuration = self.elements_df.loc[self.elements_df["element"] == el]["ElectronConfiguration"].values[0]

        if pd.isna(electron_configuration):  # Check for Nan
            raise ElectronConfigurationError(
                f"\n::No electron configuration found for element {el}:: -> CHEM.get_electron_configuration()")

        return electron_configuration

    def WALTERWHITE(self):
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
            "Say My Name ");

