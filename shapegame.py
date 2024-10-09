from random import choice
from time import sleep
from typing import Dict, List
from inputimeout import inputimeout, TimeoutOccurred
from setup.utility import clear_screen, count_down


def print_shape_lines(lines: List[str]) -> None:
    """
    Print lines of a shape.

    Parameters:
    lines (List[str]): The lines to print.
    """
    for line in lines:
        print(line)


def shape_game(diff: int, shapes: Dict[str, List[str]]) -> bool:
    """
    Main game function to guess the shape.

    Parameters:
    diff (int): Difficulty level.
    shapes (Dict[str, List[str]]): Dictionary of shape names and their ASCII art.

    Returns:
    bool: Whether the shape was guessed correctly or not.
    """
    shape_name, shape_lines = choice(list(shapes.items()))
    print("Welcome to the 3D Printer Game!")
    print("Try to guess the shape being printed.")
    count_down(5)
    
    guessed_correctly = False
    correct_id = None

    for i in range(1, len(shape_lines) + 1):
        clear_screen()
        print("Shapes available:")
        for idx, shape in enumerate(shapes.keys(), 1):
            print(f"{idx}: {shape}")
            if shape == shape_name:
                correct_id = idx

        print("Type 'quit' to exit.")
        print("3D Printer is drawing...\n")
        print_shape_lines(shape_lines[:i])
        
        try:
            guess = inputimeout(prompt="\nWhat is the shape? Give the number\n", timeout=diff)
        except TimeoutOccurred:
            guess = 'timeout'
        
        stripped_guess = guess.strip().lower()

        if guess == "quit":
            print("Thanks for playing!")
            break
        elif stripped_guess == shape_name or guess == str(correct_id):
            guessed_correctly = True
            break
        
        sleep(0.1)
        print("3D Printer is drawing...")
        sleep(0.1)
        print("3D Printer is drawing...")
        sleep(0.1)
        print("...")

    if guessed_correctly:
        print("\nCongratulations! You guessed correctly.")
    else:
        print(f"\nSorry, the correct answer was '{shape_name}'. Better luck next time!")
    
    return guessed_correctly
