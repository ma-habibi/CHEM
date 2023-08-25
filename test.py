import numpy as np
import copy as cp

def main():
    # d = ([{'C': 3, 'H': 8, 'coefficent': '2'}, {'O': 2, 'coefficent': '15'}], [{'C': 1, 'O': 2, 'coefficent': '6'}, {'H': 2, 'O': 1, 'coefficent': '8'}])
    d = ([{'C': 1, 'coefficent': '2'}, {'O': 2, 'coefficent': '25'}], [{'C': 1, 'O': 1, 'coefficent': '2'}])
    d = ([{'O': 1, 'coefficent': 1}, {'O': 3, 'coefficent': '2'}, {'O': 1, 'K': 1, 'coefficent': '4'}], [{'O': 1, 'coefficent': 1}, {'K': 1, 'coefficent': 1}])

    print(d)

    # access formula 
    lefts = np.array([])
    left_co = np.array([])
    rights = np.array([])
    right_co = np.array([])

    for a in d[0]:
        if 'O' in a.keys():
            lefts = np.append(lefts, np.int32(a['O']))
            left_co = np.append(left_co, np.int32(a['coefficent']))
    
    for a in d[1]:
        if 'O' in a.keys():
            rights = np.append(rights, np.int32(a['O']))
            right_co = np.append(right_co, np.int32(a['coefficent']))

    # Algortithm to balance element
    if np.dot(rights, right_co) == np.dot(lefts, left_co):
        print("balance")
        print(f"{lefts}{left_co}\n{right}, {right_co}")
        return

    low = (100000, 10000)
    start = target = 0

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
    
    # put formula back
    l_c = [each for each in left_co] # using python list to do FIFO
    r_c = [each for each in right_co]

    for a in d[0]:# left hand side
        if 'O' in a.keys():
            a['coefficent'] = l_c.pop(0)
    
    for a in d[1]:# right hand side
        if 'O' in a.keys():
            a['coefficent'] = r_c.pop(0)
    
    print(d)
            
# find a way to read dicts into np.array and back
# read from dict

# print(d)

main()

# right_co[0] = 11

# l_c = [each for each in left_co]
# r_c = [each for each in right_co]
# 
# # write to dict use FIFO
# 
# 
# print(d)

# 
#     print(lefts)
#     print(left_co)
# 
#     print(rights)
#     print(right_co)
