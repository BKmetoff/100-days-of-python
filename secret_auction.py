import os


def input_types():
    return ["name", "bid"]


def user_input(input_type):
    return input(f"Enter your {input_type}:\n")


def add_participant(current_participants, new_participant):
    current_participants.append(new_participant)
    return current_participants


def find_highest_bid(participants):
    winner = {}
    highest_bid = 0
    for p in participants:
        if p["bid"] > highest_bid:
            highest_bid = p["bid"]
            winner = p

    return winner


def clear_console():
    return os.system('cln' if os.name in ('nt', 'dos') else 'clear')


def execute():
    inputs = input_types()
    participants = []

    while input("add participant: y/n\n") == "y":
        name = user_input(inputs[0])
        bid = int(user_input(inputs[1]))
        participants = add_participant(
            participants, {inputs[0]: name, inputs[1]: bid}
        )
        clear_console()

    print(f"Winner: {find_highest_bid(participants)}")
    quit()


execute()
