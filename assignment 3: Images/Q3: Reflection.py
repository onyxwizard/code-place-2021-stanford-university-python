#@uthor AK
"""
This program takes an image and generates a reflection.
The top half of the generated image is the same as the original.
The bottom half is the mirror reflection of the top half.
"""

from simpleimage import SimpleImage

img = 'images/mt-rainier.jpg'


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
    mirror = SimpleImage.blank(width,height*2)
    for x in range(width):
        for y in range(height): 
            pixel = image.get_pixel(x,y)
            mirror.set_pixel(x,y,pixel)
            #if to set reflection in opposite direction add ((width-1)-x) to x co-ordinate
            mirror.set_pixel(x,((height*2)-2)-(y),pixel)
    print(width,height*2)
    return mirror

if __name__ == '__main__':
    main()
