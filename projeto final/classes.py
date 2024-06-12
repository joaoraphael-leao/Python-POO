from datetime import datetime, timedelta
import pytz


class Membro:
    def __init__(self, nome, id_membro, endereco):
        self.__nome = nome
        self.__id_membro = id_membro
        self.__endereco = endereco
        self.__livros_emprestados = []

    def get_id(self):
        return self.__id_membro

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def _get_endereco(self):
        return self.__endereco

    def _set_endereco(self, endereco):
        self.__endereco = endereco


class Emprestimo:

    def __init__(self, nome_membro, id_membro, nome_livro, autor):
        brasilia_fuso = pytz.timezone('America/Sao_Paulo')
        self.__nome_membro = nome_membro
        self.__id_membro = id_membro
        self.__nome_livro = nome_livro
        self.__status = "Emprestado"
        self.__autor = autor
        self.__data_emprestimo = datetime.now(brasilia_fuso)
        self.__data_devolucao = self.__data_emprestimo + timedelta(days=7)

    def __str__(self):
        return f"O livro {self.__nome_livro} esta emprestado ao membro(a) {self.__nome_membro} ate o dia {self.__data_devolucao}"

    def print_emprestimo(self):
        print(
            f"O livro {self.__nome_livro} foi pego no dia {self.__data_emprestimo}, estara de volta no dia {self.__data_devolucao}")

    def get_nome_livro(self):
        return self.__nome_livro

    def get_possuidor(self):
        return self.__nome_membro

    def get_id_possuidor(self):
        return self.__id_membro

    def get_autor(self):
        return self.__autor

    def get_status(self):
        return self.__status


class Livro:
    def __init__(self, nome, autor):
        self.__nome = nome
        self.__autor = autor
        self.__status = "Disponivel"

    def __set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def __set_autor(self, autor):
        self.__autor = autor

    def get_autor(self):
        return self.__autor

    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status

    def __str__(self):
        return f"{self.__nome}"


class Biblioteca:
    def __init__(self, nome):
        self.__nome = nome
        self.__livros_disponiveis = []
        self.__membros = []
        self.__emprestimos = []

    def adicionar_membro(self):  #1
        nome_membro = input("Digite o nome do novo membro")
        id_membro = input("Digite o CPF do membro(sera usado como id)")
        endereco = input("Digite o endereco do membro")
        novo_membro = Membro(nome_membro, id_membro, endereco)
        self.__membros.append(novo_membro)

    def adicionar_livro(self):  #2
        titulo = input("Digite o titulo do livro ")
        autor = input("Digite o nome do autor do livro ")

        novo_livro = Livro(titulo, autor)
        self.__livros_disponiveis.append(novo_livro)

        print()
        print("Novo livro adicionado com sucesso!!")
        print()

        self.exibir_livros_disponiveis()
        print()

    def exibir_livros_disponiveis(self):  ##7
        print("LIVROS DISPONVEIS")
        for livro in self.__livros_disponiveis:
            print(f"  - {livro}")

    def exibir_livros_emprestados(self):  ##8
        print("EMPRESTIMOS: ")
        for livro_emprestado in self.__emprestimos:
            print(f"  -{livro_emprestado.get_nome_livro}")

    def exibir_livros_reservados_por_membro(self, cpf_membro):  ##10
        membro_encontrado = None
        for membro in self.__membros:
            if membro.get_id() == cpf_membro:
                membro_encontrado = membro
                break

        if not membro_encontrado:
            print("Esse membro não está cadastrado.")
            return

        livros_emprestados = membro_encontrado.get_livros_emprestados()
        nome_membro = membro_encontrado.get_nome()
        if livros_emprestados:
            print(f"Livros reservados por {nome_membro}:")
            for livro in livros_emprestados:
                print(f"  - {livro}")
        else:
            print(f"{nome_membro} não reservou nenhum livro.")

    def pegar_livro_emprestado(self, nome_livro, nome_membro):  # 11
        livro_encontrado = None
        for livro in self.__livros_disponiveis:
            if livro.get_nome() == nome_livro:
                livro_encontrado = livro
                break

        if not livro_encontrado:
            for livro_encontrado in self.__emprestimos:
                if livro_encontrado.get_nome_livro() == nome_livro:
                    print("Esse livro já foi reservado, veja abaixo os detalhes da reserva")
                    livro_encontrado.print_emprestimo()
            return -1

        autor = livro_encontrado.get_autor()
        membro_encontrado = None

        for membro in self.__membros:
            if membro.get_nome() == nome_membro:
                membro_encontrado = membro
                break

        if not membro_encontrado:
            print("Esse membro não está cadastrado.")
            return -1
        else:
            id_membro = membro_encontrado.get_id()
            submit_id = input(f"Digite seu id, {membro_encontrado.get_nome()}")

            if submit_id == id_membro:
                print("Reserva feita com sucesso!")

        livro_encontrado.set_status("Alugado")

        self.__livros_disponiveis.remove(livro_encontrado)

        novo_emprestimo = Emprestimo(nome_membro, id_membro, nome_livro, autor)
        self.__emprestimos.append(novo_emprestimo)
        membro_encontrado.reservar_livros(livro_encontrado)

    def devolver_livro(self, nome_livro):  ##12
        for emprestimo in self.__emprestimos:
            if emprestimo.get_nome_livro() == nome_livro:
                nome_usuario = emprestimo.get_possuidor()
                tentativa_id = input(
                    f"Ola, {nome_usuario}, para devolver o livro {nome_livro}, por favor digite seu ID ")

                if tentativa_id != emprestimo.get_id_possuidor():
                    print("ERRO: Digite seu id corretamente")
                    return -1
                autor = emprestimo.get_autor()
                livro_novo = Livro(nome_livro, autor)

                self.__livros_disponiveis.append(livro_novo)
                self.__emprestimos.remove(emprestimo)

                print("Livro removido com sucesso!")
                return
