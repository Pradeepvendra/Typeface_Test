#import pillow
from PIL import Image, ImageDraw
#Taking input and multiplying to enlarge the values for big canvas

dimension=[int(i)*10 for i in input().split()]

# creating new Image object
img = Image.new("RGB", (500,500))

img1 = ImageDraw.Draw(img) 

# create ellipse point for the image with co-ordinates of our intial x,y
img1.ellipse((dimension[0]-5, dimension[1]-5, dimension[0]+5, dimension[1]+5), fill = 'white')

# create rectangle image as the boundary line for the point by using width and heigth
img1.rectangle((dimension[0]-dimension[2], dimension[1]+dimension[3], dimension[0]+dimension[2], dimension[1]-dimension[3]), fill =None, outline ="red")


img.show()
