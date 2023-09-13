import numpy as np
import string

# makes a matrix with the given key
# uses the size parameter to determine the size of the matrix, if you give it 3, it'll make a 3 x 3 matrix with the key
def makeMatrix(key, size):
    matrix = np.array([], int)

    for letter in key:
        index = string.ascii_lowercase.find(letter)
        matrix = np.append(matrix, index)
    
    matrix = np.reshape(matrix, (size,size))
    print(matrix)
    return matrix

def Encrypt():
    print("Start encryption")

    plaintext = input("Enter your message: ").lower()
    key = input("Enter your key: ").lower()
    size = int(input("Enter the size of your matrix: "))
    if(size != len(key)):
        print("Your key doesn't match the matrix size. Exitting now.")
        return
    matrix = makeMatrix(key, size)

    for index in range(0, len(plaintext), size):
        if(index + size > len(plaintext)):
            extra = ""
            for rep in range(size - (len(plaintext) - index)):
                extra += "x"
            set = plaintext[index:index + (len(plaintext) - index)] + extra
        else:
            set = plaintext[index:index + size]
        print(set)
        #TODO perform calculation on the set of letters with the matrix
    
def Decrypt():
    print("start decryption")
    #TODO this function
    
def Menu():
    exit = False
    while(not(exit)):
        selection = input("Enter selection: ")
        if selection == "1":
            Encrypt()
        elif selection == "2":
            Decrypt()
        elif selection == "3":
            print("\nExiting program.")
            exit = True
        else:
            print("Unknown option.\nTo encrypt a message, enter 1.\tTo decrypt a message, enter 2\tTo exit the program, enter 3\n")



#Driver
print("Welcome to the Hill Cipher Program.\nTo encrypt a message, enter 1.\tTo decrypt a message, enter 2\tTo exit the program, enter 3\n")
Menu()