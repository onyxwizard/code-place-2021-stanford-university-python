# Q2: Finding Forest Flames

We’re going to start by writing a function called find_flames (in the file forest_fire.py) that highlights the areas where a forest fire is active. You’re given a satellite image of Greenland’s 2017 fires (photo credit: Stef Lhermitte, Delft University of Technology).

Your job is to detect all of the “sufficiently red” pixels in the image, which are indicative of where fires are burning in the image. As we did in class with the “redscreening” example, we consider a pixel “sufficiently red” if its red value is greater than or equal to the average of the pixel’s three RGB values times a constant INTENSITY_THRESHOLD. 

Recall the average of a pixel, which has red, green and blue values is:
```
average = (red + green + blue) / 3
```
When you detect a “sufficiently red” pixel in the original image, you set its red value to 255 and its green and blue values to 0. This will highlight the pixel by making it entirely red. For all other pixels (i.e., those that are not “sufficiently red”), you should convert them to their grayscale equivalent, so that we can more easily see where the fire is originating from. You can grayscale a pixel by summing together its red, green, and blue values and dividing by three (finding the average), and then setting the pixel’s red, green, and blue values to all have this same “average” value.
<p align="center">
<img align="center" src="/images/a3-q21.png">
</p>


Two side by side photos of smoke plumes from above. The first photo is a normal image, taken from a satellite, and the right image is the same as the previous except it is black and white and the forest fires are highlighted in red.

Original forest fire image on left, and highlighted version of image on right.

Once you highlight the areas that are on fire in the image (and greyscale all the remaining pixels), you should see an image like that shown on the right in the figure. On the left side of the example image, we should the original image for comparison. 

Note: to make this algorithm work on different images of fire, select an appropriate INTENSITY_THRESHOLD value.
