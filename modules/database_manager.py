import os


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
