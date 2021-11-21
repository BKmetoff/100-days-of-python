class Validator:
    def __init__(self):
        pass

    def valid_option(self, user_input, options):
        if user_input not in options:
            return False
        else:
            return True

    #   lame but sufficient
    def valid_type(self, user_input, data_type):
        if data_type == 'number':
            try:
                float(user_input)
                return True
            except:
                return False
