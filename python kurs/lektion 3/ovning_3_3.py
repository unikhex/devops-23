import random

# Define ASCII art for each die face
dice_faces = [
    """
    -----
    |   |
    | o |
    |   |
    -----
    """,
    """
    -----
    |o  |
    |   |
    |  o|
    -----
    """,
    """
    -----
    |o  |
    | o |
    |  o|
    -----
    """,
    """
    -----
    |o o|
    |   |
    |o o|
    -----
    """,
    """
    -----
    |o o|
    | o |
    |o o|
    -----
    """,
    """
    -----
    |o o|
    |o o|
    |o o|
    -----
    """
]

def roll_die():
    return random.randint(1, 6)

def main():
    while True:
        input("Press Enter to roll the dice...")
        result = roll_die()
        print("You rolled a", result)
        print(dice_faces[result - 1])
        
        play_again = input("Do you want to roll again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    print("Welcome to the ASCII Dice Rolling Game!")
    main()
