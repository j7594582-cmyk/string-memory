import os
import random
import time
import msvcrt


def clear_screen():
    """
    clear the terminal console screen based on the operating system.
    """
    os.system("cls" if os.name == "nt" else "clear")


def clear_keyboard_buffer():
    """
    remove any mending keystrokes from keyboard buffer
    """
    while msvcrt.kbhit():
        msvcrt.getwch()


def print_countdown():
    """
    display five dots, one at a time with a one second delay between them
    """
    for _ in range(5):
        time.sleep(1)
        print(".", end="", flush=True)
    print()


def generate_string(level):
    """
    generate a random uppercase string of length 3 and above
    """
    length = int(level) + 3
    letters = [random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(length)]
    return "".join(letters)


def play_level(level):
    """
    run a single level of the game

    return teh string and the player's guess
    """
    correct_str = generate_string(level)
    print(f"level{level}\n")
    print(correct_str)
    clear_keyboard_buffer
    guess = input("Enter the string you just saw(case sensitive): ")
    return correct_str, guess.strip()


def display_game_over(level, correct_str, guess):
    """
    show the final score, correct/incorrect stringer and performance evaluation
    """
    completed_levels = level - 1
    print("incorrect!\n")
    print(f"correct string {correct_str}")
    print(f"your answer: {guess}\n")
    print(f"you successfully made it through lvels {completed_levels}.\n")

    if completed_levels <= 2:
        print("wow, did you understand the game?")
    elif completed_levels <= 6:
        print("wow! im surprised")
    else:
        print("nice job! you're a memory master!")


def ask_replay():
    """
    promt the user until they give a valid Y/N response to play again
    """
    choice = input("\nwould you like to play again?(Y/N): ").strip().upper()
    if choice in ("Y", "N"):
        return choice


def game_loop():
    """
    manages the main game loop
    """
    correct_str = generate_string(level)
    level = 1
    while True: 
        correct_str, guess = play_level(level)

        if guess.upper() == correct_str:
            print("good job!")
            time.sleep(3)
            clear_screen()
            level += 1
        else:
            display_game_over(level, correct_str, guess)
        break


def main():
    """
    handle initial startup logic and the outer loop for total game replayability
    """
    clear_screen()
    start_input = input("press Q to quit or anything else to start the game: ")
    if start_input.strip().upper() == "Q":
        print("have a good day")
        return

    while True:
        clear_screen()
        game_loop()

        if ask_replay() == "N":
            print("have a wonderful day") 
            break

if __name__ == "__main__":
    main()