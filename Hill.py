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
    return matrix

def Encrypt():
    print("Start encryption")

    plaintext = input("Enter your message: ").lower() #TODO remove spaces
    key = input("Enter your key: ").lower()
    size = int(input("Enter the size of your matrix: ")) #if you enter 2, it'll create a 2 x 2 matrix, and is used below for determining the sets of letters for the calculation below
    ciphertext = ""
    matrix = makeMatrix(key, size)

    for index in range(0, len(plaintext), size):
        if(index + size > len(plaintext)): #so if the next iteration will end after this, we need to add x at the end of the string to pad it
            extra = ""
            for rep in range(size - (len(plaintext) - index)): #loops based off the size inputted, subtraced by the result of the plaintext length minus the index
                extra += "x"
            set = plaintext[index:index + (len(plaintext) - index)] + extra
        else: #if it is fine, then take the next amount of letters from the plaintext that is the size inputted by the user earlier
            set = plaintext[index:index + size]
        
        setNum = np.array([], int) 
        for letter in set:
            setNum = np.append(setNum, string.ascii_lowercase.find(letter))
        
        result = np.dot(setNum, matrix) % 26
        for index in result:
            ciphertext += string.ascii_lowercase[index]
        
    print(ciphertext)
    
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
print("Hill Cipher Program.\nTo encrypt a message, enter 1.\tTo decrypt a message, enter 2\tTo exit the program, enter 3\n")
Menu()