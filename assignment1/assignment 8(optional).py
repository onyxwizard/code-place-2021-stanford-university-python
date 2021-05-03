from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter code.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    top()
    down()

def down():
    while facing_south():
        turn_left()
        if front_is_clear():
            tmove()
            top()

    
def top():
    while facing_east():
        up()
        if no_beepers_present():
            put_beeper()
        turn_left()
        up()
        #nxt()
        #beep()

def up():
    turn_left()
    beep()

def nxt():
    if front_is_blocked():
        right()
        tmove()
        right()

def beep():
    while front_is_clear():
        if beepers_present():
            move()
        else:
            put_beeper()
            move()

def tmove():
    move()
    move()
    move()
    move()

def right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program()
