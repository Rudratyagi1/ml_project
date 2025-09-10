import sys
from src.logger import logging


def error_message_details(error):
    _, _, exc_tb = sys.exc_info()
    if exc_tb is None:  # safeguard if called outside except block
        return f"Error: {error}"

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    return f"Error occurred in script [{file_name}] at line [{line_number}] with message: {error}"

class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message)

    def __str__(self):
        return self.error_message