import numpy as np
import copy as cp

def main():
    lefts = np.array([2])
    left_coefficents = np.array([15])
    
    rights = np.array([2, 1])
    right_coefficents = np.array([6, 8])

    if np.dot(rights, right_coefficents) == np.dot(lefts, left_coefficents):
        print("balance")
        print(f"{lefts}{left_coefficents}\n{rights}, {right_coefficents}")
        return

    low = (100000, 10000)

    for i in range(len(right_coefficents)):
        right_coefficents_cp = cp.copy(right_coefficents)
        while np.dot(lefts, left_coefficents) > np.dot(rights, right_coefficents_cp):
            right_coefficents_cp[i] += 1

        new_low = (np.dot(rights, right_coefficents_cp) - np.dot(lefts, left_coefficents), (right_coefficents_cp[i] - right_coefficents[i]))
        low = min(low, new_low)

        print(f"the least big is if {right_coefficents[i]} goes to -> {right_coefficents_cp[i]}, the diff would be {low}")
            
main()
