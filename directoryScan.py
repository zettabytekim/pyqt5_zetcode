import os
import sys

def search(dir):
    try:
        files = os.listdir(dir)
        for file in files:
            fullFilename = os.path.join(dir, file)
            if os.path.isdir(fullFilename):
                search(fullFilename)
            else:
                print(fullFilename)
    except PermissionError:
        pass


# searchDir = sys.argv[1]
search('/')