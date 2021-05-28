#@uthor AK
"""
This program highlights fires in an image by identifying pixels
whose red intensity is more than INTENSITY_THRESHOLD times the
average of the red, green, and blue values at a pixel. Those
"sufficiently red" pixels are then highlighted in the image
and other pixels are turned grey, by setting the pixel red,
green, and blue values to be all the same average value.
"""

from simpleimage import SimpleImage

INTENSITY_THRESHOLD = 1.0
img = 'images/greenland-fire.png'

def find_flames(img):
    """
    This function should highlight the "sufficiently red" pixels
    in the image and grayscale all other pixels in the image
    in order to highlight areas of wildfires.
    """
    image = SimpleImage(img)
    # TODO: your code here
    for px in image:
        avg = (px.red + px.green + px.blue)/3
        #print("1-->",px.red)
        if px.red > avg:
            px.red = px.red *225
            px.green = 1
            px.blue = 1
        else:
            px.red =avg
            px.green =avg
            px.blue = avg
    return image

def main():
    # Get file name from user input
    #filename = get_file()
    #fil=filt()
    # Show the original fire
    original_fire = SimpleImage(img)
    original_fire.show()

    # Show the highlighted fire
    fire = find_flames(img)
    fire.show()

if __name__ == '__main__':
    main()
