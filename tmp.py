
l = [{'Na': 3, 'Po': 1, 'coefficent': '2'}, {'Mg': 1, 'Cl' : 2, 'coefficent': '3'}]
r = [{'Na': 1, 'Cl': 1, 'coefficent': '6'}, {'Mg': 3, 'Po': 2, 'coefficent': '1'}]

tmp = dict()

for formula in l:
    coefficent = int(formula.pop("coefficent", None))

    for element in formula.keys():
        if element not in tmp:
            tmp[element] = 0

        tmp[element] += formula[element] * coefficent

for formula in r:
    coefficent = int(formula.pop("coefficent", None))

    for element in formula.keys():
        tmp[element] -= formula[element] * coefficent

print(tmp)
print(max(tmp.values()) == 0)
