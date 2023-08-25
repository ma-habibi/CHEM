import numpy as np
import copy as cp

class Balance:
    def __init__(self, left_side, right_side):
        self.left_side = left_side
        self.right_side = right_side

        print("in")
        print(f"{left_side} --> {right_side}")
        print("out")
        self.balanced_equation = self.__get_balanced()

    def str(self):
        """
        returns a formated string of the balanced equation
        """
        equation = self.balanced_equation
        output = ""
        for left in equation[0]:
            coefficent = left.pop("coefficent", None)
            output += str(coefficent)

            keys = left.keys()
            for k in keys:
                output += f"{k}_{left[k]}"

            output += " + "

        output += " ---> "

        for right in equation[1]:
            coefficent = right.pop("coefficent", None)
            output += str(coefficent)

            keys = right.keys()
            for k in keys:
                output += f"{k}_{right[k]}"

            output += " + "

        return output

    def __is_element_balanced(self, element, d):
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
        return self.__calculate_balanced()

    def __balance_element(self, element, d):
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
    
        low = (100000, 10000)
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
    
            print(f"the least big is if {right_co[index]} goes to -> {target} the diff would be {low}")
    
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
    
            print(f"the least big is if {left_co[index]} goes to -> {target} the diff would be {low}")
    
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
    
    def __calculate_balanced(self):
        # Parse and balance the formulas

        left_formulas = self.left_side.split(" ")
        left_formulas = [formula for formula in left_formulas if formula != '+']

        right_formulas = self.right_side.split(" ")
        right_formulas = [formula for formula in right_formulas if formula != '+']

        left_formulas_parsed = list() # list of dicts
        right_formulas_parsed = list()

        for formula in left_formulas:
            left_formulas_parsed.append(self.__parse_formula(formula))

        for formula in right_formulas:
            right_formulas_parsed.append(self.__parse_formula(formula))

        while not self.__is_balanced(left_formulas_parsed, right_formulas_parsed):
            equation = (left_formulas_parsed, right_formulas_parsed)
            self.__balance_element('C', equation)
            self.__balance_element('H', equation)
            self.__balance_element('O', equation)

        print(self.__is_balanced(left_formulas_parsed, right_formulas_parsed))

        return left_formulas_parsed, right_formulas_parsed

    def __is_balanced(self, l, r):
        return self.__is_element_balanced('O', (l, r)) and self.__is_element_balanced('C', (l, r)) and self.__is_element_balanced('H', (l, r))
        # Returns True if formula is balanced
        # tmp = dict()
        # 
        # for formula in l:
        #     # coefficent = int(formula.pop("coefficent", None))
        # 
        #     for element in formula.keys():
        #         if element == "coefficent":
        #             continue

        #         if element not in tmp:
        #             tmp[element] = 0
        # 
        #         tmp[element] += formula[element] * int(formula["coefficent"])
        # 
        # for formula in r:
        #     # coefficent = int(formula.pop("coefficent", None))
        # 
        #     for element in formula.keys():
        #         if element == "coefficent":
        #             continue

        #         tmp[element] -= formula[element] * int(formula["coefficent"])
        # 
        # return max(tmp.values()) == 0
        
    def __parse_formula(self, x):
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
    
if __name__ == "__main__":
    balance = Balance("2C_3H_8 + 15O_2", "6CO_2 + 8H_2O")
    balance = Balance("2C + 25O_2", "2CO")
    #balance = Balance("O + 2O_3 + 4OK", "O + K")
    print(balance.str())
