from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    beep()

def beep():
    while no_beepers_present():
        put_beeper()
        if not_facing_east():
            turn_left()
            turn_left()
            turn_left()
            if front_is_clear():
                dim()
        else:
            dim()
        
def dim():
    move()
    move()
    turn_left()
    move()

if __name__ == '__main__':
    run_karel_program('RampKarel1.w')
