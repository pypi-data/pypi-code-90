import logging
from datetime import datetime

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%SZ'
DATETIME_REGEX = r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}Z'


def convert_datetime_to_str(date: datetime, datetime_format=DATETIME_FORMAT) -> str:
    try:
        return date.strftime(datetime_format)
    except Exception:
        logging.exception('failed convert datetime {} to str'.format(date))
        return None


def convert_str_to_datetime(date: str, datetime_format=DATETIME_FORMAT) -> datetime:
    try:
        return datetime.strptime(date, datetime_format)
    except Exception:
        logging.exception('failed convert str {} to datetime'.format(date))
        return None


def log_execution_time(function):
    def wrapper(*args, **attributes):
        start_time = datetime.now()
        result = function(*args, **attributes)
        end_time = datetime.now()
        logging.info(f'execution duration of {function.__name__} was {end_time - start_time} seconds')
        return result

    return wrapper
