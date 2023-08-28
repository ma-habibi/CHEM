# Chem, python library for chemical calculations

## Getting Started

To use this program, clone this rep. then integrate any of chem function to your program.

## Usage

### Example

```python
if __name__ == "__main__":
  # Creates an instance
  chem = Chem();

  # Gets molar mass of water
  print(chem.get_compound_molarmass("H_2O")
```

## Contributing

If you would like to contribute to this project, please feel free to submit a pull request or open an issue.

## Documentations :

by convention a chemical formula should be passed as argument to methods in the following format:<br> 

<p align="center">H_2O</p>

* of course the first letter of an element is capitalized, second letter is lowercase and the number of atoms of the element is subscripted after the element symbol.

## chem.py :

### Constants :

```python
chem = Chem()

chem.AVOGADRO # returns avogadro constant(6.022e23)
```
### Methods :
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
returns the atomic number of the element based on symbol or name
"""
chem.get_atomic_number('He') # returns 2
chem.get_atomic_number('Lithium') # returns 3

"""
calculates the molar mass of an element.
"""
chem.get_element_molarmass('He') # returns ~ 4.0

"""
calculates the molar mass of compound.( calls the helper private method __calculate_compound_molarmass(compound)
"""
chem.get_compound_molarmass("H_2O") # returns ~ 18.0

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

```

## balance.py
```python
"""
Balances an equation, returns the balanced equation as a string.
"""
balance = Balance("C_4H_10 + O_2", "CO_2 + H_2O") 

balance.str() # -> returns 2C_4H_10 + 13O_2 --> 8C_1O_2 + 10H_2O_1
```
