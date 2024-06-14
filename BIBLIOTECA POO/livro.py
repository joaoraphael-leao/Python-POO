class Livro:
    def __init__(self, nome, autor):
        self.__nome = nome
        self.__autor = autor
        self.__status = "Disponivel"

    def _set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def _set_autor(self, autor):
        self.__autor = autor

    def get_autor(self):
        return self.__autor

    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status

    def __str__(self):
        return f"{self.__nome}"
