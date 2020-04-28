import os

path = "D:/r6/"

def cleaner(word):
    word = word[0].upper() + word[1:].lower()
    return word

def contents(path, keyword):
    for filename in os.listdir(path):
        cPath = path + filename
        if os.path.isdir(cPath):
            contents(cPath+'/', keyword)
        else:
            if keyword in cPath:
                os.startfile(cPath)

def main():
    global path
    print("Please select your map: ")
    mapS = cleaner(input()) + "/"
    print("Please select on of the sites: ")
    site = cleaner(input())
    path += mapS
    contents(path, site)

main()
    
