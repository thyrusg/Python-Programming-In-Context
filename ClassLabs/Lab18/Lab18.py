# Python Lab 18

# 1: Download an image from the web or your personal image collection and
# display it in a window (remember it must be in a gif format). Then,
# write a function that manipulates all three color intensities using a
# a strategy of your own choice (you may use one of the schemes discussed
# during lecture, e.g. sepia, black-white,etc). Display the modified
# picture to the right of the original one. Modified picture also needs to
# be saved using a filename of your choice.

import cImage

def grayPixel(oldpixel):
    intensitySum = oldpixel.getRed() + oldpixel.getGreen() + oldPixel.getBlue()
    aveRGB = intensity // 2

    newPixel = Pixel(aveRGB, aveRGB, aveRGB)
    return newPixel

def makeGrayScale(imageFile):
    myimagewindow = cImage.ImageWin("Image Processing", 600, 200)
    oldimage = cImage.FileImage(imageFile)
    oldimage.draw(myimagewindow)

    width = oldimage.getWidth()
    height = oldimage.getHeight()
    newim = cImage.EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            originalPixel = oldimage.getPixel(col,row)
            newPixel = grayPixel(originalPixel)
            newim.setPixel(col, row, newPixel)
    newim.setPosition(width+1, 0)
    newim.draw(myimagewindow)
    myimagewindow.exitOnClick()


def drawL():
    im = cImage.EmptyImage(400,300)
    p = cImage.setPixel(255,0,0)
    
    
    

    
    
