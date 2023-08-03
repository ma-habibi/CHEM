class Chem:

    def __init__(self): # Constructor
        # field variables
        self.AVOGADRO = 6.022e23;
        self.molarMassTable = self.init_molarmass_table()

    # Initialize
    def init_molarmass_table(self):
        molarMassTable = dict()

        # {Elemet : molarmass} key-value pair stored in hash table.
        molarMassTable = {
            "H": 1.008, "He": 4.003, "Li": 6.941, "Be": 9.012, "B": 10.81, "C": 12.01, "N": 14.01, "O": 16.00,
            "F": 19.00, "Ne": 20.18, "Na": 22.99, "Mg": 24.31, "Al": 26.98, "Si": 28.09, "P": 30.97, "S": 32.07,
            "Cl": 35.45, "K": 39.10, "Ar": 39.95, "Ca": 40.08, "Sc": 44.96, "Ti": 47.87, "V": 50.94, "Cr": 52.00,
            "Mn": 54.94, "Fe": 55.85, "Co": 58.93, "Ni": 58.69, "Cu": 63.55, "Zn": 65.38, "Ga": 69.72, "Ge": 72.63,
            "As": 74.92, "Se": 78.96, "Br": 79.90, "Kr": 83.80, "Rb": 85.47, "Sr": 87.62, "Y": 88.91, "Zr": 91.22,
            "Nb": 92.91, "Mo": 95.94, "Tc": 98.00, "Ru": 101.1, "Rh": 102.9, "Pd": 106.4, "Ag": 107.9, "Cd": 112.4,
            "In": 114.8, "Sn": 118.7, "Sb": 121.8, "I": 126.9, "Te": 127.6, "Xe": 131.3, "Cs": 132.9, "Ba": 137.3,
            "La": 138.9, "Ce": 140.1, "Pr": 140.9, "Nd": 144.2, "Pm": 145.0, "Sm": 150.4, "Eu": 152.0, "Gd": 157.3,
            "Tb": 158.9, "Dy": 162.5, "Ho": 164.9, "Er": 167.3, "Tm": 168.9, "Yb": 173.1, "Lu": 175.0, "Hf": 178.5,
            "Ta": 180.9, "W": 183.8, "Re": 186.2, "Os": 190.2, "Ir": 192.2, "Pt": 195.1, "Au": 197.0, "Hg": 200.6,
            "Tl": 204.4, "Pb": 207.2, "Bi": 208.9, "Th": 232.0, "Pa": 231.0, "U": 238.0, "Np": 237.0, "Pu": 244.0,
            "Am": 243.0, "Cm": 247.0, "Bk": 247.0, "Cf": 251.0, "Es": 252.0, "Fm": 257.0, "Md": 258.0, "Rf": 267.0,
        }
    
        return molarMassTable

    # Tempreture Conversions
    def fahr_to_c(self, f):
        return ( f - 32.0 ) / 1.8

    def c_to_fahr(self, c):
        return ( c * 9.0 / 5.0 ) + 32.0

    # Molar Mass Calculations
    def get_element_molarmass(self, element):
        # Calculates molar_mass of element
        """Returns molar mass of an element."""
        if element not in self.molarMassTable:
            raise ValueError("\n::NO SUCH ELEMENT:: -> CHEM.get_element_molar_mass")
    
        return self.molarMassTable[element]

    def get_compound_molarmass(self, compound):
        # Calculates molar_mass of compound 
        return self.calculate_compound_molarmass(compound, 0, 0.0)

    def get_elementary_elements(self, compound, element_g): 
        # Calculates the number of elementary elements in a compound
        molar_mass = self.get_compound_molarmass(compound)
        return (element_g * self.AVOGADRO)/molar_mass

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


    # Easter eggs
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
          "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠾⠛⠂⢹⠀⠀⠀⢡⠀⠀⠀⠀⠀⠙⠛⠿⢿\n\n"+
          "Say My Name ");
