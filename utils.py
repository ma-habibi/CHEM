import typing

def parse_formula(x: str) -> typing.Dict[str, int]:
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
