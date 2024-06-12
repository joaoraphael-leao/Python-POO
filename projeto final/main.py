from classes import Biblioteca, Membro, Livro

teste = Biblioteca("biblioteca do rapha")
while 1:
    opcao = input("""Opcoes:
                (-1) SAIR
                (1) Cadastrar um novo membro na biblioteca #check
                (2) Cadastrar um novo livro na biblioteca #check
                (3) Remover um livro da biblioteca 
                (4) Remover um membro da biblioteca
                (5) Editar endereco e nome de membro da biblioteca
                (6) Editar nome do livro
                (7) Exibir livros disponiveis para reserva #check
                (8) Exibir livros ja reservados #check
                (9) Exibir os membros da biblioteca 
                (10) Exibir livros reservados por um membro #check 
                (11) Pegar um livro emprestado #check
                (12) Devolver um ou todos os livros que voce pegou emprestado #check
                (13) Exibir quem possui cada livro
                (14) Exibir data de emprestimo e devolucao dos livros #check 
            """)

    if opcao == '0':
        break
    elif opcao == '1':
        teste.adicionar_membro()
    elif opcao == '2':
        teste.adicionar_livro()
    elif opcao == '3':
        # Coloque aqui a lógica para remover um livro da biblioteca
        pass
    elif opcao == '4':
        # Coloque aqui a lógica para remover um membro da biblioteca
        pass
    elif opcao == '5':
        # Coloque aqui a lógica para editar endereço e nome de membro da biblioteca
        pass
    elif opcao == '6':
        # Coloque aqui a lógica para editar nome do livro
        pass
    elif opcao == '7':
        teste.exibir_livros_disponiveis()
    elif opcao == '8':
        teste.exibir_livros_emprestados()
    elif opcao == '9':
        # Coloque aqui a lógica para exibir os membros da biblioteca
        pass
    elif opcao == '10':
        cpf_membro = input("Digite o CPF do membro: ")
        teste.exibir_livros_reservados_por_membro(cpf_membro)
    elif opcao == '11':
        nome_livro = input("Digite o nome do livro: ")
        nome_membro = input("Digite o nome do membro: ")
        teste.pegar_livro_emprestado(nome_livro, nome_membro)
    elif opcao == '12':
        nome_livro = input("Digite o nome do livro a devolver: ")
        teste.devolver_livro(nome_livro)
    elif opcao == '13':
        # Coloque aqui a lógica para exibir quem possui cada livro
        pass
    elif opcao == '14':
        # Coloque aqui a lógica para exibir data de empréstimo e devolução dos livros
        pass
    else:
        print("Opção inválida! Tente novamente.")

    break