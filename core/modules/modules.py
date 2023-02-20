import json
from configparser import ConfigParser
import logging
from datetime import datetime


def read_config(key: str, value: str) -> str:
    config = ConfigParser()
    config.read(r'C:\Users\evgenyp\PycharmProjects\FlightComputer\core\data\config.ini')
    return config.get(key, value)


def read_json(key: str, value: str) -> dict:
    path = read_config(key, value)
    with open(path, 'r', encoding='utf-8') as json_file:
        file = json.load(json_file)
        return file


def log(text: str, level=logging.DEBUG) -> None:

    time = datetime.now()
    time_format = f'{time: %A | %d/%m/%Y | %X}'
    path = read_config('path', 'logs')
    logging.basicConfig(filename=path,
                        format=f'%(levelname)s: {time_format} :: %(message)s',
                        level=level)

    match level:

        case logging.INFO:
            logging.info(text)

        case logging.DEBUG:
            logging.debug(text)

        case logging.ERROR:
            logging.error(text)

        case logging.CRITICAL:
            logging.critical(text)

        case logging.FATAL:
            logging.fatal(text)

        case _:
            raise Exception("wrong log level input")
