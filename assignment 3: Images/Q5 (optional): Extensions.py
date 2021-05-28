#@uthor AK
"""
This program takes an image and generates a reflection of opposite direction.
"""

from simpleimage import SimpleImage
#select your location of the image
img = 'net.jpg'


def main():
    # Get file name from user input
    filename = get_file()

    # Show the original image
    original = SimpleImage(filename)
    original.show()

    # Show the reflected image
    reflected = make_reflected(filename)
    reflected.show()

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = img
    return filename

def make_reflected(filename):
    image = SimpleImage(filename)
    # TODO: your code here.
    width = image.width
    height = image.height
    mirror = SimpleImage.blank(width,height*3)
    for x in range(width):
        for y in range(height): 
            pixel = image.get_pixel(x,y)
            #ORIGINAL IMAGE
            mirror.set_pixel(x,y,pixel)
            #REFLECTION IMAGE
            mirror.set_pixel(x,((height*2)-2)-(y),pixel)
            #REFLECTION IMAGE(OPPOSITE DIRECTION)
            mirror.set_pixel((width-1)-x,((height*3)-3)-(y),pixel)
    return mirror


if __name__ == '__main__':
    main()
