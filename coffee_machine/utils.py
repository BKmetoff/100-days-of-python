coin_vault = {
    'penny': {
        'name': 'penny',
        'value': 0.01,
        'amount': 0
    },
    'nickel': {
        'name': 'nickel',
        'value': 0.05,
        'amount': 0
    },
    'dime': {
        'name': 'dime',
        'value': 0.10,
        'amount': 0
    },
    'quarter': {
        'name': 'quarter',
        'value': 0.5,
        'amount': 0
    },
}

coffee_types = {
    "espresso": {
        "name": "espresso",
        "cost": 1.5,
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
    },
    "latte": {
        "name": "latte",
        "cost": 2.5,
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
    },
    "cappuccino": {
        "name": "cappuccino",
        "cost": 3.0,
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
    }
}

initial_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def plurarize(coin_name):
    if coin_name[-1] == 'y':
        return coin_name.replace('y', 'ies')
    else:
        coin_name += 's'

    return coin_name
