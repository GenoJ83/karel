from stanfordkarel import *

def main():
    """
    Karel walks down a row and picks up ANY beepers it finds.
    This teaches the 'if' statement and checking for beepers.
    """
    while front_is_clear():
        # Check if there is a beeper on this square
        if beepers_present():
            pick_beeper()
            
        # Keep moving forward regardless
        move()
        
    # Check the very last square just in case!
    if beepers_present():
        pick_beeper()

if __name__ == "__main__":
    # The default world might not have beepers scattered, 
    # but you can add them manually in the UI before pressing "Run"
    run_karel_program()
