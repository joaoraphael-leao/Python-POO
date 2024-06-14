from Biblioteca import Biblioteca

teste = Biblioteca("biblioteca do rapha")
while 1:
    opcao = input(
"""                 MENU
                    (-1) SAIR
                    (1) Cadastro de novos objetos (Membro ou Livro)
                    (2) Remocoes e edicoes de objetos
                    (3) Exibicoes
                    (4) Acoes
                    Digite aqui a opção desejada: """)

    if opcao == '1':
        escolha_final = input(
"""             MENU
                (-1) SAIR
                (1) Cadastrar um novo membro na biblioteca 
                (2) Cadastrar um novo livro na biblioteca 
                (3)Voltar para o Menu Principal
                Digite aqui a opção desejada: """)

        if escolha_final == '1':
            teste.adicionar_membro()
        elif escolha_final == '2':
            teste.adicionar_livro()
        elif escolha_final == '3':
            continue
        elif escolha_final == '-1':
            break
        else:
            print("Opcao Invalida")

    elif opcao == '2':
        escolha_final = input(
"""              MENU
                 (-1) SAIR
                 (1) Remover um livro da biblioteca
                 (2) Remover um membro da biblioteca
                 (3) Editar endereco e nome de membro da biblioteca 
                 (4) Editar nome e nome do autor do livro
                 (5) Voltar para o menu principal
                 Digite aqui a opção desejada: """)
        if escolha_final == '1':
            teste.remover_livro()
        elif escolha_final == '2':
            teste.remover_membro()
        elif escolha_final == '3':
            teste.editar_infos_membro()
        elif escolha_final == '4':
            teste.editar_infos_livro()
        elif escolha_final == '5':
            continue
        elif escolha_final == '-1':
            break
        else:
            print("Opcao invalida")

    elif opcao == '3':
        escolha_final = input(
"""              MENU
                 (-1) SAIR
                 (1) Exibir livros disponiveis para reserva 
                 (2) Exibir livros ja reservados 
                 (3) Exibir os membros da biblioteca 
                 (4) Exibir livros reservados por um membro 
                 (5) Exibir quem possui cada livro
                 (6) Exibir data de emprestimo e devolucao dos livros
                 (7) Voltar para o menu principal
                 Digite aqui a opção desejada: """)

        if escolha_final == '1':
            teste.exibir_livros_disponiveis()
        elif escolha_final == '2':
            teste.exibir_livros_emprestados()
        elif escolha_final == '3':
            teste.exibir_membros_biblioteca()
        elif escolha_final == '4':
            id_membro = int(input("Digite seu CPF"))
            teste.exibir_livros_reservados_por_membro(id_membro)
        elif escolha_final == '5':
            teste.print_donos()
        elif escolha_final == '6':
            teste.exibir_datas_emprestimo_e_devolucao()
        elif escolha_final == '7':
            continue
        elif escolha_final == '-1':
            break
        else:
            print("Opcao invalida")

    elif opcao == '4':
        escolha_final = input(
"""              MENU
                 (-1) SAIR
                 (1) Pegar um livro emprestado 
                 (2) Devolver um ou todos os livros que voce pegou emprestado
                 (3) Voltar para o menu principal 
                 Digite aqui a opção desejada: """)
        if escolha_final == '1':
            teste.pegar_livro_emprestado()
        elif escolha_final == '2':
            teste.devolver_livro()
        elif escolha_final == '3':
            continue
        elif escolha_final == '-1':
            break
        else:
            print("Opcao invalida")
        pass
    elif opcao == '-1':
        break
    else:
        print("Opcao Invalida!!")
