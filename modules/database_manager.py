import os

from modules.nlp_manager import learn_polish_language_from_seed
from modules.nlp_manager import load_learned_data_about_polish_language
from modules.nlp_manager import learn_spam_data_from_seed
from modules.nlp_manager import load_learned_spam_data_from_database


POLISH_DICTIONARY_DB_PATH: str = 'database/polish-database.json'
"""Ścieżka do pliku bazy danych z wyuczonymi danymi na temat polskich słów."""
SPAM_LEARN_DATA_DB_PATH: str = 'database/spam-database.json'
"""Ścieżka do pliku bazy danych z wyuczonymi danymi na temat spamu i nie spamu."""


def init_database() -> None:
    """
    Tworzy puste bazy danych przeznaczone do wyuczonych danych.

    :return: None
    """
    if not os.path.exists(POLISH_DICTIONARY_DB_PATH):
        learn_polish_language_from_seed()
    else:
        load_learned_data_about_polish_language()

    if not os.path.exists(SPAM_LEARN_DATA_DB_PATH):
        learn_spam_data_from_seed()
    else:
        load_learned_spam_data_from_database()

    if not os.path.exists('database/questions-database.json'):
        with open('database/questions-database.json', 'w') as f:
            f.writelines('[]')
