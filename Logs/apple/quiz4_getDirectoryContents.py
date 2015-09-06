import os

def getChildItems(targetPath=""):
    
    if not os.path.isdir(targetPath):
        raise "Invalid path provided..."
    
    for item in os.listdir(targetPath):
        if os.path.isdir(os.path.join(targetPath, item)):
            print "Directory: " + item
            getChildItems(os.path.join(targetPath, item))
        else:
            print "File: " + item 
      

if __name__ == "__main__":

	getChildItems("/etc")      
