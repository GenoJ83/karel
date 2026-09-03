from stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def safe_put_beeper():
    """Places a beeper only if there isn't one already."""
    if not beepers_present():
        put_beeper()

def repair_column():
    """
    Karel climbs the column, placing beepers where missing, 
    and then returns to the bottom facing East.
    """
    turn_left()  # Face North to climb
    while front_is_clear():
        safe_put_beeper()
        move()
    safe_put_beeper()  # Don't forget the very top of the column!
    
    # Return to the bottom
    turn_around()  # Face South to descend
    while front_is_clear():
        move()
    turn_left()  # Face East again for the next column

def move_to_next_column():
    """Moves Karel exactly 4 avenues to the next column."""
    for _ in range(4):
        move()

def main():
    """
    Karel repairs the arches (columns) that are spaced 4 avenues apart.
    """
    while True:
        repair_column()
        
        # If the front is clear, it means there are more columns to repair
        if front_is_clear():
            move_to_next_column()
        else:
            break

if __name__ == "__main__":
    run_karel_program("stone_mason_karel")
