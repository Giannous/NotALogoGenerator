# import all the libraries
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy
from numpy import random

circle = Image.open('.\\shapes\\circle.png')
triangle = Image.open('.\\shapes\\triangle.png')
square = Image.open('.\\shapes\\square.png')

shapes = [circle, triangle, square]

blank_image = Image.new("RGB", (600, 600), (255, 255, 255))  # Crea immagine con sfondo bianco 600x600

# draw = ImageDraw.Draw(blank_image)
# draw.rounded_rectangle(xy=(10, 20, 190, 180), radius=30, fill="red")

blank_image.save('.\\generated_images\\blank_background.png')

blank_image_copy = blank_image.copy()

radius = 20  # Radius in pixel
area = 3.14 * radius * radius  # Pi * radius^2, not sure if I need it now

for n in range(1000):
    x = random.randint(0, 600, size=2)  # Random Position coordinate

    # Array of (x,y) tuples to make a cross
    radiusToChek = [(x[0] - radius, x[1]), (x[0], x[1] + radius), (x[0] + radius, x[1]), (x[0], x[1] - radius)]

    nearShapeFlag = False  # Flag to check if there is a nearby shape

    # Loop to check if there is a nearby shape, if yes we put the flag to true and break from the loop
    for point in radiusToChek:
        try:
            if ((blank_image_copy.getpixel(point)) != (
            255, 255, 255)):  # If the color is not 255 (white) means there is another shape
                nearShapeFlag = True
                break
        except Exception as ex:  # For now when i try to get coordinate outside the image i catch the exception, raise and go on
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)

    if nearShapeFlag: continue

    imgIndex = random.randint(3)  # Random index to pick a shape from the array of shapes
    shape = shapes[imgIndex]  # Getting the shape with the random index
    shape = shape.resize((30, 30))  # Resizing the shape
    blank_image_copy.paste(shape, (x[0], x[1]))  # Copying the shape

# blank_image_copy.show()
blank_image_copy.save('.\\generated_images\\logo.png')
