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
