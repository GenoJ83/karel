from stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def main():
    """
    Draws a checkerboard pattern of beepers in any sized world!
    It uses a Python boolean variable to remember if it should 
    place a beeper on the current square or not.
    """
    should_place = True
    
    while True:
        # 1. Place a beeper if it's the correct alternating square
        if should_place:
            put_beeper()
            
        # 2. Try to move forward in the current row
        if front_is_clear():
            move()
            # Flip the boolean for the next square
            should_place = not should_place
        else:
            # 3. We hit a wall! We need to move up to the next row.
            if facing_east():
                # We are at the right wall, move up and face West
                if left_is_clear():
                    turn_left()
                    move()
                    turn_left()
                    # The next square should be the opposite of the last one
                    should_place = not should_place
                else:
                    # No more rows above us, we are done!
                    break
            else:
                # We are at the left wall, move up and face East
                if right_is_clear():
                    turn_right()
                    move()
                    turn_right()
                    should_place = not should_place
                else:
                    # No more rows above us
                    break

if __name__ == "__main__":
    run_karel_program(world_text="Dimension: (8, 8)\nKarel: (1, 1); east\nBeeperBag: INFINITY", main_func=main)
