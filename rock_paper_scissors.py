import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]


def get_player_choice():
    return input("\n\nchoose 0 for rock, 1 for paper, 2 for scissors, or 4 to stop the game.\n")


def stop_game():
    print("Thank you for playing")
    quit()


def get_computer_choice(): return random.randint(0, 2)


def display_choice(choice): print(options[choice])


def calculate_winner(player, computer):
    difference = player - computer

    if difference == 0:
        return "Tie"
    elif difference % 3 == 1:
        return "You win"
    elif difference % 3 == 2:
        return "You lose"


def error_message():
    print("Incorrect input. Try again.")


def play_game():
    while True:
        player = get_player_choice()

        try:
            player = int(player)
        except:
            error_message()
            continue

        if player == 4:
            stop_game()
            return

        try:
            display_choice(player)
        except:
            error_message()
            continue

        print("Computer got:")
        computer = get_computer_choice()
        display_choice(computer)

        print(calculate_winner(player, computer))


play_game()
