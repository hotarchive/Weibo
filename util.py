import logging
import os
from datetime import datetime

logging.basicConfig(
    format='%(asctime)s %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)


def strip_embracing_quotes(text: str):
    if text.startswith('"') and text.endswith('"'):
        return text[1:-1]
    return text


def current_time():
    return datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %z')


def current_date():
    return datetime.now().astimezone().strftime('%Y-%m-%d')


def current_date_year():
    return datetime.now().astimezone().strftime('%Y')


def current_date_month():
    return datetime.now().astimezone().strftime('%m')


def current_date_day():
    return datetime.now().astimezone().strftime('%d')


def ensure_dir(file: str):
    directory = os.path.abspath(os.path.dirname(file))
    if not os.path.exists(directory):
        os.makedirs(directory)


def write_text(file: str, text: str):
    ensure_dir(file)
    with open(file, 'w') as f:
        f.write(text)


if __name__ == "__main__":
    logger.info('hello world')
