from os import system, name
from time import sleep
from typing import List, Tuple, Dict, Optional


def get_int(prompt: str = "Please enter an integer: ") -> int:
    """
    Prompt the user to enter an integer and return it.

    Parameters:
    prompt (str): The prompt message to display to the user.

    Returns:
    int: The integer entered by the user.
    """
    while True:
        try:
            user_input = input(prompt)
            user_integer = int(user_input)
            return user_integer
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def count_down(n: int = 3) -> None:
    """
    Count down from a given number with a delay of 1 second.

    Parameters:
    n (int): The number to count down from.
    """
    for i in range(n, 0, -1):
        sleep(1)
        print(f"{i}")
    clear_screen()


def display_menu(options: List[str]) -> int:
    """
    Display a menu and get the user's choice.

    Parameters:
    options (List[str]): The list of options to display.

    Returns:
    int: The user's choice as an integer.
    """
    options_with_exit = options + ["Exit"]
    print("Please choose one of the following options:")
    for index, option in enumerate(options_with_exit, start=1):
        print(f"{index}. {option}")
    
    while True:
        choice = input("Enter your choice: ")
        try:
            choice_int = int(choice)
            if 1 <= choice_int <= len(options_with_exit):
                if choice_int == len(options_with_exit):
                    print("Exiting the program!")
                    exit()
                print(f"You chose option {choice_int}: {options_with_exit[choice_int - 1]}\n")
                return choice_int
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def clear_screen() -> None:
    """
    Clear the console screen.
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def find_diff(skill_lvl: int = 1, goal_lvl: int = 1, hack: int = 1, goal: str = "design") -> Tuple[int, int, int, str, int]:
    """
    Calculate the difficulty based on skill level, goal level, hack, and goal type.

    Parameters:
    skill_lvl (int): Skill level.
    goal_lvl (int): Goal level.
    hack (int): Hack level.
    goal (str): Goal type.

    Returns:
    Tuple[int, int, int, str, int]: The calculated difficulty parameters.
    """
    if goal_lvl == 4:
        goal_lvl = -2
    if goal_lvl < 0:
        if skill_lvl == 5:
            skill_lvl = -3
        else:
            skill_lvl = min(skill_lvl, 2)
    else:
        if skill_lvl == 5:
            skill_lvl = 2
    if abs(skill_lvl) - 1 >= abs(goal_lvl) and goal == "design":
        diff = max(0, min(5, 10 + 2 * abs(goal_lvl) - 3 * abs(skill_lvl) - hack))
    elif skill_lvl == 1:
        diff = 7
    else:
        diff = 5
    return skill_lvl, goal_lvl, hack, goal, diff


def get_data() -> Tuple[List[str], Dict[str, List[str]], List[str]]:
    """
    Get random data for 3D printing aspects, words, and shapes.

    Returns:
    Tuple[List[str], Dict[str, List[str]], List[str]]: Random words, shapes, and aspects.
    """
    random_aspects = [
        "Color", "Temperature", "Gradient", "Texture", "LayerHeight", "InfillDensity",
        "InfillPattern", "PrintSpeed", "ExtrusionRate", "NozzleDiameter", "BedTemperature",
        "CoolingFanSpeed", "PrintMaterial", "BuildVolume", "PrintTime", "Resolution",
        "SupportStructure", "Raft", "Skirt", "Brim", "OverhangAngle", "Retraction",
        "FilamentDiameter", "PrintOrientation", "ShellThickness"
    ]
    
    random_words = [
        "Vertex", "Edge", "Face", "Polygon", "Mesh", "Curve", "Surface", "Point",
        "Line", "Angle", "Bevel", "Extrusion", "Corner", "Intersection", "Arc",
        "Loop", "Ring", "Segment", "Plane", "Grid", "Patch", "Seam", "Junction",
        "Spline", "Contour"
    ]
    
    shapes = {
        "cube": [
            "  +------+",
            " /      /|",
            "+------+ |",
            "|      | +",
            "|      |/",
            "+------+"
        ],
        "bullet": [
            "    /\\    ",
            "   /  \\   ",
            "  / || \\  ",
            " /  ||  \\ ",
            "|   ||   |",
            "|   ||   |",
            "|   ||   |",
            "|   ||   |",
            "|   ||   |",
            "|   ||   |",
            "|   ||   |",
            " \\  ||  / ",
            "  \\_||_/  "
        ],
        "spiral": [
            " *********",
            "         *",
            " ******* *",
            " *  _  * *",
            " * * ) * *",
            " * *   * *",
            " * ***** *",
            " *       *",
            " *********"
        ],
        "circle": [
            "   ***   ",
            " *     * ",
            "*       *",
            "*       *",
            " *     * ",
            "   ***   "
        ],
        "triangles": [
            "   /\\   ",
            "  /  \\  ",
            " /____\\ ",
            " \\    / ",
            "  \\  /  ",
            "   \\/   "
        ],
        "cylinder": [
            "  .-----.  ",
            " |._____.' ",
            " |       | ",
            " |       | ",
            " |       | ",
            " |       | ",
            " |       | ",
            " |       | ",
            "  `-____,' "
        ]
    }
    return random_words, shapes, random_aspects


# Example usage of the functions
if __name__ == "__main__":
    words, shapes, aspects = get_data()
    print(words)  # Print random words
    print(shapes["cube"])  # Print cube shape
    print(aspects)  # Print random aspects
