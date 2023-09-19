import numpy as np
from sympy import Matrix
# brute force list of alphabet chars
alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
        "t", "u", "v", "w", "x", "y", "z"]

"""
function makes a key matrix using the string from the key param. The size of the matrix is determined by the size param
So a size of 3 will make a 3x3 matrix
quick matrix explanation alphabet -> a=0 through z=25
example matrix: key = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
"""
def makeKeyMatrix(key, size):
    matrix = np.array([], int)

    for letter in key:
        index = alph.index(letter)
        matrix = np.append(matrix, index)

    matrix = np.reshape(matrix, (size,size))
    print(matrix)
    return matrix

def encrypt(message, matrixSize, key):
    """
    function encrypts the message string using hill cipher with the key param
    """
    # initialized junk
    numList = []
    codeList = []
    codedMesssage = ""
    
    # makes the matrix from the given key
    keyMatrix = makeKeyMatrix(key, matrixSize)

    # adds the necessary x's to the end of the list to make sure the length of the numList is divisible by the matrix size
    if len(message) % matrixSize != 0:
        amountToAdd = matrixSize - (len(message) % matrixSize)
        allX = amountToAdd * alph[23]
        message += allX

    # converts each character to a number that we can perform math on
    for cha in message:
            num = alph.index(cha)
            numList.append(num)
    
    # breaks down numList into groups of the matrix size so that it can be multiplied with the key
    for index in range(0, len(numList), matrixSize):
        chars = numList[index:index + matrixSize]
        codeList = keyMatrix.dot(chars) % 26

        # converting numerical values back into a string of alphabetical values
        for index in codeList:
            codedMesssage += alph[index]

    #return final result
    return codedMesssage



def decrypt(encodedMessage, matrixSize, key):
    """
    function decrypts the encoded string using hill cipher (modular inverse)
    :param encodedMessage:
    :return: decodedChars
    """
    # initialized bs
    numList = []
    decodedList = []
    decodedMessage = ""

    # roundabout way find modular inverse of keyMatrix using sympy, then converting back to a numpy array
    newMatrix = Matrix(makeKeyMatrix(key, matrixSize))
    print(newMatrix)
    invsymmatrix = newMatrix.inv_mod(26)
    inverseModMatrix = np.array(invsymmatrix)

    # converts alphabetic list of chars into numeric values
    for char in encodedMessage:
        num = alph.index(char)
        numList.append(num)

    # breaks down numList into groups of the matrix size so that it can be multiplied with the reverse key
    for index in range(0, len(numList), matrixSize):
        chars = numList[index:index + matrixSize]
        decodedList = inverseModMatrix.dot(chars) % 26

        # converting numerical values back into a list of alphabetical values
        for index in decodedList:
            decodedMessage += alph[index]
    
    #return result
    return decodedMessage



def Menu():
    exit = False
    while(not(exit)):
        selection = input("Enter selection: ")
        #Success is the ability to go from one failure to another with no loss of enthusiasm
        if selection == "1":
            message = input("\nEnter your message: ").lower().replace(" ", "")
            matrixSize = int(input("Enter the size of the key matrix: "))
            key = input("Enter your key: ").lower().replace(" ", "")
            key3by3 = "monarchyz"
            key4by4 = "cdbfbechdvgiacdb"
            key5by5 = "bcdefcdefbdefbcefbcdfbcde"
            codedMessage = encrypt(message, matrixSize, key)
            print("\nYour encrypted message: {}".format(codedMessage) )

        elif selection == "2":
            message = input("\nEnter your message: ").lower().replace(" ", "")
            matrixSize = int(input("Enter the size of the key matrix: "))
            key = input("Enter your key: ").lower().replace(" ", "")
            key3by3 = "monarchyz"
            key4by4 = "cdbfbechdvgiacdb"
            key5by5 = "bcdefcdefbdefbcefbcdfbcde"
            decodedMessage = decrypt(message, matrixSize, key)
            print("\nYour decrypted message: {}".format(decodedMessage))

        elif selection == "3":
            print("\nExiting program.")
            exit = True

        else:
            print("Unknown option.\nTo encrypt a message, enter 1.\tTo decrypt a message, enter 2\tTo exit the program, enter 3\n")

if __name__ == '__main__':
    Menu()

"""
current issues:
* no validation for size of the matrixes from input. Both for the matrix size and for the actual key inputted
* sometimes it throws an exception generating the inverse of the key matrix for decryption, not sure what causes it
*
*
"""