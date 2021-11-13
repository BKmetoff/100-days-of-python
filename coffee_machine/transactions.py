from input_prompt import input_prompts
from utils import coin_vault


def return_change(change):
    print(input_prompts('return_change', change))


def get_cash():
    print(input_prompts('insert_coins'))

    gathered_cash = 0
    for coin in coin_vault:
        num_of_coins = input(input_prompts('coin', coin_vault[coin]['name']))
        gathered_cash += coin_vault[coin]['value'] * int(num_of_coins)

    return gathered_cash
