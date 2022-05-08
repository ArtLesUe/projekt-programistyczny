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
