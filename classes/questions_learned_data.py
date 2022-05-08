class QuestionsLearnedData:
    """
    Klasa posiadająca wyuczone dane na temat pytań i odpowiedzi dla chat bota.
    """
    def __init__(self, initial_data: list) -> None:
        """
        Klasa posiadająca wyuczone dane na temat pytań i odpowiedzi dla chat bota.

        :param list initial_data: lista z wyuczonymi danymi na temat pytań i odpowiedzi
        :return: None
        """
        self.__learned_data: list = initial_data
