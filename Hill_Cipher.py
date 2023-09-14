import numpy as np
from sympy import Matrix
# brute force list of alphabet chars
alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
        "t", "u", "v", "w", "x", "y", "z"]
"""
quick matrix explanation alphabet -> a=0 through z=25
hardcoded 3x3 matrix. key = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
"""
# hard coded key matrix
keyMatrix = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
# roundabout way find modular inverse of keyMatrix using sympy, then converting back to a numpy array
newMatrix = Matrix(keyMatrix)
invsymmatrix = newMatrix.inv_mod(26)
inverseModMatrix = np.array(invsymmatrix)

# hard coded user string
usrStr = "Success is the ability to go from one failure to another with no loss of enthusiasm"
# removes spaces
usrStr = usrStr.replace(" ", "")
# initialized lists
chList = []
numList = []
# makes list of chars in usrStr while making sure all chars are lower case
for ch in usrStr.lower():
    chList.append(ch)


def encrypt(chList):
    """
    function encrypts the character list using a 3x3 hill cipher
    :param chList:
    :return: codedChars
    """
    # converts each character to a number that we can perform math on
    for cha in chList:
        num = alph.index(cha)
        numList.append(num)
    # adds the necessary x's to the end of the list to make sure the length of the numList is divisible by 3
    if len(numList) % 3 == 2:
        numList.append(23)
    if len(numList) % 3 == 1:
        numList.append(23)
        numList.append(23)
    # initialized junk
    one = 0
    two = 0
    three = 0
    counter = 1
    codeList = []
    holdList = []
    # breaks down numList into groups of 3 so that it can be multiplied with the 3x3 key
    while len(numList) > 0:
        if counter == 1:
            one = numList.pop(0)
            counter = 2
        elif counter == 2:
            two = numList.pop(0)
            counter = 3
        elif counter == 3:
            three = numList.pop(0)
            # once one, two, and three are correct from numList, add to a new 3x1 array (1x3 array? idk, who cares)
            threeChars = np.array([[one], [two], [three]])
            # matrix multiplication of 3x3 key and 3x1 group of numerical chars
            codedGroup = keyMatrix.dot(threeChars)
            # add each element of new 3x1 matrix to temporary list
            holdList.append(codedGroup[0, 0])
            holdList.append(codedGroup[1, 0])
            holdList.append(codedGroup[2, 0])
            counter = 1
        else:
            print("something went wrong")
    # mods each number in temp list by 26 to finish modular matrix multiplication and adds results to codeList
    while len(holdList) > 0:
        codeList.append(holdList.pop(0) % 26)
    # converting numerical values back into a list of alphabetical values
    codedChars = []
    for index in codeList:
        char = alph[index]
        codedChars.append(char)

    return codedChars


def decrypt(encodedChars):
    """
    function decrypts the character list of encoded characters using a 3x3 hill cipher (modular inverse)
    :param encodedChars:
    :return: decodedChars
    """
    # converts alphabetic list of chars into numeric values
    for c in encodedChars:
        num = alph.index(c)
        numList.append(num)
    # initialized bs
    one = 0
    two = 0
    three = 0
    counter = 1
    codeList = []
    holdList = []
    # breaks down numList into groups of 3 so that it can be multiplied with the 3x3 reverse key
    while len(numList) > 0:
        if counter == 1:
            one = numList.pop(0)
            counter = 2
        elif counter == 2:
            two = numList.pop(0)
            counter = 3
        elif counter == 3:
            three = numList.pop(0)
            # once one, two, and three are correct from numList, add to a new 3x1 array (1x3 array? idk, who cares)
            threeChars = np.array([[one], [two], [three]])
            # matrix multiplication of 3x3 reverse key and 3x1 group of numerical chars
            decodedGroup = inverseModMatrix.dot(threeChars)
            # add each element of new 3x1 matrix to temporary list
            holdList.append(decodedGroup[0, 0])
            holdList.append(decodedGroup[1, 0])
            holdList.append(decodedGroup[2, 0])
            counter = 1
        else:
            print("something went wrong")
    # mods each number in temp list by 26 to finish modular matrix multiplication and adds results to codeList
    while len(holdList) > 0:
        codeList.append(holdList.pop(0) % 26)
    # converting numerical values back into a list of alphabetical values
    decodedChars = []
    for index in codeList:
        char = alph[index]
        decodedChars.append(char)

    return decodedChars


if __name__ == '__main__':
    print("Key Matrix:")
    print(keyMatrix)
    print("Reverse Key Matrix:")
    print(inverseModMatrix)
    encryptedChars = encrypt(chList)
    print("Encrypted Characters:")
    print(encryptedChars)
    decryptedChars = decrypt(encryptedChars)
    print("Decrypted Characters:")
    print(decryptedChars)
"""
current issues:
* no user input, everything is hard coded
* 4x4 matrix and 5x5 matrix ciphers still need to be coded
*
*
*
*
"""