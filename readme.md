# CHEM a library for chemical calculations

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

## Manuals : 

### Variables :

#### Chem.AVOGADRO
returns avogadro constant(6.022e23)

### Functions :

#### unit conversion
> fahr_to_c(f):

    takes fahrenheit as input and outputs the amount in celsius.

> c_to_fahr(c):

    takes celsius as input and outputs the amount in fahrenheit.

> get_element_molarmass(element):

    calculates the molar mass of an element.
> get_compound_molarmass(compound)

    calculates the molar mass of compound.( calls the helper function calculate_compound_molarmass(compound, i:0, sum:0.0) )

    parameter compound : the input, contains name of the compound. number of atoms must be provided for each element, even if is 1.
    Example : "H2O1"
> get_elementary_elements(compound, element_g):

    calculates the number of elementary elements in a given compound.
