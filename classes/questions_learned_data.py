import hashlib

from classes.polish_learned_data import PolishLearnedData


class QuestionsLearnedData:
    """
    Klasa posiadająca wyuczone dane na temat pytań i odpowiedzi dla chat bota.
    """
    def __init__(self, initial_data: dict) -> None:
        """
        Klasa posiadająca wyuczone dane na temat pytań i odpowiedzi dla chat bota.

        :param dict initial_data: lista z wyuczonymi danymi na temat pytań i odpowiedzi
        :return: None
        """
        self.__learned_data: dict = initial_data

    def dump_database(self) -> dict:
        """
        Zrzuca nauczone dane do zmiennej.

        :return: dict - słownik zawierający dane nauki.
        """
        return self.__learned_data

    def get_answer(self, question: str) -> dict:
        """
        Wprowadza pytanie do modelu i uzyskuje odpowiedź na podstawie wyuczonych danych.

        :param str question: pytanie, które zostanie przekazane do modelu.
        :return: dict - słownik zawierający odpowiedź i jej punktację
        """
        text = "".join([ch for ch in question if ch.isalpha() or ch == " "])
        word_table: list = text.lower().split(" ")

        contest: dict = {}

        for word in word_table:
            if len(word) >= 4:
                if self.__learned_data['words'].get(word) is not None:
                    for answer in self.__learned_data["words"][word]:
                        if contest.get(answer) is None:
                            contest[answer] = 0
                        contest[answer] += self.__learned_data["words"][word][answer]

        if len(contest) == 0:
            print('[ASK] szacuję odpowiedź na pytanie na: brak odpowiedzi')

            return {
                'answer': 'Nie wiem o co ci chodzi, napisz to inaczej.',
                'probability': 0,
                'answerId': 0
            }

        max_points: int = 0
        max_answer: str = ""
        max_id: str = ""

        for item in contest:
            if contest[item] > max_points:
                max_points = contest[item]
                max_answer = self.__learned_data["answers"][item]
                max_id = item

        print('[ASK] szacuję odpowiedź na pytanie na: ' + str({
            'answer': max_answer,
            'probability': str(max_points),
            'answerId': max_id
        }))

        return {
            'answer': max_answer,
            'probability': str(max_points),
            'answerId': max_id
        }

    def learn(self, question: str, answer: str, dictionary: PolishLearnedData) -> None:
        """
        Funkcja ucząca algorytm nowych pytań i odpowiedzi.

        :param str question: pytanie, na jakie uczymy bota odpowiadać.
        :param str answer: odpowiedź na postawione pytanie.
        :param PolishLearnedData dictionary: słownik języka polskiego
        :return: None
        """
        if self.__learned_data.get('answers') is None:
            self.__learned_data['answers'] = {}

        if self.__learned_data.get('words') is None:
            self.__learned_data['words'] = {}

        text: str = "".join([ch for ch in answer if ch.isalpha() or ch == " "])
        answer_uuid: str = hashlib.md5(text.lower().encode()).hexdigest()
        self.__learned_data['answers'][answer_uuid] = answer

        text = "".join([ch for ch in question if ch.isalpha() or ch == " "])
        word_table: list = text.lower().split(" ")

        for word in word_table:
            if len(word) >= 4:
                if self.__learned_data['words'].get(word) is None:
                    if dictionary.is_polish_word(word):
                        self.__learned_data['words'][word] = {}
                    else:
                        continue

                if self.__learned_data["words"][word].get(answer_uuid) is None:
                    self.__learned_data["words"][word][answer_uuid] = 1
                else:
                    self.__learned_data["words"][word][answer_uuid] += 1

        print("[LEARN] nauczyłem się tylu słów kluczowych i odpowiedzi na nie: " +
            str(len(self.__learned_data['words'])) + " / " + str(len(self.__learned_data['answers'])))
