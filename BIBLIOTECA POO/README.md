
![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)
# Biblioteca Virtual

Este é um sistema de gerenciamento de biblioteca virtual desenvolvido em Python, que permite realizar operações básicas de gerenciamento de livros, membros e empréstimos.

## Funcionalidades

- **Gerenciamento de Membros**:
  - Adicionar novos membros à biblioteca.
  - Remover membros existentes.
  - Editar informações de membros (nome e endereço).
  - Exibir todos os membros cadastrados na biblioteca.

- **Gerenciamento de Livros**:
  - Adicionar novos livros ao acervo.
  - Remover livros do acervo.
  - Editar informações de livros (título e autor).
  - Exibir todos os livros disponíveis na biblioteca.
  - Exibir todos os livros atualmente emprestados.

- **Empréstimos e Devoluções**:
  - Registrar o empréstimo de livros para membros.
  - Registrar a devolução de livros emprestados.
  - Exibir datas de empréstimo e data de devolução prevista.

## Estrutura do Projeto

O projeto está estruturado em classes que representam diferentes componentes da biblioteca:

- **Livro**: Representa um livro na biblioteca, com título, autor e status de disponibilidade.
- **Membro**: Representa um usuário da biblioteca, com nome, ID (CPF), endereço e lista de livros emprestados.
- **Emprestimo**: Gerencia as informações de um empréstimo específico, incluindo o nome do membro, ID do membro, nome do livro, autor, data de empréstimo e data de devolução.
- **Biblioteca**: Classe principal que contém listas de livros disponíveis, membros cadastrados e empréstimos registrados, além de métodos para interação com esses objetos.

## Utilização

Para utilizar o sistema, você pode executar o arquivo `main.py` que contém a lógica principal do programa. Aqui estão alguns exemplos de operações que você pode realizar:

- Adicionar novos membros e livros.
- Realizar empréstimos de livros para membros cadastrados.
- Registrar a devolução de livros emprestados.
- Editar informações de membros e livros existentes.
- Visualizar todos os livros disponíveis e os membros cadastrados na biblioteca.

## Como Executar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Clone este repositório para o seu ambiente local.
3. Navegue até o diretório onde o projeto foi clonado.
4. Execute o arquivo `main.py` para iniciar o programa.

```bash
python main.py