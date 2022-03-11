# import all the libraries
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy
from numpy import random

blank_image = Image.new("RGB", (600, 600), (255, 255, 255))  # Creating a white background 600x600

# Creating masks with various shapes, i'll then create rectangular shapes of one color and i'll paste
# The rectangles on the white background applying a rando mask, effectively "drawing" a shape on the image

# Circle mask
circleMask = Image.new("L", (200, 200), 0)
draw = ImageDraw.Draw(circleMask)
draw.ellipse((50, 50, 150, 150), fill=255)
circleMask.save('.\\masks\\mask_circle.jpg', quality=95)

# Square mask
squareMask = Image.new("L", (200, 200), 0)
draw = ImageDraw.Draw(squareMask)
draw.rectangle((50, 50, 150, 150), fill=255)
squareMask.save('.\\masks\\mask_square.jpg', quality=95)

# Triangle mask
triangleMask = Image.new("L", (200, 200), 0)
draw = ImageDraw.Draw(triangleMask)
draw.polygon(((50,150), (150,150), (100,50), (50,150)), fill=255)
triangleMask.save('.\\masks\\triangle_square.jpg', quality=95)

# Creating the colors
red = Image.new("RGB", (200, 200), (246, 150, 121))
green = Image.new("RGB", (200, 200), (130, 202, 156))
blue = Image.new("RGB", (200, 200), (109, 207, 246))

colors =[red, green, blue]
masks = [circleMask, squareMask, triangleMask]

blank_image.save('.\\generated_images\\blank_background.png')

blank_image_copy = blank_image.copy()

radius = 20  # Radius in pixel
area = 3.14 * radius * radius  # Pi * radius^2, not sure if I need it now

for n in range(10000):
    x = random.randint(0, 600, size=2)  # Random Position coordinate

    # Array of (x,y) tuples to make a cross
    radiusToCheck = [(x[0] - radius, x[1]), (x[0], x[1] + radius), (x[0] + radius, x[1]), (x[0], x[1] - radius),
                     ((x[0] - radius), (x[1] + radius)), ((x[0] + radius), (x[1] + radius)),
                     ((x[0] + radius), (x[1] - radius)), ((x[0] - radius), (x[1] - radius))]

    nearShapeFlag = False  # Flag to check if there is a nearby shape

    # Loop to check if there is a nearby shape, if yes we put the flag to true and break from the loop
    for point in radiusToCheck:
        try:
            if ((blank_image_copy.getpixel(point)) != (255, 255, 255)):  # If the color is not 255 (white) means there is another shape
                nearShapeFlag = True
                break
        except Exception as ex:  # When i try to get coordinate outside the image I catch the exception, raise it and put the flag to flase to avoid that paste
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            nearShapeFlag = True

    if nearShapeFlag: continue

    imgIndex = random.randint(3)  # Random index to pick a shape from the array of shapes (masks)
    colIndex = random.randint(3)
    shape = masks[imgIndex]  # Getting the shape with the random index
    color = colors[colIndex] # Getting the color with the random index
    shape = shape.resize((30, 30))  # Resizing the shape
    color = color.resize((30, 30))  # Resizing the color because it's an image too
    blank_image_copy.paste(color, (x[0], x[1]), shape)  # Pasting the color with the shape mask

blank_image_copy.show()
blank_image_copy.save('.\\generated_images\\logo.png')
