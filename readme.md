# Chem a library for chemical calculations

## Getting Started

To use this program, clone this rep. then integrate any of chem function to your program.

## Usage

### Example

```python
  def main():
    # Creates an instance
    chem = Chem();
    
    # Gets molar mass of water
    print(chem.get_compound_molarmass("H201")
```

## Contributing

If you would like to contribute to this project, please feel free to submit a pull request or open an issue.

## Documentations : 

### Constants :

```python
chem = Chem()

chem.AVOGADRO # returns avogadro constant(6.022e23)
```

### Functions :

```python
chem = Chem() # creates an instance of Chem

"""
takes fahrenheit as input and outputs the amount in celsius.
"""
chem.fahr_to_c(32.0) # returns 0.0

"""
takes celsius as input and outputs the amount in fahrenheit.
"""
chem.c_to_fahr(0): # returns 32.0

"""
calculates the molar mass of an element.
"""
chem.get_element_molarmass('He') # returns ~ 4.0

"""
calculates the molar mass of compound.( calls the helper function calculate_compound_molarmass(compound, i:0, sum:0.0)) 
parameter compound : the input, contains name of the compound. number of atoms must be provided for each element, even if is 1. Example : "H2O1"
"""
chem.get_compound_molarmass("H2O1") # returns ~ 18.0

"""
calculates the number of elementary elements in a given compound.
"""
chem.get_elementary_elements('c', 12.0) # returns 6.022e23

"""
returns group of element symbol
"""
chem.get_group('H') # returns Nonmetal

"""
returns the electron configuration of an element.
"""
chem.get_electron_configuration("He") # returns "1s2"

"""
Takes the number of elementary elements (atoms or compounds) . returns the mass of in grams.
"""
chem.atoms_to_mass(2.35e24, "Cu1") # returns ~ 248
