class Balance:
    def __init__(self, left_side, right_side):
        self.left_side = left_side
        self.right_side = right_side
        self.balanced_equation = self.__get_balanced()

    def str(self):
        """
        returns a formated string of the balanced equation
        """
        return self.balanced_equation

    def __get_balanced(self):
        return self.__calculate_balanced()
    
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


        # TODO
        # while not equation balance:
            # if not element_balanced(C):
                # balance c
            # if not element_balance(O):
                # balance o
        # return equation


        while not self.__is_balanced(left_formulas_parsed, right_formulas_parsed):
            # self.__is_element_balanced()
            pass
        
        return left_formulas_parsed, right_formulas_parsed

        # Balance

    def __is_balanced(self, l, r):
        # Returns True if formula is balanced
        tmp = dict()
        
        for formula in l:
            # coefficent = int(formula.pop("coefficent", None))
        
            for element in formula.keys():
                if element == "coefficent":
                    continue

                if element not in tmp:
                    tmp[element] = 0
        
                tmp[element] += formula[element] * int(formula["coefficent"])
        
        for formula in r:
            # coefficent = int(formula.pop("coefficent", None))
        
            for element in formula.keys():
                if element == "coefficent":
                    continue

                tmp[element] -= formula[element] * int(formula["coefficent"])
        
        return max(tmp.values()) == 0
        
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
    balance = Balance("1C_3H_8 + 5O_2", "3CO_2 + 4H_2O")
    # balance = Balance("2C + O_2", "2CO")
    print(balance.str())
