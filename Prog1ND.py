#Skip leading whitespace function; Returns first non-blank character in the line.
def skipBlanks(inputLine):
    for itr in range(len(inputLine)):
        if inputLine[itr] != ' ':
            return itr
    return -1

#Skip whitespace between words in a line.
def skipBlanks2(inputLine, intStart):
    for itr in range(intStart, len(inputLine)):
        if inputLine[itr] != ' ':
            return itr
    return -1

#Skip to next whitespace in a line.
def skipToBlank(inputLine, intStartIndex):
    for itr in range(intStartIndex, len(inputLine)):
        if inputLine[itr] == ' ':
            return itr
    return -1

#Username/Password Encoding function.
def encodeWord(encodingWordValue):
    encodedWord = ' '
    for itr in range(0,len(encodingWordValue)):
        singleCharacter = encodingWordValue[itr]
        asciiValue = ord(singleCharacter)
        if(asciiValue>32 and asciiValue<95):
            asciiValue = asciiValue + 10
        else:
            asciiValue = asciiValue - 10
            encodedWord = encodedWord + chr(asciiValue)
    return encodedWord

#Trim a line in the file. Iterates until eof in main.
def trimLine(inputLine):
    indexStart = skipBlanks(inputLine)
    indexEnd = skipToBlank(inputLine, indexStart)
    accountName = inputLine[indexStart:indexEnd].strip()

    indexStart = skipBlanks2(inputLine, indexStart)
    userName = inputLine[indexStart:indexEnd].strip()

    indexStart = skipBlanks2(inputLine, indexEnd)
    passwordHint = inputLine[indexStart:].strip()

    return accountName + '\t' + encodeWord(userName) + '\t' + encodeWord(passwordHint)



#Main.
def main():
    # Asking for input file name. 
    inputFileName = input("Enter the name of the file:")
    inputFileName = open('accounts.txt', 'r')
    outputFile = open('prog1outND.txt', 'w')

    # Skip Header
    inputFileName.readline()
    for line in  inputFileName:
        outputFile.write(trimLine(line) + '\n')

    inputFileName.close()
    outputFile.close()

if __name__ == '__main__':
    main()