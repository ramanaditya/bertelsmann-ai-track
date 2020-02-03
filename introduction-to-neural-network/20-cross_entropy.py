"""
Quiz: Coding Cross-entropy
Now, time to shine! Let's code the formula for cross-entropy in Python. As in the video, Y in the quiz is for the category, and P is the probability.
"""
import numpy as np

def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))