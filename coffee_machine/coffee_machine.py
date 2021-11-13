from input_prompt import input_prompts
from transactions import return_change, get_cash
from beverage_operations import select_coffee, serve_coffee
from ingredients_operations import enough_ingredients, update_ingredients
from utils import coffee_types, initial_resources

# make coffee:
#   - ask user to select option
#   - check available resources
#   - check if enough money
#   - subtract from resources
#   - update current money
#   - repeat untill out of resources
#   - extra input optinos: 'report' & 'quit'


def execute():
    menu = coffee_types
    current_payment = 0
    total_profit = 0
    resources = list(initial_resources.values())
    remaining_ingredients = initial_resources

    print(input_prompts('intro'))

    selected_coffee = select_coffee(menu, resources)

    while enough_ingredients(selected_coffee, remaining_ingredients):

        current_payment = get_cash()

        while current_payment < selected_coffee['cost']:
            remainder = selected_coffee['cost'] - current_payment
            print(input_prompts('insufficient_cash', remainder))
            current_payment += get_cash()

        if current_payment > selected_coffee['cost']:
            return_change(current_payment - selected_coffee['cost'])

            total_profit += selected_coffee['cost']
            remaining_ingredients =\
                update_ingredients(selected_coffee, remaining_ingredients)
            serve_coffee(selected_coffee)

        selected_coffee =\
            select_coffee(menu, list(remaining_ingredients.values()))

        resources = remaining_ingredients
        if not enough_ingredients(selected_coffee, remaining_ingredients):
            print(input_prompts('insufficient_ingredients'))
            continue

    quit()


execute()
