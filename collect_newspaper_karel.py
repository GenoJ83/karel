from stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def move_to_newspaper():
    """Moves Karel from the starting position to the newspaper."""
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()

def return_to_start():
    """Returns Karel back to the starting point and starting direction."""
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()

def main():
    """
    Collects the newspaper (beeper) from outside the house
    and returns it to Karel's starting position.
    """
    move_to_newspaper()
    pick_beeper()
    return_to_start()

if __name__ == "__main__":
    # Note: make sure you have CollectNewspaperKarel.w or similar world file
    run_karel_program()
