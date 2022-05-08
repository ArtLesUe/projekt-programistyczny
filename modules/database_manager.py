import os

from modules.nlp_manager import learn_polish_language_from_seed
from modules.nlp_manager import load_learned_data_about_polish_language


POLISH_DICTIONARY_DB_PATH: str = 'database/polish-database.json'


def init_database() -> None:
    """
    Tworzy puste bazy danych przeznaczone do wyuczonych danych.

    :return: None
    """
    if not os.path.exists('database/spam-database.json'):
        with open('database/spam-database.json', 'w') as f:
            f.writelines('[]')

    if not os.path.exists('database/questions-database.json'):
        with open('database/questions-database.json', 'w') as f:
            f.writelines('[]')

    if not os.path.exists(POLISH_DICTIONARY_DB_PATH):
        learn_polish_language_from_seed()
    else:
        load_learned_data_about_polish_language()
