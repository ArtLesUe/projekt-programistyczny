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
