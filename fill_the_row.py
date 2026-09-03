from stanfordkarel import *

def main():
    """
    Karel places a solid line of beepers across the entire floor.
    This teaches how to combine actions inside a while loop.
    """
    # As long as the path is clear...
    while front_is_clear():
        # Place a beeper on the current square
        put_beeper()
        # Take a step forward
        move()
        
    # CRITICAL: We hit the wall! But we haven't placed a beeper 
    # on the very last square yet because the loop stopped.
    # So we must manually place one last beeper at the end!
    put_beeper()

if __name__ == "__main__":
    # Karel needs infinite beepers in its bag for this
    run_karel_program()
