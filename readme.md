# Chemical Molar Mass Calculator

This program is a console-based application that can calculate the molar mass of a given chemical compound. It can be used to quickly calculate the molar mass of a compound for a chemistry experiment, for example.

## Getting Started

To use this program, you will need to have a C++ compiler installed on your system. Once you have a compiler installed, simply clone this repository and compile the `Chem.cpp` file using your compiler of choice.

## Usage

To use this program, enter the chemical compound as a string in the following format: [Element][Number of atoms][Element][Number of atoms].... For example, the compound for water would be entered as H2O1.
Once you have entered the compound, the program will calculate its molar mass and display the result.

### Example

```cpp
#include<iostream>
#include"Chem"

int main(){
    Chem chem;

    std::string compound;
    std::cout << " ENTER THE COMPOUND : " << std::endl;
    std::cin >> compound;

    long double sum = 0;

    try{
        chem.compoundMolarMass(compound, 0, sum);
        std::cout << std::setprecision(9) << sum << std::endl;
    }
    catch(std::exception &e){
        std::cout << "ERROR::" << e.what() << std::endl;
    }


    return 0;
}
```

## Contributing

If you would like to contribute to this project, please feel free to submit a pull request or open an issue.
