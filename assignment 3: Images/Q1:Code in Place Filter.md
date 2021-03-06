# Q1: Code in Place Filter

Write a program that asks the user to enter an image file, loads that file and applies the “Code in Place” filter.
Photo of Stanford Main Quad on a nice day.
Same photo as previous but tinted pinkish purple.
<p align="center">
<img align="center" src="/images/a3-q11.png">
</p>
<p align="center">
<img align="center" src="/images/a3-q12.png">
</p>

To apply the Code in Place filter, you are going to change every **pixel** to have the following new red, green and blue values, based off the pixels old red, green and blue values:

```
new red value = old red value * 1.5
new green value = old green value * 0.7
new blue value = old blue value * 1.5
```

Problem written by Chris Piech. Inspired by image library and examples from Nick Parlante.
