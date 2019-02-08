import os

def selectImages():
    #Manually enter the "IDs" of each image you want to keep into this list
    listOfFilesToKeep = ["1", "3", "5"]

    #This portion cleans up the input for later by appending .jpg to the
    #filenames ie "1" becomes "1.jpg"
    listOfFileNames = []

    for filename in listOfFilesToKeep:
        filename = filename + '.jpg'
        listOfFileNames.append(filename)

    #Enter the filepath to where your images are located
    startPath = 'C:/Code/Projects/image select and wipe/testfolder'

    #Enter the filepath that you want the selected images to be moved to
    #You don't have to create this folder yourself. The code will do it later.
    targetPath = 'C:/Code/Projects/image select and wipe/targetfolder'

    #If you copy and paste a path, you must manually replace all backslashes "\"
    #with forwardslashes "/"

    #This portion makes it so you don't have to manually create a new folder for
    #the moved images. It does it for you!
    if not os.path.exists(targetPath):
        os.makedirs(targetPath)

    #Look through the files in your starting folder for the files you indicated
    #earlier, and then plop them in your target folder
    for filename in os.listdir(startPath):
        if filename in listOfFileNames:
            currentLoc = os.path.join(startPath, filename)
            targetLoc = os.path.join(targetPath, filename)
            os.rename(currentLoc, targetLoc)
            print(filename)

def main():
    selectImages()

if __name__ == '__main__':
    main()
