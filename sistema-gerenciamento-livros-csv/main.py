from livro_dao import guardar_livro
from livro_dao import listar_livro
from livro_dao import alugar_livro

while True:

    print("sistema de gerenciamento de livros em um acervo")
    print("*" * 40)
    print("1. Cadastrar Livro")
    print("2. Listar Livros")
    print("3. Alugar Livro")
    print("4. Remover Livro")
    print("5. Sair")

    try:
        opcao = int(input("Opção: "))
    except FileNotFoundError:
        print("Digite um numero valido!")

    if opcao == 1:
        livro = guardar_livro()
    elif opcao == 2:
        livro = listar_livro()
    elif opcao == 3:
        livro = alugar_livro()
    elif opcao == 5:
        print("Obrigado por usar o sistema! Até mais.")
        break


