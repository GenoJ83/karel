from stanfordkarel import *

def main():
    """Karel code goes here!"""
    move()
    turn_left()
    move()
    put_beeper()

if __name__ == "__main__":
    run_karel_program(world_text="Dimension: (10, 10)\nKarel: (1, 1); east\nBeeperBag: INFINITY", main_func=main)
