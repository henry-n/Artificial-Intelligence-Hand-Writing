import scipy.io
import numpy

# Structure of image files
# [offset] [type]          [value]          [description] 
# 0000     32 bit integer  0x00000803(2051) magic number 
# 0004     32 bit integer  60000            number of images 
# 0008     32 bit integer  28               number of rows 
# 0012     32 bit integer  28               number of columns 
# 0016     unsigned byte   ??               pixel 
# 0017     unsigned byte   ??               pixel 
# ........ 
# xxxx     unsigned byte   ??               pixel
# Pixels are organized row-wise. Pixel values are 0 to 255. 0 means background (white), 255 means foreground (black).
def image():
    data = open("Datasets\emnist-letters-train-images-idx3-ubyte", "rb")
    magicNum = data.read(4)
    itemsNum = int.from_bytes(data.read(4), "big")
    imageSize = int.from_bytes(data.read(4), byteorder='big'), int.from_bytes(data.read(4), byteorder='big')

    # I don't know wtf I was thinking when I wrote this
    #images = []
    #for image in range(int(itemsNum / 4)): # Iterate every pixel
    #    imageMatrix = numpy.zeros((imageSize[0], imageSize[1])) # Create a matrix to hold all the pixels of a single image
    #    for j in range(imageSize[1]): # Iterate through every spot in the matrix and save each pixel in the right spot
    #        for i in range(imageSize[0]):
    #            imageMatrix[i][j] = int.from_bytes(data.read(1), byteorder='big') # Add the matrix to the list containing the images

    #    images.append(imageMatrix)

    images = []
    file = open("images.txt", "w") # Image matrices will be printed to this file
    imageMatrix = numpy.zeros((imageSize[0], imageSize[1]), dtype = int) # Create a matrix to hold all the pixels of a single image
    imageMatrix = imageMatrix.flatten()
    for index in range(int(itemsNum / 4)): # Iterate every pixel
        imageMatrix[index % (imageSize[0] * imageSize[1])] = int.from_bytes(data.read(1), byteorder='big') # Read each pixel, byte by byte

        if ((index + 1) % (imageSize[0] * imageSize[1]) == 0): # Check if all pixels in one image have been processed
            imageMatrix = imageMatrix.reshape((imageSize[0], imageSize[1])) # Reshape the matrix
            images.append(imageMatrix) # Add the matrix to the list

            for i in range(imageSize[0]): # Print the matrix to the file
                s = ''
                for j in range(imageSize[1]):
                    s+=('{:03d}' + ' ').format(int(imageMatrix[i][j]))
                s += "\n"
                file.write(s);
            file.write("\n\n")

            imageMatrix = numpy.zeros((imageSize[0], imageSize[1])) # Create a new matrix
            imageMatrix = imageMatrix.flatten()
    

# Structure of label files
# [offset] [type]          [value]          [description] 
# 0000     32 bit integer  0x00000801(2049) magic number (MSB first) 
# 0004     32 bit integer  60000            number of items 
# 0008     unsigned byte   ??               label 
# 0009     unsigned byte   ??               label 
# ........ 
# xxxx     unsigned byte   ??               label
# The labels values are 1 to 26 (it seems like)
def label():
    data = open("Datasets\emnist-letters-train-labels-idx1-ubyte", "rb")
    magicNum = data.read(4)
    itemsNum = int.from_bytes(data.read(4), "big")

    labels = []
    for label in range(itemsNum):
        char = chr(int.from_bytes(data.read(1), byteorder='big') + 64) # Idk if I'm interpreting this right
        labels.append(char)

image()