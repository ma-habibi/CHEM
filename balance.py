class Balance:
    def __init__(self, left_side, right_side):
        self.left_side = left_side
        self.right_side = right_side

        self.balanced_equation = self.__get_balanced()

        # print(self.__parse_formula("H_2O")

    def str(self):
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

        return left_formulas_parsed, right_formulas_parsed
        
        # Balance
        
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
    balance = Balance("2NH_3 + 5O_2", "2NO + 3H_2O")
    print(balance.str())
