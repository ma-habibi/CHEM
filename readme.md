# CHEM a library for chemical calculations

## Getting Started

To use this program, clone this rep. then integrate any of chem function to your program.

## Usage

### Example

```java
  public static void main(String[] args){
    Chem chem = new Chem();//create an instance of Chem
    
    System.out.println(chem.getCompoundMolarMass("H2O1", 0, 0.0));//print out the molar mass of H2O
    
    return;
  }

```

## Contributing

If you would like to contribute to this project, please feel free to submit a pull request or open an issue.
(for classmates and other students at nis. university, if you want to contribute to this project as a part of your chemistry course activity,
but you are not sure how you can help this project feel free to message me.)

## MANUALS : 

### Variables :

#### Chem.AVOGADRO
returns avogadro constant(6.022e23)

### Functions :

#### Chem.compoundMolarMass(string compound,int i,double sum)
'Calculates the molar mass of a compound.'

-param String compound : the input, contains name of the compound. number of atoms must be provided for each element, even if is 1.
Example : "H2O1"
-param int i : index to read from the the compound.must be initially set to 0.
-param double sum : stores the sum of mass of each elements.
-return a double, the molar mass of given compound.

#### Chem.getElementryElements(String compound, double element_g)
'Calculates the number of elementary elements in a given compound.'

-param String compound : The compound formula as a string, containing the name of the compound.
Example: "H2O1"
-param double element_g : The mass of the elementary element in grams.
-return a double, The number of elementary elements in the compound.
