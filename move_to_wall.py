
from stanfordkarel import *

def main():
    """
    Karel walks forward until it hits a wall.
    This teaches the most basic while loop and condition sensor!
    """
    # As long as there is no wall directly in front of Karel...
    while front_is_clear():
        # Take one step forward
        move()
        
    # When the loop finishes (because Karel hit a wall), the program ends.

if __name__ == "__main__":
    # We use an empty 10x10 world for this
    run_karel_program()
