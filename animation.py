from microbit import *

# Learn how to make an animation.
def bang(n):
    display.clear()
    display.set_pixel(2,2,9)
    sleep(n)
    display.clear()
    display.show(Image.DIAMOND_SMALL)
    sleep(n)
    display.clear()
    display.show(Image.DIAMOND)
    sleep(n)
    display.clear()
    sleep(n)
# TODO: Add your code here. 
