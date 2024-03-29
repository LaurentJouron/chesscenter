from ..bases.views import BaseView
from datetime import datetime
import re


class BaseDate(BaseView):
    date_validator = None

    def display_format_error(self):
        print("Invalid date format. Please use dd-mm-aaaa format.")

    def display_invalid_date(self):
        print("Invalid date. Please enter a date not earlier than today.")

    def display_invalid_end_date(self):
        print("Invalid date. End date should not be earlier than start date.")

    def _get_date(self, prompt, validator=None):
        """
        Collect a date input from the user.

        Args:
            prompt (str): The input prompt.
            validator (function, optional): A validation function.
            Defaults to None.

        Returns:
            str: The user's input as a date.
        """
        validator = validator or type(self).date_validator
        while True:
            answer = input(prompt).strip()
            if self.validate_date(answer):
                return answer

    def validate_date(self, date):
        """
        Validate a date input.

        Args:
            date (str): The date input.

        Returns:
            bool: True if the date is valid, False otherwise.
        """
        pattern = r"^\d{8}$"
        return bool(re.match(pattern, date))

    def _get_valid_date(self, prompt, start_date=None, future_date=True):
        while True:
            answer = input(prompt).strip()
            if self.validate_date(answer):
                if start_date is not None:
                    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
                    end_datetime = datetime.strptime(answer, "%Y-%m-%d")
                    if end_datetime < start_datetime:
                        self.display_invalid_end_date()
                        continue
                if not future_date and not self.is_date_valid(answer):
                    self.display_invalid_date()
                return answer
            else:
                self.display_format_error()

    def is_date_valid(self, birthday):
        try:
            date = datetime.strptime(birthday, "%Y-%m-%d").date()
            return date.date() >= datetime.now().date()
        except ValueError:
            return False

    def convert(self, birthday):
        try:
            date = datetime.strptime(birthday, "%Y-%m-%d").date()
            return date.strftime("%A %d %B %Y")
        except ValueError:
            return None
