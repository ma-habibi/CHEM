import pandas as pd

class Element:
    """Represents an element in the periodic table
    
    attributes: 'element', 'name', 'AtomicNumber', 'Name', 'molar_mass',
       'CPKHexColor', 'ElectronConfiguration', 'Electronegativity',
       'AtomicRadius', 'IonizationEnergy', 'ElectronAffinity',
       'OxidationStates', 'StandardState', 'MeltingPoint', 'BoilingPoint',
       'Density', 'GroupBlock', 'YearDiscovered'
    """
    
    def __init__(self):
        pass 
    
    @classmethod
    def create_element_object(cls, i, df):
        elem = Element()
        elem.element = df['element'][i]
        for attr in df.columns:
            setattr(elem, attr, df[attr][i])
        return elem

    @classmethod
    def create_all_element_objects(cls):
        df = pd.read_csv("CHEM/data.csv")
        for i in range(len(df)):
            ele = cls.create_element_object(i, df)
            globals()[ele.element] = ele
        
    def is_more_electronegative(self, element2):
        return self.Electronegativity > element2.Electronegativity
    
    def __str__(self):
        return self.name
    


Element.create_all_element_objects()


print(F.is_more_electronegative(O))

print(F)