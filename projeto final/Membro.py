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

    def reservar_livros(self, livro):
        self.__livros_emprestados.append(livro)

    def get_livros_emprestados(self):
        return self.__livros_emprestados


class Livro:
    def __init__(self, nome, autor):
        self.__nome = nome
        self.__autor = autor
        self.__status = "Disponivel"
        self.__quem_possui = "Ainda nao esta com ninguem"

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

    def set_quem_possui(self, nova_posse):
        self.__quem_possui = nova_posse

    def get_quem_possui(self):
        return self.__quem_possui

    def __str__(self):
        return f"{self.__nome}"


class Biblioteca:
    def __init__(self, nome):
        self.__nome = nome
        self.__livros_disponiveis = []
        self.__livros_emprestados = []
        self.__membros = []

    def adicionar_membro(self):
        nome_membro = input("Digite o nome do novo membro")
        id_membro = input("Digite o CPF do membro(sera usado como id)")
        endereco = input("Digite o endereco do membro")
        novo_membro = Membro(nome_membro, id_membro, endereco)
        self.__membros.append(novo_membro)



    def pegar_livro_emprestado(self, nome_livro, nome_membro):
        livro_encontrado = None
        for livro in self.__livros_disponiveis:
            if livro.get_nome() == nome_livro:
                livro_encontrado = livro
                break

        if not livro_encontrado:
            print("Esse livro não está disponível.")
            return -1

        membro_encontrado = None
        for membro in self.__membros:
            if membro.get_nome() == nome_membro:
                membro_encontrado = membro
                break

        if not membro_encontrado:
            print("Esse membro não está cadastrado.")
            return -1
        else:
            submit_id = input(f"Digite seu id, {membro_encontrado.get_nome()}")

            if submit_id == membro_encontrado.get_id():
                print("Reserva feita com sucesso!")
        livro_encontrado.set_status("Alugado")
        livro_encontrado.set_quem_possui(nome_membro)
        self.__livros_disponiveis.remove(livro_encontrado)
        self.__livros_emprestados.append(livro_encontrado)
        membro_encontrado.reservar_livros(livro_encontrado)

    def exibir_livros_disponiveis(self):
        print("LIVROS DISPONVEIS")
        for livro in self.__livros_disponiveis:
            print(f"  - {livro}")

    def adicionar_livro(self):
        titulo = input("Digite o titulo do livro ")
        autor = input("Digite o nome do autor do livro ")

        novo_livro = Livro(titulo, autor)
        self.__livros_disponiveis.append(novo_livro)

        print()
        print("Novo livro adicionado com sucesso!!")
        print()

        self.exibir_livros_disponiveis()
        print()

    def exibir_livros_reservados_por_membro(self, cpf_membro):
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

teste = Biblioteca("biblioteca do rapha")
while 1:
    input("""Opcoes:
                (1) Cadastrar um novo membro na biblioteca
                (2) Cadastrar um novo livro na biblioteca
                (3) Remover um livro da biblioteca
                (4) Remover um membro da biblioteca
                (5) Editar endereco e nome de membro da biblioteca
                (6) Editar nome do livro ou autor do livro (nao faz muito sentido mas ta ai)
                (7) Exibir livros disponiveis para reserva
                (8) Exibir livros ja reservados
                (9) Exibir os membros da biblioteca
                (10) Exibir livros reservados por um membro
                (11) Pegar um livro emprestado
                (12) Devolver um ou todos os livros que voce pegou emprestado
            """)
    break

#teste.adicionar_livro()
#teste.adicionar_livro()
#teste.adicionar_membro()
#teste.pegar_livro_emprestado("Harry Potter", "Rapha")
#teste.exibir_livros_reservados_por_membro("Rapha")
