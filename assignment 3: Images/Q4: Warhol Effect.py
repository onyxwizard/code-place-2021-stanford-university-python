"""
This program generates the Warhol effect based on the original image.
"""
from simpleimage import SimpleImage
N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'
def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    # This is an example which should generate a pinkish patch
    img = PATCH_NAME
    red(img)
    green(img)
    blue(img)
    dgreen(img)
    yel(img)
    org(img)
    f = mr(img)
    f.show()
    '''
    Implement this function to make a patch for the Warhol Filter.
    It loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixel's red component by
    :param green_scale: A number to multiply each pixel's green component by
    :param blue_scale: A number to multiply each pixel's blue component by
    Returns the newly generated patch.
    '''
def mr(pic):
    r = red(pic)
    g = green(pic)
    b = blue(pic)
    dg = dgreen(pic)
    ye = yel(pic)
    o = org(pic)
    patch = SimpleImage(pic)
    width = patch.width
    height = patch.height
    mirror = SimpleImage.blank(width*3,height*2)
    for x in range(width):
        for y in range(height): 
            #color to apply for images
            rd = r.get_pixel(x,y)
            bl = b.get_pixel(x,y)
            grn = g.get_pixel(x,y)
            dgrn = dg.get_pixel(x,y)
            yello = ye.get_pixel(x,y)
            orange = o.get_pixel(x,y)
            #pixel arrange in rows/columns
            mirror.set_pixel(x,y,rd)
            mirror.set_pixel((width*1)+x,y,bl)
            mirror.set_pixel((width*2)+x,y,grn)
            mirror.set_pixel(x,(height*1)+y,dgrn)
            mirror.set_pixel((width*1)+x,(height*1)+y,yello)
            mirror.set_pixel((width*2)+x,(height*1)+y,orange)
    return mirror
def red(pic):
    patch = SimpleImage(pic)
    for px in patch:
        px.red = px.red // 1 #float(red_scale)
        px.green = 0 #float(green_scale)
        px.blue =0 #float(blue_scale)
    return patch
def green(pic):
    patch = SimpleImage(pic)
    for px in patch:
        px.red =  0 #float(red_scale)
        px.green =px.green // 1 #float(green_scale)
        px.blue = 0 #float(blue_scale)
    return patch
def dgreen(pic):
    patch = SimpleImage(pic)
    for px in patch:
        px.red = px.red #float(red_scale)
        px.green =px.green #float(green_scale)
        px.blue = px.blue #float(blue_scale)
    return patch
def yel(pic):
    patch = SimpleImage(pic)
    for px in patch:
        px.red = px.red //1 #float(red_scale)
        px.green =px.green // 5 #float(green_scale)
        px.blue =px.blue // 2 #float(blue_scale)
    return patch
def org(pic):
    patch = SimpleImage(pic)
    for px in patch:
        px.red = px.red // 1 #float(red_scale)
        px.green =px.green // 2 #float(green_scale)
        px.blue =px.blue // 7 #float(blue_scale)
    return patch
def blue(pic):
    patch = SimpleImage(pic)
    for px in patch:
        px.red = 0 #float(red_scale)
        px.green = 0 #float(green_scale)
        px.blue =px.blue // 1 #float(blue_scale)
    return patch
if __name__ == '__main__':
    main()
