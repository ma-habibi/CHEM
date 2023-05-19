import java.util.HashMap;
import java.util.Map;

class Chem{
  //Walter White
  public void getWalterWhite(){
  System.out.println(
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
  }

  //Fields
  Map<String, Double> table_map = new HashMap<>();

  //Constatns
  double AVOGADRO = 6.022e23;

  //Tempreture Conversion
  public double convertFToC(double f){
      return ( f - 32.0 ) / 1.8;
  }
  public double convertCToF(double c){
      return ( c * 9.0 / 5.0 ) + 32.0;
  }

  public double getElementMolarMass(String compound_name) {
    /* Returns molar mass of element. */
    if(!table_map.containsKey(compound_name)){
      throw new IllegalArgumentException("\n::NO SUCH ELEMENT:: -> CHEM.getElementMolarMass ");
    }

    return table_map.get(compound_name);
  }

  public double getCompoundMolarMass(String compound,int i, double sum){
    if(i < compound.length()){
  
      //Accesses element name
      String element = "";
      while(Character.isUpperCase(compound.charAt(i)) || Character.isLowerCase(compound.charAt(i))){//Checks if char is alphabetical 
          element += compound.charAt(i);//Reads from input to temp_element charactar by charactar
          i++;//Increments i when compound.charAt(i) is read.
      }

      if(element.length() == 0){
        throw new IllegalArgumentException("\n::WRONG INPUT.:: -> CHEM.getCompoundMolarMass ");
      }
  
      //accesses number of atoms
      String atoms_count_buffer = "";
      while (i < compound.length() && compound.charAt(i) >= '0' && compound.charAt(i) <= '9'){
        //First read the number of atom into a string
        atoms_count_buffer += compound.charAt(i);
        i++;
      }
      if(atoms_count_buffer.length() == 0){
        throw new IllegalArgumentException("\n::YOU MUST ENTER THE NUMBER OF ATOMS, EVEN IF THERE IS ONE (eg : 'H2O1'):: -> CHEM.getCompoundMolarMass ");
      }
      short atoms_count = Short.parseShort(atoms_count_buffer);//Parses the number of atoms to short

      double molar_mass = getElementMolarMass(element);//gets molar_mass of element
      
      //Adds the contribution of molecule to total molar mass of compound
      sum += (atoms_count * molar_mass);
  
      //Recursively calls itself with new index for compound to read next molecule
      getCompoundMolarMass(compound, i, sum);
    }
    return sum;//Handles the base case 
  }

  public double getElementryElements(String compound, double element_g){
    //Caculates number of elementary elements
    double molar_mass = getCompoundMolarMass(compound, 0, 0.0);
    return (element_g * AVOGADRO)/molar_mass;
  }

  private void initElementsMap(){
      //Elemet-molar mass key-value pair stored in a linked hash map.
      table_map.put("H", 1.008);  table_map.put("He", 4.003); table_map.put("Li", 6.941);
      table_map.put("Be", 9.012); table_map.put("B", 10.81);  table_map.put("C", 12.01);
      table_map.put("N", 14.01);  table_map.put("O", 16.00);  table_map.put("F", 19.00);
      table_map.put("Ne", 20.18); table_map.put("Na", 22.99); table_map.put("Mg", 24.31);
      table_map.put("Al", 26.98); table_map.put("Si", 28.09); table_map.put("P", 30.97);
      table_map.put("S", 32.07);  table_map.put("Cl", 35.45); table_map.put("K", 39.10);
      table_map.put("Ar", 39.95); table_map.put("Ca", 40.08); table_map.put("Sc", 44.96);
      table_map.put("Ti", 47.87); table_map.put("V", 50.94);  table_map.put("Cr", 52.00);
      table_map.put("Mn", 54.94); table_map.put("Fe", 55.85); table_map.put("Co", 58.93);
      table_map.put("Ni", 58.69); table_map.put("Cu", 63.55); table_map.put("Zn", 65.38);
      table_map.put("Ga", 69.72); table_map.put("Ge", 72.63); table_map.put("As", 74.92);
      table_map.put("Se", 78.96); table_map.put("Br", 79.90); table_map.put("Kr", 83.80);
      table_map.put("Rb", 85.47); table_map.put("Sr", 87.62); table_map.put("Y", 88.91);
      table_map.put("Zr", 91.22); table_map.put("Nb", 92.91); table_map.put("Mo", 95.94);
      table_map.put("Tc", 98.00); table_map.put("Ru", 101.1); table_map.put("Rh", 102.9);
      table_map.put("Pd", 106.4); table_map.put("Ag", 107.9); table_map.put("Cd", 112.4);
      table_map.put("In", 114.8); table_map.put("Sn", 118.7); table_map.put("Sb", 121.8);
      table_map.put("I", 126.9);  table_map.put("Te", 127.6); table_map.put("Xe", 131.3);
      table_map.put("Cs", 132.9); table_map.put("Ba", 137.3); table_map.put("La", 138.9);
      table_map.put("Ce", 140.1); table_map.put("No", 259.0); table_map.put("Lr", 262.0);
      table_map.put("Pr", 140.9); table_map.put("Nd", 144.2); table_map.put("Pm", 145.0);
      table_map.put("Sm", 150.4); table_map.put("Eu", 152.0); table_map.put("Gd", 157.3);
      table_map.put("Tb", 158.9); table_map.put("Dy", 162.5); table_map.put("Ho", 164.9);
      table_map.put("Er", 167.3); table_map.put("Tm", 168.9); table_map.put("Yb", 173.1);
      table_map.put("Lu", 175.0); table_map.put("Hf", 178.5); table_map.put("Ta", 180.9);
      table_map.put("W", 183.8);  table_map.put("Re", 186.2); table_map.put("Os", 190.2);
      table_map.put("Ir", 192.2); table_map.put("Pt", 195.1); table_map.put("Au", 197.0);
      table_map.put("Hg", 200.6); table_map.put("Tl", 204.4); table_map.put("Pb", 207.2);
      table_map.put("Bi", 208.9); table_map.put("Th", 232.0); table_map.put("Pa", 231.0);
      table_map.put("U", 238.0);  table_map.put("Np", 237.0); table_map.put("Pu", 244.0);
      table_map.put("Am", 243.0); table_map.put("Cm", 247.0); table_map.put("Bk", 247.0);
      table_map.put("Cf", 251.0); table_map.put("Es", 252.0); table_map.put("Fm", 257.0);
      table_map.put("Md", 258.0);  
      table_map.put("Rf", 267.0);
  }

  Chem(){//Constructore
    initElementsMap();//Initializes elements table
  }
}

