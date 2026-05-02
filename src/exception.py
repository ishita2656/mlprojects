import sys
import logging
from src.logger import logging


def error_message_detail(error, error_detail: sys) -> str:
    _, _, exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    line_number = exec_tb.tb_lineno

    error_message = "Error occurred in Python script name [{0}] at line number [{1}] error message [{2}]".format(
        file_name, line_number, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":
    try:
        try:
            a = 1/0
        except Exception as e:
            logging.info("Division by zero error occurred.")
            raise CustomException(e, sys)
    except CustomException as ce:
        logging.error(ce)

    