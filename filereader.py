class FileReader:
# Variables:
    # Hided data
    __fileName = 0      # Store the file's name
    __endOfFile = 0     # Total lines od the file

# Hided Methods:
    # Constructor
    def __init__(self, inputFileName):
        #
        self.__fileName = inputFileName
        #
        # Get File's lines number
        f = open(self.__fileName, "r")
        lines = len(f.readlines())
        self.__endOfFile = lines
        #
        # Close file
        f.close()

# Interface:
    # Read all of file line by line
    def readLines(self):
        #
        contentAsList = []        # Store the content of the file, each index = 1 line of the file.
        # 
        # Open file
        fileObj = open(self.__fileName, "r")
        #
        # Read line by line of the file
        for count in range(self.__endOfFile):
            contentAsList.append(fileObj.readline())
        #
        # Close file and return lines content
        fileObj.close()
        return contentAsList
    
    #
    # Read all of file like a package
    def readFile(self):
        #
        contentAsString = ""        # Store the content of the file in a string package.
        # 
        # Open file
        fileObj = open(self.__fileName, "r")
        #
        # Read the file
        contentAsString = fileObj.read()
        #
        # Close file and return lines content
        fileObj.close()
        return contentAsString
