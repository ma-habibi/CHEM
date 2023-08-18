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

"""takes fahrenheit as input and outputs the amount in celsius."""
 chem.fahr_to_c(f)


"""takes celsius as input and outputs the amount in fahrenheit."""
chem.c_to_fahr(c): 


"""calculates the molar mass of an element."""
chem.get_element_molarmass(element) 


"""calculates the molar mass of compound.( calls the helper function calculate_compound_molarmass(compound, i:0, sum:0.0)) 
parameter compound : the input, contains name of the compound. number of atoms must be provided for each element, even if is 1. Example : "H2O1"
"""
chem.get_compound_molarmass(compound)


"""calculates the number of elementary elements in a given compound."""
chem.get_elementary_elements(compound, element_g)


"""returns the electron configuration of an element."""
chem.get_electron_configuration(el)
