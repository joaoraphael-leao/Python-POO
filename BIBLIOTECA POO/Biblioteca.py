from datetime import datetime, timedelta
import pytz
from membro import Membro
from livro import Livro

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
        print(f"O livro {self.__nome_livro} foi pego no dia {self.__data_emprestimo}, estara de volta no dia {self.__data_devolucao}")

    def get_nome_livro(self):
        return self.__nome_livro

    def _get_possuidor(self):
        return self.__nome_membro

    def _get_id_possuidor(self):
        return self.__id_membro

    def get_autor(self):
        return self.__autor

    def get_status(self):
        return self.__status

    def _set_possuidor(self, possuidor):
        self.__nome_membro = possuidor
    def _set_id_possuidor(self, id_possuidor):
        self.__id_membro = id_possuidor


class Biblioteca:
    def __init__(self, nome):
        self.__nome = nome
        self.__livros_disponiveis = []
        self.__membros = []
        self.__emprestimos = []

    def adicionar_membro(self):
        nome_membro = input("Digite o nome do novo membro")
        id_membro = int(input("Digite o CPF do membro(sera usado como id)"))
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

    def remover_livro(self): #3
        self.exibir_livros_disponiveis()
        livro_removido = False
        titulo_livro = input("Qual livro voce deseja remover ? ")
        for livro in self.__livros_disponiveis:
            if(livro.get_nome() == titulo_livro):
                livro_removido = True
                self.__livros_disponiveis.remove(livro)
                print("Livro removido com sucesso!! ")

        if not livro_removido:
            print("Nao foi encontrado nenhum livro com esse nome ")

    def remover_membro(self): #4

        nome_membro = input("Digite seu nome ")
        id_membro = int(input("Digite seu cpf "))
        for membro in self.__membros:
            if membro._get_nome() == nome_membro and membro._get_id() == id_membro:
                confirmacao = input("Digite 'CONFIRMAR' para excluir sua conta ")
                if(confirmacao == "CONFIRMAR"):
                    self.__membros.remove(membro)
                    print("Cadastro excluido com sucesso!")
                else:
                    print("ERRO, tente novamente ")
                return
        print("Nenhum usuario achado com essas informacoes ")

    def editar_infos_membro(self): #5
        nome_membro = input("Digite seu nome ")
        id_membro = int(input("Digite seu cpf "))
        for membro in self.__membros:
            if membro._get_nome() == nome_membro and membro._get_id() == id_membro:
                resposta = int(input("Digite 1 se quiser mudar seu nome "))
                if resposta == 1:
                    novo_nome = input("Digite o seu novo nome ")
                    for emprestimo in self.__emprestimos:
                        if emprestimo._get_possuidor() == membro._get_nome() and emprestimo._get_id_possuidor() == membro._get_id():
                            emprestimo._set_possuidor(novo_nome)
                    membro._set_nome(novo_nome)
                resposta = int(input("Digite 1 se quiser mudar seu endereco "))
                if resposta == 1:
                    novo_endereco = input("Digite seu novo endereco ")
                    membro._set_endereco(novo_endereco)
                print("Informacoes atualizadas ")
    def editar_infos_livro(self):#6
        self.exibir_livros_disponiveis()
        nome_livro = input("Digite o nome do livro que voce deseja alterar informacoes ")
        livro_achado = False
        for livro in self.__livros_disponiveis:
            if livro.get_nome() == nome_livro:
                livro_achado = True
                resposta = int(input("Digite 1 se quiser mudar o nome do livro "))
                if resposta == 1:
                    novo_nome = input("Digite o novo nome do livro ")
                    livro._set_nome(novo_nome)
                resposta = int(input("Digite 1 se quiser mudar o autor do livro "))
                if resposta == 1:
                    novo_autor = input("Digite o nome do novo autor ")
                    livro._set_autor(novo_autor)

        if not livro_achado:
            print("Nao encontramos esse livro na nossa biblioteca!")
            self.exibir_livros_disponiveis()

    def exibir_livros_disponiveis(self):  ##7
        print("LIVROS DISPONVEIS")
        for livro in self.__livros_disponiveis:
            print(f"  - {livro}")


    def exibir_livros_emprestados(self):  ##8
        print("EMPRESTIMOS: ")
        for livro_emprestado in self.__emprestimos:
            print(f"  -{livro_emprestado.get_nome_livro()}")

    def exibir_membros_biblioteca(self): #9
        print("Membros cadastrados:")
        for membro in self.__membros:
            print(f"  -{membro}")

    def exibir_livros_reservados_por_membro(self, id_membro):  ##10
            membro_encontrado = None
            for membro in self.__membros:
                if membro._get_id() == id_membro:
                    membro_encontrado = membro
                    break

            if not membro_encontrado:
                print("Esse membro não está cadastrado.")
                return

            print(f"{membro_encontrado._get_nome()} esta na posse de:")
            tem_emprestimo = False
            for emprestimo in self.__emprestimos:
                if(membro_encontrado._get_nome() == emprestimo._get_possuidor() and membro_encontrado._get_id() == emprestimo._get_id_possuidor()):
                    tem_emprestimo = True
                    print(f"{membro_encontrado._get_nome()} esta na posse de: -{emprestimo.get_nome_livro()}")

            if not tem_emprestimo:
                print("Nenhum livro :(, alugue um dos disponiveis!!")
                self.exibir_livros_disponiveis()
    def pegar_livro_emprestado(self):# 11
        self.exibir_livros_disponiveis()
        nome_membro = input("Digite o seu nome ")
        id_membro = int(input("Digite o o seu CPF "))
        nome_livro = input("Digite o nome do livro que voce deseja reservar ")

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
            if membro._get_nome() == nome_membro and membro._get_id() == id_membro:
                membro_encontrado = membro
                break

        if not membro_encontrado:
            print("Esse membro não está cadastrado.")
            return -1
        else:
            print("Reserva feita com sucesso!")

            livro_encontrado.set_status("Alugado")

            self.__livros_disponiveis.remove(livro_encontrado)

            novo_emprestimo = Emprestimo(nome_membro, id_membro, nome_livro, autor)
            self.__emprestimos.append(novo_emprestimo)
            return
    def devolver_livro(self):  ##12
        nome_membro = input("Digite o seu nome ")
        cpf_membro = int(input("Digite o seu CPF "))
        nome_livro = input("Digite o nome do livro a devolver ")
        self.exibir_livros_reservados_por_membro(cpf_membro)
        for emprestimo in self.__emprestimos:
            if emprestimo.get_nome_livro() == nome_livro and emprestimo._get_id_possuidor() == cpf_membro and emprestimo._get_possuidor() == nome_membro:

                autor = emprestimo.get_autor()
                livro_novo = Livro(nome_livro, autor)

                self.__livros_disponiveis.append(livro_novo)
                self.__emprestimos.remove(emprestimo)

                print("Livro devolvido com sucesso!")
                return
        print("Nao encontramos nenhuma reserva com esses dados!")

    def print_donos(self):
        for emprestimo in self.__emprestimos:
            nome_possuidor = emprestimo._get_possuidor()
            nome_livro = emprestimo.get_nome_livro()

            print(f"- Nome do Membro: {nome_possuidor}. Nome do Livro: {nome_livro}")

    def exibir_datas_emprestimo_e_devolucao(self):
        for emprestimo in self.__emprestimos:
            emprestimo.print_emprestimo()
