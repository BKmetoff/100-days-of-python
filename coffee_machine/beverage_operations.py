from input_prompt import input_prompts


def select_coffee(menu, resources):
    selected_coffee = input(input_prompts('start_order', menu))

    while selected_coffee not in "/".join(list(menu.keys())):
        if selected_coffee == 'report':
            print(input_prompts('report', resources))
        elif selected_coffee == 'quit':
            print(input_prompts('quit'))
            quit()
        else:
            print("invalid input")

        selected_coffee = input(input_prompts('start_order', menu))

    return menu[selected_coffee]


def serve_coffee(selected_coffee):
    print(input_prompts('complete_order', selected_coffee['name']))
