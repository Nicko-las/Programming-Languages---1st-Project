# Nickolas Downey
# Programming Project 1 - Programming Languages



#---------------
# Function Name: skipBlanks
# Programmer: Nickolas Downey
# Date Created: 2/7/2023
# Last Modified: 2/9/2023
#
# Agruments: inputLine - String; A line of input from the given file in main. 
# Example Usage: skipBlanks(inputLine)
# This function skips the leading whitespace and returns the first non-blank character. It begins at position 0.
#---------------
def skipBlanks(inputLine):
    itr = 0
    for itr in range(len(inputLine)):
        if not inputLine[itr].isspace():
            break
    return itr

#---------------
# Function Name: skipBlanks2
# Programmer: Nickolas Downey
# Date Created: 2/7/2023
# Last Modified: 2/9/2023
#
# Agruments: inputLine - String; A line of input from the given file in main. 
#            intStart - int; A position in the line to start. 
# Example Usage: skipBlanks2(inputLine, intStart)
# This function skips the leading whitespace and returns the first non-blank character it finds. It begins at position intStart specified by the user.
# The beginning if block checks for error. It is so the start value does not overrun the length of the word. 
#---------------
def skipBlanks2(inputLine, intStart):
    if intStart >= len(inputLine):
        return -1
    itr = intStart
    for itr in range(intStart, len(inputLine)):
        if not inputLine[itr].isspace():
            break
    return itr


#---------------
# Function Name: skipToBlank
# Programmer: Nickolas Downey
# Date Created: 2/7/2023
# Last Modified: 2/9/2023
#
# Agruments: inputLine - String; A line of input from the given file in main. 
#            intStartIndex - int; An index in the line to start. 
# Example Usage: skipToBlank(inputLine, intStartIndex)
# This function starts at the index in the line specified by the user. It then scans until it finds a blank character and returns the position of that character.
#---------------
def skipToBlank(inputLine, intStartIndex):
    itr = intStartIndex
    for itr in range(intStartIndex, len(inputLine)):
        if inputLine[itr].isspace():
            break
    return itr


#---------------
# Function Name: encodeWord
# Programmer: Nickolas Downey
# Date Created: 2/7/2023
# Last Modified: 2/9/2023
#
# Agruments: encodingWordValue - String; A word to be encoded.
# Example Usage: encodeWord(encodingWordValue)
# This function encodes a string character by character. If the ASCII value is between 35 & 95 the it is shifted up by 10 positions. Otherwise the value is decremented by 10 positions.
# It returns a word in the form of a string that is encoded with ASCII shifting.
#---------------
def encodeWord(encodingWordValue):
    encodedWord = ''
    for itr in encodingWordValue:
        asciiValue = ord(itr)
        if(32 <= asciiValue <= 95):
            asciiValue = asciiValue + 10
        else:
            asciiValue = asciiValue - 10
        encodedWord = encodedWord + chr(asciiValue)
    return encodedWord

#---------------
# Function Name: trimLine
# Programmer: Nickolas Downey
# Date Created: 2/7/2023
# Last Modified: 2/9/2023
#
# Agruments: inputLine - String; A line of input from the given file in main. 
# Example Usage: trimLine(inputLine)
# This function takes in a line of input from a file called in main. It the uses the previous functions to trim a single line of whitespace and encode the username and password. 
#---------------
#Trim a line in the file. Iterates until eof in main.
def trimLine(inputLine):
    indexStart = skipBlanks(inputLine)
    indexEnd = skipToBlank(inputLine, indexStart)
    accountName = inputLine[indexStart:indexEnd].strip()

    indexStart = skipBlanks2(inputLine, indexEnd)
    indexEnd = skipToBlank(inputLine,indexStart)
    userName = inputLine[indexStart:indexEnd].strip()

    indexStart = skipBlanks2(inputLine, indexEnd)
    passwordHint = inputLine[indexStart:].strip()

    userName = encodeWord(userName)
    passwordHint = encodeWord(passwordHint)

    return accountName + '\t\t' + userName + '\t\t' + passwordHint


#---------------
# Function Name: Main
# Programmer: Nickolas Downey
# Date Created: 2/7/2023
# Last Modified: 2/9/2023
#
# Main asks for a name of an input file and opens it. Then it opens an output file. 
# It then outputs the trimmed and encoded words to the output file. It ends by closing both files. 
# The final two lines are for running main when the run button is pressed in Visual Studio Code. 
#---------------
def main():
    # Asking for input file name. 
    inputFileName = input("Enter the name of the file:")
    inputFileName = open(inputFileName, 'r')
    outputFile = open('prog1outND.txt', 'w')

    # Skip Header
    inputFileName.readline()
    for line in  inputFileName:
        outputFile.write(trimLine(line) + '\n')

    inputFileName.close()
    outputFile.close()

if __name__ == '__main__':
    main()