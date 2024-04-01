from datetime import datetime
from .views import BaseView
import re


class BaseDate(BaseView):
    date_validator = None

    def display_format_error(self):
        print("Invalid date format. Please use YYYY.MM.DD format.")

    def display_invalid_date(self):
        print("Invalid date. Please enter a date not earlier than today.")

    def display_invalid_end_date(self):
        print("Invalid date. End date should not be earlier than start date.")

    def _get_valid_date(self, prompt, start_date=None, future_date=True):
        while True:
            answer = input(prompt).strip()
            if self.validate_date(answer):
                if start_date is not None:
                    start_datetime = datetime.strptime(start_date, "%Y.%m.%d")
                    end_datetime = datetime.strptime(answer, "%Y.%m.%d")
                    if end_datetime < start_datetime:
                        self.display_invalid_end_date()
                        continue
                if not future_date and not self.is_date_valid(answer):
                    self.display_invalid_date()
                return answer
            else:
                self.display_format_error()

    def validate_date(self, date):
        """
        Validate a date input.

        Args:
            date (str): The date input.

        Returns:
            bool: True if the date is valid, False otherwise.
        """
        pattern = r"^\d{4}\.\d{2}\.\d{2}$"
        return bool(re.match(pattern, date))

    def is_date_valid(self, date):
        try:
            date = datetime.strptime(date, "%Y.%m.%d").date()
            return date >= datetime.now().date()
        except ValueError:
            return False

    def convert(self, date):
        try:
            return datetime.strptime(date, "%Y.%m.%d").date()
        except ValueError:
            return None
