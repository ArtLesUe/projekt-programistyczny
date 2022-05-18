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
