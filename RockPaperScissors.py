import random


def start_game():
    while True:
        valid_choice = False
        while not valid_choice:
            user_choice = int(input("Please enter 1 (for rock), 2 (for paper), 3 (for scissors): "))
            if user_choice not in [1, 2, 3]:
                print("Your choice is invalid. Please choose 1, 2, or 3.")
                break

            comp_choice = determine_computer_choice()
            valid_choice = determine_winner(user_choice, comp_choice)

        if not play_again():
            break


# computer choice
def determine_computer_choice():
    comp_choice = random.randint(1, 3)
    return comp_choice


def determine_winner(user_choice, comp_choice):

    print(f"You have chosen {'rock' if comp_choice == 1 else 'paper' if comp_choice == 2 else 'scissors'}")
    print(f"The computer has chosen {'rock' if comp_choice == 1 else 'paper' if comp_choice == 2 else 'scissors'}")

    # if a draw occurs, start process again
    if user_choice == comp_choice:
        print("DRAW -- PLAY AGAIN")
        valid_choice = False
        return valid_choice

    win_conditions = {
        1: 3,  # Rock beats Scissors
        2: 1,  # Paper beats Rock
        3: 2   # Scissors beats Paper
    }

    if comp_choice == win_conditions[user_choice]:
        print("You have won!!")
        valid_choice = True
        return valid_choice
    else:
        print("The computer has won: YOU LOSE")
        valid_choice = True
        return valid_choice


def play_again():
    while True:
        play = int(input("Do you want to play again? 1 for yes, 0 for no: "))
        if play == 0:
            return False
        elif play == 1:
            return True
        else:
            message = "Your choice is invalid. Please choose 0 or 1"
            print(message)


if __name__ == '__main__':
    start_game()