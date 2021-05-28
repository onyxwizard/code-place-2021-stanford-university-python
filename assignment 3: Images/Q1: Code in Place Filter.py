"""
This program implements a rad image filter.
@author AK
"""

from simpleimage import SimpleImage

img = 'images/quad.jpg'

    # Apply the filter
def filt():
    # Read image file path from user, or use the default file
    name = SimpleImage(img)
    for px in name: 
      px.red = px.red * 1.5
      px.green = px.green * 0.7
      px.blue = px.blue * 1.5
    return name
def main():
    # Get file name from user input
    filename = filt()
    # Load image and show image before the transform
    image = SimpleImage(img)
    image.show()
    # Show the image after the transform
    filename.show()

if __name__ == '__main__':
    main()
