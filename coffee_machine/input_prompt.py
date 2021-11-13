from utils import plurarize


def input_prompts(prompt_type, copy=None):

    water, milk, coffee, order, coin_type = [""] * 5
    coffee_options = {}
    change = 0
    remaining_cash = 0

    argument_type = type(copy)

    if argument_type == list:
        water, milk, coffee = copy
    elif argument_type == dict:
        coffee_options = "/".join(list(copy.keys()))
    elif argument_type == float:
        change = copy
        remaining_cash = copy
    else:
        order = copy
        if copy != None:
            coin_type = plurarize(copy)

    prompts = {
        'intro': 'This be Coffee Machine!',
        'report': f"Water: {water}ml\nMilk: {milk}ml\nCoffee {coffee}gr",
        'start_order': f"What would you like: ({coffee_options}): ",
        'complete_order': f"Here is your {order}. Enjoy!",
        'insert_coins': 'Please, insert coins!',
        'coin': f"How many {coin_type}? ",
        'return_change': f"Here is ${change} in change.",
        'insufficient_ingredients': "Sorry, not enough ingredients.",
        'insufficient_cash':
            f"Sorry, not enough $$$, insert ${round(remaining_cash, 2)}.",
        'quit': "Goodbye!"

    }

    return prompts.get(prompt_type)
