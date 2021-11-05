import string


def input_types():
    return {
        "fst": "first number",
        "snd": "second number",
        "opr": "operation"
    }


def user_input(input_type):
    return input(f"What's the {input_type}? \n")


def flow_prompts(flow_type, prompt_param):
    flows = {
        "result": f"The result is {prompt_param}",
        "continue": f"Continue calculating with {prompt_param}? y/n\n",
        "stop": "Goodbye! Press Enter to quit."
    }

    if flow_type == "result":
        return print(f"{flows.get(flow_type)}")
    else:
        return input(flows.get(flow_type))


def error_message(error_type):
    invalid_types = ["operation", "input"]

    errors = {
        "opr": f"Invalid {invalid_types[0]}!",
        "int": f"Invalid {invalid_types[1]}!",
        "flow": f"Invalid {invalid_types[1]}!"
    }

    return print(errors.get(error_type, "Unknown error!"))


def calculate(first_number, second_number, operation):
    first_number = int(first_number)
    second_number = int(second_number)

    operations = {
        "+": first_number + second_number,
        "-": first_number - second_number,
        "*": first_number * second_number,
        "/": first_number / second_number,
    }

    return operations.get(operation)


def get_number(which_number):
    number = user_input(which_number)
    while not validate_input("int", number):
        error_message("int")
        number = user_input(which_number)

    return number


def get_operation(opr):
    operation = user_input(opr)
    while not validate_input("opr", operation):
        error_message("opr")
        operation = user_input(opr)

    return operation


def validate_input(input_type, user_input):
    if input_type == "int":
        return user_input in string.digits
    elif input_type == "opr":
        return user_input in ["+", "-", "*", "/"]
    elif input_type == "flow":
        return user_input in ["y", "n"]


def exectute():
    inputs = input_types()
    continue_with_result = "y"

    first_number = get_number(inputs["fst"])
    second_number = get_number(inputs["snd"])
    operation = get_operation(inputs["opr"])

    result = calculate(first_number, second_number, operation)

    while continue_with_result == "y":
        flow_prompts("result", result)

        continue_with_result = flow_prompts("continue", result)
        if continue_with_result == "n":
            continue

        while not validate_input("flow", continue_with_result):
            continue_with_result = flow_prompts("continue", result)

        first_number = result
        second_number = get_number(inputs["snd"])
        operation = get_operation(inputs["opr"])

        result = calculate(first_number, second_number, operation)

    flow_prompts("stop", "")
    quit()


exectute()
