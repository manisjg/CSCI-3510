# This import should be all we need for the Ceasar Cipher portion.
# Pandas DataFrame is a 2-dimensional labeled data structure like any table with rows and columns
import pandas as pd

# This is a probably overly complicated way to show each character in the Project 1 subset of Unicode characters
# creates a list named chars that holds each
df = {'chars': [' ', '!', '"', '#', '$', '%', '&', "\'", '(', ')', '*', '+', ',', '-', '.', '/',
                 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?',
                 '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_',
                 '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']}
# This creates a pandas dataframe based on the list we just created
unicodeDF = pd.DataFrame(data=df)
# because the project 1 doc has only a subset of unicode chars starting at #32,
# this creates a new list of numbers 32-126 just as in the doc
code = unicodeDF.index + 32
# creates a new column, named code, based on the 32-126 values we just created
unicodeDF["code"] = code


def strEncrypt(usrStr):
    """
    function that accepts usrStr string which it then breaks apart and turns into code before shifting a
    set amount and turning the code back into the now encrypted characters
    :param usrStr:
    :return: encryptedStr
    """
    chList = []
    indList = []
    coList = []
    newchList = []
    newindList = []
    newcoList = []
    encryptedStr = ""

    for ch in usrStr:
        chList.append(ch)

    for ch in chList:
        indList.append(unicodeDF[unicodeDF['chars'] == ch].index[0])

    for i in indList:
        col = unicodeDF['code']
        coList.append(col[i])
    print(coList)
    newcoList = encrypt(coList)

    for co in newcoList:
        newindList.append(unicodeDF[unicodeDF['code'] == co].index[0])

    for i in newindList:
        col = unicodeDF['chars']
        newchList.append(col[i])

    for ch in newchList:
        encryptedStr += ch

    return encryptedStr


def strDecrypt(encryptedStr):
    """
    This function accepts the newly encrypted string and basically reverses the encryption resulting in the original
    string.
    :param encryptedStr:
    :return: decryptedStr
    """
    chList = []
    indList = []
    coList = []
    newchList = []
    newindList = []
    newcoList = []
    decryptedStr = ""

    for ch in encryptedStr:
        chList.append(ch)

    for ch in chList:
        indList.append(unicodeDF[unicodeDF['chars'] == ch].index[0])

    for i in indList:
        col = unicodeDF['code']
        coList.append(col[i])
    print(coList)
    newcoList = decrypt(coList)

    for co in newcoList:
        newindList.append(unicodeDF[unicodeDF['code'] == co].index[0])

    for i in newindList:
        col = unicodeDF['chars']
        newchList.append(col[i])

    for ch in newchList:
        decryptedStr += ch

    return decryptedStr


def encrypt(coList):
    """
    this function simply adds 5 to each number of the coded version of the string resulting in a 5 char ceasar shift
    :param coList:
    :return: coList
    """
    coList = [co + 5 for co in coList]
    return coList


def decrypt(coList):
    """
    this function simply subtracts 5 to each number of the coded version of the string resulting in a 5 char ceasar shift
    :param coList:
    :return: coList
    """
    coList = [co - 5 for co in coList]
    return coList


if __name__ == '__main__':
    usrStr = input("What String would you like to encrypt?\n")
    print("Encrypted string:")
    eString = strEncrypt(usrStr)
    print(eString)
    print("Decrypted string:")
    print(strDecrypt(eString))

"""
current issues:
* no user input for what amount of ceasar shift to use
* not every character works - if the numbers in the code would go above 126, it does not loop back to 32 correctly,
I assume that ceasar shifting in the negative direction would have a similar problem if it were to go below 32
*
*
*
*
"""

