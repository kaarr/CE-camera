from PIL import Image
import os

# Open a file
path = "timing/"
dirs = os.listdir( path )
imgSize = (1280,800)
# imgSize = (640,400)

# This would print all the files and directories
for file in dirs:
    if not file.startswith("."):
        print(file)
        rawData = open(path + file, 'rb').read()
        img = Image.frombytes('L', imgSize, rawData)
        img.save(file + ".png")# can give any format you like .png
