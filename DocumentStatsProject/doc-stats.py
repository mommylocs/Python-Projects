
def getTextFile():
    fileName = input("Enter the text file name: ")
    textFile = open( fileName, 'r' )
    return fileName, textFile

def outputCountResults( fileName, lineCount, wordCount, charCount, nonartCount ):
    print()
    print( "******* {} *******".format( fileName ))
    print( "Line Count: {}".format( lineCount ))
    print( "Word Count: {}".format( wordCount ))
    print( "Char Count: {}".format( charCount ))
    print( "NonArticle Count: {}".format( nonartCount ))

def countCharacters(line):
    charCount = 0
    for c in line:
        if not c.isspace():
            charCount = charCount + 1
    return charCount
    
def countWords( line ):
    words = line.split()
    return len( words )

def nonarticles(line):
    nonartCount =0
    nonartword = line.split()
    for i in nonartword:
        if (nonartword == "and"):
            nonartCount = nonartword + nonartCount +1
    return nonartCount

def countDocStats( docFile ):
    lineCount = 0
    totalCharacters = 0
    totalWords = 0
    nonartCount = 0
    for line in docFile:
        lineCount = lineCount + 1
        totalCharacters = totalCharacters + countCharacters( line )
        totalWords = totalWords + countWords( line )
        nonartCount
    return lineCount, totalCharacters, totalWords, nonartCount

def main():
    fileName, textFile = getTextFile()
    lineCount, totalCharacters, totalWords, nonartCount = countDocStats( textFile )
    outputCountResults( fileName, lineCount, totalWords, totalCharacters,nonartCount )
    
main()


