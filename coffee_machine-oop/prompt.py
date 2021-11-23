class Prompt:
    def say(self, generic_copy, calculated_copy=None):
        if calculated_copy is None:
            return f"{generic_copy}"
        else:
            return f"{generic_copy} {calculated_copy}"

    def error(self, copy):
        return f"Error! {copy}"
