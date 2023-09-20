import numpy as np
from sympy import Matrix
# brute force list of alphabet chars
alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
        "t", "u", "v", "w", "x", "y", "z"]

def makeKeyMatrix(key, size):
    matrix = np.array([], int)

    for letter in key:
        index = alph.index(letter)
        matrix = np.append(matrix, index)

    matrix = np.reshape(matrix, (size,size))
    return matrix

def testMatrix(key):
    newMatrix = Matrix(makeKeyMatrix(key, 5))
    print(newMatrix)
    invsymmatrix = newMatrix.inv_mod(26)
    print(invsymmatrix)
    inverseModMatrix = np.array(invsymmatrix)
    print(inverseModMatrix)

keepGoing = True
while(keepGoing):
    key = input("Enter a key to test: ")
    try:
        testMatrix(key)
        print("\"" + key + "\" works!")
        keepGoing = False
    except:
        print("\"" + key + "\" it no workie")