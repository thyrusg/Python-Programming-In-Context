# 1: Write a function called DrawLine that takes parameter img and draws two vertical lines to img, one red line from (50,0) to (50,300) and one made up of randomly
# colored pixels from (150,50) to (150,250)

import cImage
def DrawLine(img):
    #win = cImage.ImageWin('test',300,300)
    im = cImage.EmptyImage(300,300)
    p = cImage.Pixel(255,0,0)
    for i in range(300):
        im.setPixel(50,i,p)
    im.draw(img)
    
    p2 = cImage.Pixel(234,154,125)
    for l in range(250):
        im.setPixel(150,l,p2)
    im.draw(img)

# 2: Re-write the function you created in excercise 1 in the following manner. DrawLines draws only one line of randomly colored pixels and it takes the following 
# parameters: img, x1,y1,x2,y2, where x1 and y1 are coordinates for the beginning of the line and x2, y2 are coordinates for the end of the line.

import cImage
import random
import math
def DrawLines(img,x1,y1,x2,y2):
    #win = cImage.ImageWin('test',500, 500)
    im = cImage.EmptyImage(300,300)
    r,g,b = 255,0,0 #random.randint(0,255),random.randint(0,255),random.randint(0,255)
    p = cImage.Pixel(r,g,b)
    slope = (y2-y1) // (x2-x1)
    #im.setPixel(x1,y1,p)
    for i in range(math.abs(y2-y1)):
        im.setPixel(x1,y1,p)
        x1 += slope
        y1 += slope
    im.draw(img)

# 3: Download an image from the Web or your personal collection and display it in a window(remember it must be in gif format and it should
# be small). Then, remove all green from the picture, save it, and display it in the same window below the original image.


def noGreen(oldpixel):
    oldgreen = oldpixel.getGreen()
    newgreen = cImage.Pixel(oldpixel.getRed(),0,oldpixel.getBlue())
    return newgreen

def removeGreen(image):
    myimagewindow = cImage.ImageWin("Image Processing",600,200)
    oldimage = cImage.FileImage(image)
    oldimage.draw(myimagewindow)

    width = oldimage.getWidth()
    height = oldimage.getHeight()
    newim = cImage.EmptyImage(width,height)

    for row in range(height):
        for col in range(width):
            originalPixel = oldimage.getPixel(col,row)
            newPixel = noGreen(originalPixel)
            newim.setPixel(col,row,newPixel)

    newim.setPosition(width+1,0)
    newim.draw(myimagewindow)
    myimagewindow.exitOnClick()



        
