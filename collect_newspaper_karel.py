from stanfordkarel import *

def turn_right():
    # Karel turns left 3 times to simulate turning right
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    # Karel turns left 2 times to face the opposite direction
    turn_left()
    turn_left()

def move_to_newspaper():
    """Moves Karel from the starting position to the newspaper."""
    move()         # Walk to the wall
    move()         # Walk to the corner
    turn_right()   # Face South to go down to the door
    move()         # Move down to the doorway
    turn_left()    # Face East to go outside
    move()         # Step outside to the newspaper

def return_to_start():
    """Returns Karel back to the starting point and starting direction."""
    turn_around()  # Turn around to face West
    move()         # Step back inside the house
    turn_right()   # Face North
    move()         # Move up to the starting row
    turn_left()    # Face West
    move()         # Walk back to the starting corner
    move()         # Arrive at starting position
    turn_around()  # Turn around to face East again

def main():
    """
    Collects the newspaper (beeper) from outside the house
    and returns it to Karel's starting position.
    """
    move_to_newspaper() # Execute our custom function to go outside
    pick_beeper()       # Pick up the newspaper
    return_to_start()   # Execute our custom function to go home

if __name__ == "__main__":
    # Launch the specific Collect Newspaper world
    run_karel_program("collect_newspaper_karel")
