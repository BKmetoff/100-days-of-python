from ruamel.yaml import YAML
from utils import coins, beverages, initial_resources, messages, ui_menu, additional_options, boolean_choice
from coin_collector import CoinCollector
from resource import Resource
from prompt import Prompt
from validator import Validator

# make coffee:
#   - ask user to select option
#   - validate user input
#   - check available resources
#   - collect coins
#   - collect until enough
#   - update current profit
#   - subtract from resources
#   - serve beverage
#   - repeat until out of resources or quit
#   - extra input optinos: 'report' & 'quit'


class CoffeeMachine:
    def __init__(self):
        self._coin_collector = CoinCollector()
        self._validator = Validator()
        self._continue_ordering = True
        self._selected_beverage = {}
        self._prompter = Prompt()
        self._resources = {
            'water': Resource(initial_resources[0]['type'],
                              initial_resources[0]['amount']),
            'milk': Resource(initial_resources[1]['type'],
                             initial_resources[1]['amount']),
            'coffee': Resource(initial_resources[2]['type'],
                               initial_resources[2]['amount'])
        }

    def _prompt(self, generic_copy, calculated_copy=None, is_error=False):
        if is_error:
            print(self._prompter.error(generic_copy))
        else:
            print(self._prompter.say(generic_copy, calculated_copy))

    def _enforce_validation(
        self,
        ui_message,
        input_options,
        input_prompt=None,
        user_input=None
    ):
        """
        ui_message -> plain text output,\n
        input_options -> pool of allowed values,\n
        input_prompt -> text displayed on user input,\n
        user_input -> value entered by user
        """

        choice = ''
        input_text = '' if input_prompt is None else input_prompt
        ui_text = '' if ui_message is None else ui_message

        self._prompt(ui_text)
        if user_input == None:
            choice = input(f"{input_text} ").lower()
        else:
            choice = user_input

        #   enforce:
        while not self._validator.valid_option(choice, input_options):
            self._prompt(ui_text)
            choice = input(f"{input_text} ").lower()

        return choice

    #   ask user to select option
    def _select_beverage(self):
        available_beverages = '/'.join(
            (beverages[b]['name'] for b in beverages)
        )

        choice = self._enforce_validation(
            ui_message=messages['select'],
            input_prompt=available_beverages,
            input_options=ui_menu,
            user_input=None
        )

        if choice in additional_options:
            self._selected_beverage = choice
        else:
            self._selected_beverage = beverages[choice]

    #   check available resources
    def _check_available_resources(self):
        for r in self._resources:
            resource_name = self._resources[r].get_name()
            required_amount = self._selected_beverage['ingredients'][resource_name]

            if not self._resources[r].is_enough(required_amount):
                self._prompt(
                    f"{messages['error']} {resource_name}! {messages['quit']}")
                quit()

            #   subtract resources
            else:
                self._resources[r].use(required_amount)

    #   collect coins
    def _collect_coins(self):
        self._prompt(messages['insert_coins'])
        self._prompt(messages['coin'])
        for coin in coins:
            self._coin_collector.collect(coins[coin])

    #   collect $$$ until enough
    def _collect_remaining_amount(self):
        beverage_cost = self._selected_beverage['cost']
        user_input = self._coin_collector._get_user_input()

        while not self._coin_collector.input_is_enough(beverage_cost):
            user_input = self._coin_collector._get_user_input()
            error_message = (
                f"{messages['insert_remaining']} "
                f"{round(beverage_cost - user_input, 2)}"
            )

            self._prompt(error_message)
            self._collect_coins()

    #   serve beverage
    def _serve(self):
        self._prompt(messages['serve'], self._selected_beverage['name'])

    #   continue until quit or out of resources
    def _continue_operation(self):
        choice = self._enforce_validation(
            ui_message=None,
            input_prompt=messages['continue'],
            input_options=boolean_choice,
            user_input=None,
        )

        if boolean_choice[choice]:
            return boolean_choice[choice]
        else:
            self._prompt(messages['quit'])
            return boolean_choice[choice]

    #   print available resources & profit:
    def _report(self):
        remaining_resources = " / ".join(
            str(self._resources[r].get_availability())
            for r in self._resources
        )

        self._prompt(messages['report'], remaining_resources)
        self._prompt(messages['profit'], self._coin_collector.get_profit())

    #   start
    def _start(self):
        self._prompt(messages['intro'])

        while self._continue_ordering:
            self._select_beverage()

            if self._selected_beverage == additional_options['report']:
                self._report()
                self._select_beverage()
            elif self._selected_beverage == additional_options['quit']:
                self._prompt(messages['quit'])
                quit()

            self._check_available_resources()
            self._collect_coins()
            self._collect_remaining_amount()
            self._serve()
            self._continue_ordering = self._continue_operation()

        quit()


if __name__ == '__main__':
    machine = CoffeeMachine()
    machine.start()
