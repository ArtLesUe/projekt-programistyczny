from classes.polish_learned_data import PolishLearnedData


class SpamLearnedData:
    """
    Klasa posiadająca wyuczone informacje na temat co jest spamem, a co nie jest spamem.
    """
    def __init__(self, initial_data: dict) -> None:
        """
        Klasa posiadająca wyuczone informacje na temat co jest spamem, a co nie jest spamem.

        :param list initial_data: lista z wyuczonymi danymi na temat spamu
        :return: None
        """
        self.__learned_data: dict = initial_data

    def dump_database(self) -> dict:
        """
        Zrzuca nauczone dane do zmiennej.

        :return: dict - słownik zawierający dane nauki.
        """
        return self.__learned_data

    def process_text(self, text: str, is_spam: bool, dictionary: PolishLearnedData) -> None:
        """
        Przetwarza zadany tekst i traktuje go jako spam lub nie spam.

        :param str text: tekst do przetworzenia przez nauczanie
        :param bool is_spam: flaga czy podany tekst jest spamem, czy nie
        :param PolishLearnedData dictionary: słownik języka polskiego
        :return: None
        """
        text = "".join([ch for ch in text if ch.isalpha() or ch == " "])
        word_table: list = text.lower().split(" ")

        for word in word_table:
            if len(word) >= 4:
                if self.__learned_data.get(word) is None:
                    if dictionary.is_polish_word(word):
                        self.__learned_data[word] = {"spam": 0, "nie-spam": 0}
                    else:
                        continue
                if is_spam:
                    self.__learned_data[word]["spam"] += 1
                else:
                    self.__learned_data[word]["nie-spam"] += 1

    def learn_spam(self, text: str, dictionary: PolishLearnedData) -> None:
        """
        Naucz nowe informacje na temat tekstu będącego spamem.

        :param str text: tekst, który będzie traktowany jako spam i posłuży do uczenia
        :param PolishLearnedData dictionary: słownik języka polskiego
        :return: None
        """
        self.process_text(text, True, dictionary)
        print('[LEARN] nauczono się nowych wyrazów, rozmiar słownika spam/nie-spam: ' + str(len(self.__learned_data)))

    def learn_no_spam(self, text: str, dictionary: PolishLearnedData) -> None:
        """
        Naucz nowe informacje na temat tekstu niebędącego spamem.

        :param str text: tekst, który będzie traktowany jako dobry tekst i posłuży do uczenia
        :param PolishLearnedData dictionary: słownik języka polskiego
        :return: None
        """
        self.process_text(text, False, dictionary)
        print('[LEARN] nauczono się nowych wyrazów, rozmiar słownika spam/nie-spam: ' + str(len(self.__learned_data)))
