from utils import plurarize, messages
from validator import Validator


class CoinCollector:
    def __init__(self):
        self._profit = 100.00
        self._current_user_input = 0
        self._validator = Validator()

    def _enforce_validation(self, input_prompt, data_type):
        num_of_coins = input(f"{input_prompt}: ")

        while not self._validator.valid_type(num_of_coins, data_type):
            num_of_coins = input(f"{input_prompt}")

        return num_of_coins

    def _deposit(self, amount):
        self._profit += amount

    def _return_change(self, change):
        print(f"{messages['change']} {round(change, 2)}")

    def _get_user_input(self):
        return self._current_user_input

    def _reset_current_user_input(self):
        self._current_user_input = 0

    def input_is_enough(self, beverage_cost):
        if beverage_cost > self._current_user_input:
            return False

        elif self._current_user_input > beverage_cost:
            change = self._current_user_input - beverage_cost
            self._return_change(change)
            self._deposit(beverage_cost)
            self._reset_current_user_input()
            return True

        else:
            self._deposit(beverage_cost)
            self._reset_current_user_input()
            return True

    def get_profit(self):
        return self._profit

    def collect(self, coin):
        pluralized_coin_name = plurarize(coin['name'])
        num_of_coins = self._enforce_validation(
            f"{pluralized_coin_name}",
            'number'
        )
        self._current_user_input += float(num_of_coins) * coin['value']
