class Membro:
    def __init__(self, nome, id_membro, endereco):
        self.__nome = nome
        self.__id_membro = id_membro
        self.__endereco = endereco
        self.__livros_emprestados = []

    def __str__(self):
        return f"Nome do Usuario: {self._get_nome()}, ID Usuario: {self._get_id()}"

    def _get_id(self):
        return self.__id_membro

    def _get_nome(self):
        return self.__nome

    def _set_nome(self, nome):
        self.__nome = nome

    def _get_endereco(self):
        return self.__endereco

    def _set_endereco(self, endereco):
        self.__endereco = endereco

    def _get_livros_emprestados(self):
        return self.__livros_emprestados