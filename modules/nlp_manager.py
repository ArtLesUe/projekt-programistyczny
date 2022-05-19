import json

from typing import IO

from classes.polish_learned_data import PolishLearnedData
from classes.spam_learned_data import SpamLearnedData
from classes.questions_learned_data import QuestionsLearnedData


POLISH_DICTIONARY_DB_PATH: str = 'database/polish-database.json'
"""Ścieżka do pliku bazy danych z wyuczonymi danymi na temat polskich słów."""
SEED_POLISH_DICTIONARY_PATH: str = 'seed/learn-polish-language.txt'
"""Ścieżka do pliku słownika języka polskiego, który będzie uczył o polskich słowach."""
SPAM_LEARN_DATA_DB_PATH: str = 'database/spam-database.json'
"""Ścieżka do pliku bazy danych z wyuczonymi danymi na temat spamu i nie spamu."""
SEED_SPAM_LEARN_DATA_PATH: str = 'seed/learn-data-spam.json'
"""Ścieżka do pliku nauki na temat tego, co jest spamem, a co nie jest spamem."""
QUESTIONS_LEARN_DATA_DB_PATH: str = "database/questions-database.json"
"""Ścieżka do pliku bazy danych z wyuczonymi danymi na temat pytań i odpowiedzi."""
SEED_QUESTIONS_LEARN_DATA_DB_PATH: str = "seed/learn-data-questions.json"
"""Ścieżka do pliku nauki na temat pytań i odpowiedzi na nie."""

polish_learned_data: PolishLearnedData = PolishLearnedData([])
"""Zmienna zawierająca obiekt z wyuczonymi danymi na temat polskich słów."""
spam_learned_data: SpamLearnedData = SpamLearnedData({})
"""Zmienna zawierająca obiekt z wyuczonymi danymi na temat spamu i nie spamu."""
questions_learned_data: QuestionsLearnedData = QuestionsLearnedData({})
"""Zmienna zawierająca obiekt z wyuczonymi danymi na temat pytań i odpowiedzi."""


def learn_spam_new_data(text_data: str, is_spam: bool) -> None:
    """
    Uczy model nowych danych, które są spamem lub nie są spamem.

    :param str text_data: dane tekstowe, które będą analizowane.
    :param bool is_spam: wartość logiczna czy tekst jest spamem.
    :return: None
    """
    global polish_learned_data
    global spam_learned_data

    if is_spam:
        spam_learned_data.learn_spam(text_data, polish_learned_data)
    else:
        spam_learned_data.learn_no_spam(text_data, polish_learned_data)

    words_json: str = json.dumps(spam_learned_data.dump_database())

    with open(SPAM_LEARN_DATA_DB_PATH, 'w') as f:
        f.writelines(words_json)


def load_learned_questions_data_from_database() -> None:
    """
    Funkcja wczytuje do pamięci wyuczone dane o pytaniach i odpowiedziach.

    :return: None
    """
    questions_learned: IO = open(QUESTIONS_LEARN_DATA_DB_PATH, 'r')
    questions_learned_json: str = ' '.join(questions_learned.readlines())
    questions_learned.close()
    questions_learned_list: dict = json.loads(questions_learned_json)
    global questions_learned_data
    questions_learned_data = SpamLearnedData(questions_learned_list)
    dump_database: dict = questions_learned_data.dump_database()
    print('[LEARN] Wczytano dane nauki dla następującej ilości pytań i odpowiedzi: ' +
          str(len(dump_database['words'])) + " / " +
          str(len(dump_database['answers'])))


def learn_questions_data_from_seed() -> None:
    """
    Funkcja wczytuje dane uczące i przetwarza je w celu nauki algorytmu pytań i odpowiedzi.

    :return: None
    """
    print("\n[LEARN] Uczenie się informacji o pytaniach i odpowiedziach na podstawie pliku nauki...")

    seed_file: IO = open(SEED_QUESTIONS_LEARN_DATA_DB_PATH, 'r')
    questions_data_json: str = ' '.join(seed_file.readlines())
    seed_file.close()
    questions_data: dict = json.loads(questions_data_json)
    global questions_learned_data

    for question in questions_data:
        questions_learned_data.learn(question['question'], question['answer'], polish_learned_data)

    print('[LEARN] Zapisywanie efektów nauki do bazy danych...')

    questions_json: str = json.dumps(questions_learned_data.dump_database())

    with open(QUESTIONS_LEARN_DATA_DB_PATH, 'w') as f:
        f.writelines(questions_json)

    print('[LEARN] Zapisano wyniki uczenia do pliku bazy danych...')


def load_learned_spam_data_from_database() -> None:
    """
    Funkcja wczytuje do pamięci wyuczone dane o spamie.

    :return: None
    """
    spam_learned: IO = open(SPAM_LEARN_DATA_DB_PATH, 'r')
    spam_learned_json: str = ' '.join(spam_learned.readlines())
    spam_learned.close()
    spam_learned_list: dict = json.loads(spam_learned_json)
    global spam_learned_data
    spam_learned_data = SpamLearnedData(spam_learned_list)
    print('[LEARN] Wczytano dane nauki dla następującej ilości słów spamowych: ' +
          str(len(spam_learned_data.dump_database())))


def learn_spam_data_from_seed() -> None:
    """
    Wczytuje dane uczące i rozpoczyna ich przetwarzanie w celu nauki algorytmu.

    :return: None
    """
    print("\n[LEARN] Uczenie się informacji o spamie na podstawie pliku nauki...")

    seed_file: IO = open(SEED_SPAM_LEARN_DATA_PATH, 'r')
    spam_data_json: str = ' '.join(seed_file.readlines())
    seed_file.close()
    spam_data: dict = json.loads(spam_data_json)
    text_spam_data: list = spam_data['spam']
    text_no_spam_data: list = spam_data['nie-spam']
    global spam_learned_data

    for learn_text in text_spam_data:
        spam_learned_data.learn_spam(learn_text, polish_learned_data)

    for learn_text in text_no_spam_data:
        spam_learned_data.learn_no_spam(learn_text, polish_learned_data)

    print('[LEARN] Zapisywanie efektów nauki do bazy danych...')

    words_json: str = json.dumps(spam_learned_data.dump_database())

    with open(SPAM_LEARN_DATA_DB_PATH, 'w') as f:
        f.writelines(words_json)

    print('[LEARN] Zapisano wyniki uczenia do pliku bazy danych...')


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
    global polish_learned_data
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

    polish_learned_data = PolishLearnedData(polish_words_list)

    print("[LEARN] Nauczono się następującej liczby polskich słów: " + str(len(polish_words_list)))
