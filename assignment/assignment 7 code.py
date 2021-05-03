def main():
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()
    if front_is_clear():
        move()
    midpoint()

def midpoint():
    while no_beepers_present():
        move()
        if beepers_present():
            pick_beeper()
            turn_around()
            move()
            put_beeper()
            move()
    if beepers_present():
        pick_beeper()
        turn_around()
        if front_is_clear():
            move()

def turn_around():
      turn_left()
      turn_left()

if __name__ == '__main__':
    run_karel_program()
