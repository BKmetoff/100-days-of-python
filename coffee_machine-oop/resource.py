class Resource:
    def __init__(self, name, amount):
        self._name = name
        self._amount = amount

    def is_enough(self, needed_amount):
        return self._amount >= needed_amount

    def use(self, needed_amount):
        self._amount -= needed_amount

    def get_availability(self):
        return self._amount

    def get_name(self):
        return self._name
