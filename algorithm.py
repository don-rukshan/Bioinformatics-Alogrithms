# -*- coding: utf-8 -*-
"""Algorithm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e6AARjX_HNQvpLmm3Ks7dNrsNU-Gw7M0

# CSC 464 2.0 Computational Biology - Assignment 1
## AS2016461 - T. B. S. M. Paranavithana

---

# **Configuration**
"""

import numpy as np

"""# **Part 1 -** Needleman-Wunsch algorithm"""

# method to initialize the scoring scheme
def scoring(match = 1,mismatch = -1, gap = -1):
    # dictionary to hold the penalty values
    penalty = {'MATCH': match, 'MISMATCH': mismatch, 'GAP': gap}
    return penalty

# method to return values for the cases of match or mismatch
def match_diag(char1, char2):
    if char1 == char2:
        return penalty['MATCH']
    else:
        return penalty['MISMATCH']

# method to return pointer values accoriding to the maximum value
def pointer(d, h, v, max_value):
    if max_value == d and max_value == h and max_value == v:
        return "DHV"
    elif max_value == d and max_value == h:
        return "DH"
    elif max_value == d and max_value == v:
        return "DV"
    elif max_value == h and max_value == v:
        return "HV"
    elif max_value == d:
        return "D"
    elif max_value == h:
        return "H"
    else:
        return "V"

# find best alignments recursively
def find_alignments(current, array1, array2, i, j, pointer_needle):
    ###### have to code

# method to perform the global alignment and print out one or more best alignments
def needle(seq1, seq2):
    # dimensions of the score and pointer matrices
    m = len(seq1) + 1
    n = len(seq2) + 1

    # initializing the score matrix
    score_needle = np.zeros((n,m),dtype = int)

    # initializing the pointer matrix
    pointer_needle = np.empty((n,m),dtype = 'U3')

    # fill the first row with gap penalty
    for i in range(m):
        score_needle[0][i] = penalty['GAP'] * i
        pointer_needle[0][i] = 'H'

    # fill the first column with gap penalty
    for i in range(n):
        score_needle[i][0] = penalty['GAP'] * i
        pointer_needle[i][0] = 'V'

    # change back the (0,0) element of the pointer matrix back to 0
    pointer_needle[0][0] = '0'

    # loop through all the elements in the matrix
    for i in range(1, n):
        for j in range(1, m):
            # get the diagonal, horizontal and vertical values according to the penalty
            d = score_needle[i-1][j-1] + match_diag(seq1[j-1], seq2[i-1])
            h = score_needle[i][j-1] + penalty['GAP']
            v = score_needle[i-1][j] + penalty['GAP']
            # get the maximum value among d,h, v
            max_value = max(d, h, v)
            # fill the score matrix with the maximum value
            score_needle[i][j] = max_value
            # fill the pointer matrix with the relevent pointer
            pointer_needle[i][j] = pointer(d, h, v, max_value)
    
    # arrays to hold best alignments
    array1 = []
    array2 = []
    
    # find all the best alignments
    find_alignments(0, array1, array2, n, m, pointer_needle)

    print(score_needle)
    print(pointer_needle)

# setting up the scoring scheme (default)
penalty = scoring()

# test case
needle('ATTAC', 'AATTC')

"""# **Part 2 -** Smith-Waterman algorithm"""