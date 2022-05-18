class PolishLearnedData:
    """
    Klasa posiadająca dane nauki na temat języka polskiego oraz wykonująca na nich operacje.
    """
    def __init__(self, initial_data: list) -> None:
        """
        Klasa posiadająca dane nauki na temat języka polskiego oraz wykonująca na nich operacje.

        :param list initial_data: lista z danymi wyuczonymi na temat polskich słów
        :return: None
        """
        self.__learned_data: list = initial_data

    def is_polish_word(self, word: str) -> bool:
        """
        Sprawdza, czy podane słowo jest polskim wyrazem.

        :param str word: słowo, które sprawdzamy, czy jest polskim wyrazem
        :return: bool — wartość logiczna czy słowo jest polskim wyrazem
        """
        if self.__learned_data.count(word) > 0:
            return True
        else:
            return False
