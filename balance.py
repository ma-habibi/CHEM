import numpy as np
import copy as cp

class Balance:
    def __init__(self, left_side, right_side):
        """
        left_side: string of the left side of the equation
        right_side: string of the right side of the equation
        left_tables: list of dictionaries of the left side of the equation
        right_tables: list of dictionaries of the right side of the equation
        elements: set of elements in the equation
        balanced_equation: tuple of the balanced left and right side of the equation
        """

        self.left_side = left_side
        self.right_side = right_side
        self.left_tables = []
        self.right_tables = []
        self.elements = set()
        self.__initialize()
        print("in")
        print(f"{left_side} --> {right_side}")
        print("out")
        self.balanced_equation = self.__get_balanced()

    def __initialize(self):
        """
        initializes the fields of the class
        """

        left_formulas = self.left_side.split(" ")
        left_formulas = [formula for formula in left_formulas if formula != '+']

        right_formulas = self.right_side.split(" ")
        right_formulas = [formula for formula in right_formulas if formula != '+']

        for formula in left_formulas:
            self.left_tables.append(self.__parse_formula(formula))

        for formula in right_formulas:
            self.right_tables.append(self.__parse_formula(formula))

        for t in self.left_tables:
            keys = t.keys()
            for k in keys:
                if k == "coefficent":
                    continue

                self.elements.add(k)

        for t in self.left_tables:
            keys = t.keys()
            for k in keys:
                if k == "coefficent":
                    continue

                self.elements.add(k)

    def __calculate_balanced(self):
        """
        calculates the balanced equation
        """

        left_formulas_parsed = self.left_tables
        right_formulas_parsed = self.right_tables

        while not self.__is_balanced(left_formulas_parsed, right_formulas_parsed):
            equation = (left_formulas_parsed, right_formulas_parsed)
            for element in self.elements:
                self.__balance_element(element, equation)
                self.__balance_element(element, equation)
                self.__balance_element(element, equation)

        # uncomment for debug
        # print(self.__is_balanced(left_formulas_parsed, right_formulas_parsed)) # DEBUG

        return left_formulas_parsed, right_formulas_parsed

    def __balance_element(self, element, d):
        """
        balances the element in the equation
        """

        # access formula
        lefts = np.array([])
        left_co = np.array([])
        rights = np.array([])
        right_co = np.array([])
    
        for a in d[0]:
            if element in a.keys():
                lefts = np.append(lefts, np.int32(a[element]))
                left_co = np.append(left_co, np.int32(a['coefficent']))
        
        for a in d[1]:
            if element in a.keys():
                rights = np.append(rights, np.int32(a[element]))
                right_co = np.append(right_co, np.int32(a['coefficent']))
    
        # Algortithm to balance element
        if np.dot(rights, right_co) == np.dot(lefts, left_co):
            return
    
        low = (100000, 10000) # DEBUG
        start = target = 0
    
        if np.dot(lefts, left_co) > np.dot(rights, right_co):
            for i in range(len(right_co)):
                right_co_cp = cp.copy(right_co)
                while np.dot(lefts, left_co) > np.dot(rights, right_co_cp):
                    right_co_cp[i] += 1
    
                new_low = (np.dot(rights, right_co_cp) - np.dot(lefts, left_co), (right_co_cp[i] - right_co[i]))
    
                if new_low < low:
                    low = new_low
                    index = i
                    target = right_co_cp[i]
    
            # uncomment for debug
            # print(f"the least big is if {right_co[index]} goes to -> {target} the diff would be {low}")
            right_co[index] = target
    
        elif np.dot(lefts, left_co) < np.dot(rights, right_co):
            for i in range(len(left_co)):
                left_co_cp = cp.copy(left_co)
                while np.dot(lefts, left_co_cp) < np.dot(rights, right_co):
                    left_co_cp[i] += 1
    
                new_low = (np.dot(lefts, left_co_cp) - np.dot(rights, right_co), (left_co_cp[i] - left_co[i]))
    
                if new_low < low:
                    low = new_low
                    index = i
                    target = left_co_cp[i]
    
            # uncomment for debug
            # print(f"the least big is if {left_co[index]} goes to -> {target} the diff would be {low}")
    
            left_co[index] = target
    
        # put formula back
        l_c = [each for each in left_co] # using python list to do FIFO
        r_c = [each for each in right_co]
    
        for a in d[0]:# left hand side
            if element in a.keys():
                a['coefficent'] = l_c.pop(0)
        
        for a in d[1]:# right hand side
            if element in a.keys():
                a['coefficent'] = r_c.pop(0)

    def __is_balanced(self, l, r):
        """
        checks if the equation is balanced
        """

        for element in self.elements:
            if not self.__is_element_balanced(element, (l, r)):
                return False

        return True

    def __is_element_balanced(self, element, d):
        """
        checks if the element is balanced for example 
        if quantity of 'O' in right side == quantity of 'O' in left side
        """

        # access formula
        lefts = np.array([])
        left_co = np.array([])
        rights = np.array([])
        right_co = np.array([])
    
        for a in d[0]:
            if element in a.keys():
                lefts = np.append(lefts, np.int32(a[element]))
                left_co = np.append(left_co, np.int32(a['coefficent']))
        
        for a in d[1]:
            if element in a.keys():
                rights = np.append(rights, np.int32(a[element]))
                right_co = np.append(right_co, np.int32(a['coefficent']))
    
        # Algortithm to balance element
        if np.dot(rights, right_co) == np.dot(lefts, left_co):
            return True
    
        return False
            
    def __get_balanced(self):
        """
        calls the function to calculate the balanced equation
        """

        return self.__calculate_balanced()

    def __parse_formula(self, x):
        """
        takes formula as string and returns a dictionary of the elements and their quantity
        in this format {element: quantity, element: quantity, coefficent: coefficent}
        eg : {'H': 2, 'O': 1, 'coefficent': 2}
        """

        i = 0
        
        left_side_table = dict()

        coefficents = list()
        
        while(i < len(x)):
            elements = list()
            numeric_buffer = ""
            quantity_buffer = ""
            alpha_buffer   = ""
        
            while(i < len(x) and x[i].isspace()):
                i += 1
        
            while(i < len(x) and x[i].isnumeric()):
                numeric_buffer += x[i]
                i += 1
        
            while(i < len(x) and x[i].isalpha()):
                if x[i].isupper() and alpha_buffer:
                    elements.append(alpha_buffer)
                    alpha_buffer = ""

                alpha_buffer += x[i]
                i += 1
        
            # check for subscript
            if(i < len(x) and x[i] == '_'):
                if alpha_buffer:
                    elements.append(alpha_buffer)
                    alpha_buffer = ""

                i += 1

                while(i < len(x) and x[i].isnumeric()):
                    quantity_buffer += x[i]
                    i += 1

            if alpha_buffer:
                elements.append(alpha_buffer)

            coefficents.append(numeric_buffer)
            subscript  = quantity_buffer

            for element in elements:
                if element:
                    if element not in left_side_table:
                        left_side_table[element] = 0

            if subscript and elements[-1]:# adds subscript only to the last element
                left_side_table[elements[-1]] += int(subscript)

        left_side_table["coefficent"] = max(coefficents)
        if not left_side_table["coefficent"]:
            left_side_table["coefficent"] = 1

        for element in elements:
            if left_side_table[element] == 0:
                left_side_table[element] = 1

        return left_side_table

    def str(self):
        """
        returns a formated string of the balanced equation
        """

        equation = self.balanced_equation
        output = ""

        i = 0
        for left in equation[0]:
            coefficent = left.pop("coefficent", None)
            output += str(coefficent)

            keys = left.keys()
            for k in keys:
                output += f"{k}_{left[k]}"

            if not i == len(equation[0]) - 1:
                output += " + "

            i += 1

        output += " ---> "

        i = 0
        for right in equation[1]:
            coefficent = right.pop("coefficent", None)
            output += str(coefficent)

            keys = right.keys()
            for k in keys:
                output += f"{k}_{right[k]}"

            if not i == len(equation[1]) - 1:
                output += " + "

            i += 1

        return output
    
if __name__ == "__main__": # DEBUG
    test = []
    test.append(("C_4H_10 + O_2", "CO_2 + H_2O"))
    test.append(("Al + HCl", "AlCl_3 + H_2"))
    test.append(("Ga + CuBr_2", "GaBr_3 + Cu"))
    test.append(("I_2 + F_2", "IF_7"))
    test.append(("SO_2 + O_2", "SO_3"))
    test.append(("Na + S_8", "Na_2S"))
    for each in test:
        balance = Balance(each[0], each[1])
        print(balance.str())
