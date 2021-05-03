from karel.stanfordkarel import *

def main():
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

def up():
    turn_left()
    beep()

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

if __name__ == '__main__':
    run_karel_program('SampleQuad1.w')
