additional_options = {
    'report': 'report',
    'quit': 'quit',
}

boolean_choice = {
    'y': True,
    'n': False
}

coins = {
    'penny': {
        'name': 'penny',
        'value': 0.01,
    },
    'nickel': {
        'name': 'nickel',
        'value': 0.05,
    },
    'dime': {
        'name': 'dime',
        'value': 0.10,
    },
    'quarter': {
        'name': 'quarter',
        'value': 0.5,
    },
}

beverages = {
    "espresso": {
        "name": "Espresso",
        "cost": 1.5,
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
    },
    "latte": {
        "name": "Latte",
        "cost": 2.5,
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
    },
    "cappuccino": {
        "name": "Cappuccino",
        "cost": 3.0,
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
    }
}


messages = {
    'intro': 'This be Coffee Machine!',
    'report': '\nWater(ml) / Milk(ml) / Coffee(gr):',
    'profit': 'Profit: $',
    'select': '\nWhat would you like:',
    'serve': 'Here is your order:',
    'insert_coins': '\nPlease, insert coins',
    'insert_remaining': '\nInsert remaining $',
    'coin': 'How many...',
    'change': 'Here is your change: $',
    'ingredients': "Insufficient ingredients!",
    'continue': "Order something else? y/n",
    'quit': 'Goodbye!',
    'error': 'Insufficient'
}


ui_menu = \
    [k for k, v in beverages.items()] + \
    [k for k, v in additional_options.items()]


initial_resources = [
    {'type': 'water', 'amount': 500},
    {'type': 'milk', 'amount': 300},
    {'type': 'coffee', 'amount': 200},
]


def plurarize(coin_name):
    if coin_name[-1] == 'y':
        return coin_name.replace('y', 'ies')
    else:
        coin_name += 's'

    return coin_name
