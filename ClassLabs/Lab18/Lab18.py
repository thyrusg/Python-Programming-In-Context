# Python Lab 18
#
# 1: Download an image from the web or your personal image collection and
# display it in a window (remember it must be in a gif format). Then,
# write a function that manipulates all three color intensities using a
# a strategy of your own choice (you may use one of the schemes discussed
# during lecture, e.g. sepia, black-white,etc). Display the modified
# picture to the right of the original one. Modified picture also needs to
# be saved using a filename of your choice.

import cImage


def grayPixel(oldpixel):
    intensitySum = oldpixel.getRed() + oldpixel.getGreen() + oldpixel.getBlue()
    aveRGB = intensitySum // 2

    newPixel = cImage.Pixel(aveRGB, aveRGB, aveRGB)
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
            originalPixel = oldimage.getPixel(col, row)
            newPixel = grayPixel(originalPixel)
            newim.setPixel(col, row, newPixel)
    newim.setPosition(width + 1, 0)
    newim.draw(myimagewindow)
    myimagewindow.exitOnClick()


# 2: Use any picture that you wish, display it in a window and then draw a large
# letter L (uppercase) over it, that would cover most of the canvas. Make sure
# the L is thick enough to be seen.

from cImage import *
def bigL(image):
myWin = ImageWin('L',500,500)
file = FileImage('buildings.gif')
redPixel = Pixel(255,0,0)
x,y = 0,0
im = EmptyImage(file.getWidth,file.getHeight())

for a in range(file.getWidth()):
    im.setPixel(x,a,redpixel)

for b in range(file.getHeight()):
    im.setPixel(b,a,redpixel)

im.draw(myWin)

# 3: Download the image file buildings.gif. First, display the original
# picture in a window. Then, create a new image by rotating the original
# image by 90 degrees clockwise. Display this new image on the right
# side of the original one.


from cImage import *

def rotate(image):
    picture = FileImage(image)
    myWin = ImageWin('Picture', 1000, 800)
    oldw = picture.getWidth()
    oldh = picture.getHeight()
    picture.draw(myWin)

    newim = EmptyImage(oldw,oldw)
    for row in range(oldh):
        for col in range(oldw):
            oldpixel = picture.getPixel(col, row)
            newim.setPixel(oldw-row, col, oldpixel)

    newim.setPosition(oldh+1,0)
    newim.draw(myWin)
