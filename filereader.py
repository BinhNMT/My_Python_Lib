class FileReader:
# Variables:
    # Hided data
    __fileName = 0      # Store the file's name
    __endOfFile = 0     # Total lines od the file
    # Public data
    content = []        # Store the content of the file, each index = 1 line of the file

# Hided Methods:
    # Constructor
    def __init__(self, inputFileName):
        #
        self.fileName = inputFileName
        #
        # Get File's lines number
        f = open(self.fileName, "r")
        lines = len(f.readlines())
        self.__endOfFile = lines
        #
        # Close file
        f.close()

# Interface:
    # Read all of file line by line
    def readFile(self):
        #
        # Open file
        fileObj = open(self.fileName, "r")
        #
        # Read line by line of the file
        for count in range(self.__endOfFile):
            self.content.append(fileObj.readline())
        #
        # Close file
        fileObj.close()