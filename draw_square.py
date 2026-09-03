from stanfordkarel import *

def draw_side():
    """
    Karel puts a beeper and moves forward 3 times.
    This creates one side of the square.
    """
    for _ in range(3):
        put_beeper()
        move()

def main():
    """
    Karel draws a 4x4 square of beepers.
    It draws 4 sides, turning left at each corner.
    """
    for _ in range(4):
        draw_side()
        turn_left()

if __name__ == "__main__":
    run_karel_program("8x8")
