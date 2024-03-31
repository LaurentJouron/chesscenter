import re
from pyfiglet import Figlet
from chesscenter.utils.constants import SIZE_LINE


def _get_string(var):
    pattern = r"^[a-zA-Z -àçéëêèïîôûù]+$"
    return bool(re.match(pattern, var))


def _get_int(var):
    pattern = r"^\d+$"
    return bool(re.match(pattern, var))


def _get_float(var):
    try:
        var = float(var)
        return True
    except ValueError:
        return False


class BaseView:
    string_validator = _get_string
    integer_validator = _get_int
    float_validator = _get_float

    def _get_string(self, prompt, validator=None):
        validator = validator or type(self).string_validator
        while True:
            answer = input(prompt).strip()
            if validator(answer) and answer > 0:
                return answer

    def _get_int(self, prompt, validator=None):
        validator = validator or type(self).integer_validator
        while True:
            answer = input(prompt).strip()
            if validator(answer):
                return int(answer)

    def _get_float(self, prompt, validator=None):
        validator = validator or type(self).float_validator
        while True:
            answer = input(prompt).strip()
            if validator(answer):
                return float(answer)

    def _select_number(self):
        while True:
            try:
                return input("Select the menu number: ")
            except ValueError as e:
                self._message_error(e)

    def _space_presentation(self, prompt):
        print(f"\n{prompt.center(SIZE_LINE, ' ')}".upper())

    def _double_point_presentation(self, prompt):
        print(f"\n{prompt.center(SIZE_LINE, ':')}")

    def _drew_presentation(self, prompt):
        print(f"\n{prompt.center(SIZE_LINE, '-')}")

    def _star_presentation(self, prompt):
        print(f"\n{prompt.center(SIZE_LINE, '*')}")

    def _value_error(self, value=""):
        if value != "":
            print(f"\n{value} is value error.")
        else:
            print("Value error.")

    def _success_message(self):
        print("Successfully.")

    def _display_message(self, prompt):
        print(prompt)

    def _display_pyfiglet(self, prompt):
        f = Figlet(font="ivrit")
        print(f.renderText(prompt))

    def _enter_information(self):
        return self._star_presentation(" Enter information ")

    def display_value_and_sentence(self, sentence, value):
        print(f"\n{sentence}: {value}")

    def display_made_your_choice(self):
        print(self._space_presentation(" MADE YOUR CHOICE "))
