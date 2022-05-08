class SpamLearnedData:
    """
    Klasa posiadająca wyuczone informacje na temat co jest spamem, a co nie jest spamem.
    """
    def __init__(self, initial_data: list) -> None:
        """
        Klasa posiadająca wyuczone informacje na temat co jest spamem, a co nie jest spamem.

        :param list initial_data: lista z wyuczonymi danymi na temat spamu
        :return: None
        """
        self.__learned_data: list = initial_data

    def learn_spam(self, text: str) -> None:
        """
        Naucz nowe informacje na temat tekstu będącego spamem.

        :param str text: tekst, który będzie traktowany jako spam i posłuży do uczenia
        :return: None
        """

    def learn_no_spam(self, text: str) -> None:
        """
        Naucz nowe informacje na temat tekstu niebędącego spamem.

        :param str text: tekst, który będzie traktowany jako dobry tekst i posłuży do uczenia
        :return: None
        """
