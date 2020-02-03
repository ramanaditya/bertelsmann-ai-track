import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    denominator = 0
    for i in L:
        denominator += np.exp(i)
    result = []
    for i in L:
        result.append(np.exp(i)/denominator)
    return result

"""
Trying for L=[5,6,7].
The correct answer is
[0.09003057317038046, 0.24472847105479764, 0.6652409557748219]
And your code returned
[0.09003057317038046, 0.24472847105479764, 0.6652409557748219]

Correct!

"""
