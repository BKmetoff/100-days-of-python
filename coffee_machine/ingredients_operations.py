def enough_ingredients(selected_coffee, current_ingredients):
    coffee_ingredients = selected_coffee['ingredients']
    for ingredient in coffee_ingredients:
        if current_ingredients[ingredient] < coffee_ingredients[ingredient]:
            return False

    return True


def update_ingredients(selected_coffee, current_ingredients):

    coffee_ingredients = selected_coffee['ingredients']
    for ingredient in coffee_ingredients:
        current_ingredients[ingredient] -= coffee_ingredients[ingredient]

    return current_ingredients
