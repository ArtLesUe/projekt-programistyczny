import json

from typing import IO

from classes.polish_learned_data import PolishLearnedData


POLISH_DICTIONARY_DB_PATH: str = 'database/polish-database.json'
"""Ścieżka do pliku bazy danych z wyuczonymi danymi na temat polskich słów."""
SEED_POLISH_DICTIONARY_PATH: str = 'seed/learn-polish-language.txt'
"""Ścieżka do pliku słownika języka polskiego, który będzie uczył o polskich słowach."""

polish_learned_data: PolishLearnedData = PolishLearnedData([])
"""Zmienna zawierająca obiekt z wyuczonymi danymi na temat polskich słów."""


def load_learned_data_about_polish_language() -> None:
    """
    Wczytuje już nauczone dane na temat języka polskiego do pamięci aplikacji.

    :return: None
    """
    polish_learned: IO = open(POLISH_DICTIONARY_DB_PATH, 'r')
    polish_learned_json: str = ' '.join(polish_learned.readlines())
    polish_learned.close()
    polish_learned_list: list = json.loads(polish_learned_json)
    global polish_learned_data
    polish_learned_data = PolishLearnedData(polish_learned_list)
    print('[LEARN] Wczytano dane nauki dla następującej ilości polskich słów: ' + str(len(polish_learned_list)))


def learn_polish_language_from_seed() -> None:
    """
    Tworzy bazę danych polskich wyrazów na podstawie pliku nauki.

    :return: None
    """
    print("\n[LEARN] Uczenie się języka polskiego na podstawie słownika języka polskiego...")
    dictionary_file: IO = open(SEED_POLISH_DICTIONARY_PATH, 'r')
    polish_words = dictionary_file.readlines()
    dictionary_file.close()

    polish_words_list: list = []
    i: int = 0

    for word in polish_words:
        new_word: str = word.replace("\n", "").replace("\r", "")
        polish_words_list.append(new_word)
        i = i + 1
        if i % 100000 == 0 or i == len(polish_words):
            print('[LEARN] Trwa uczenie się języka polskiego ze słownika: ' + str(i) + ' / ' + str(len(polish_words)))

    print('[LEARN] Zapisywanie efektów nauki do bazy danych...')

    polish_words_json: str = json.dumps(polish_words_list)

    with open(POLISH_DICTIONARY_DB_PATH, 'w') as f:
        f.writelines(polish_words_json)

    print("[LEARN] Nauczono się następującej liczby polskich słów: " + str(len(polish_words_list)))
