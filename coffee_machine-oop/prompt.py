class Prompt:
    def __init__(self):
        pass

    def say(self, generic_copy, calculated_copy=None):
        if calculated_copy != None:
            return f"{generic_copy} {calculated_copy}"
        else:
            return f"{generic_copy}"

    def error(self, copy):
        return f"Error! {copy}"
