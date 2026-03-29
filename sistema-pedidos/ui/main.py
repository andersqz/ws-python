from models.Produto import Produto
from repository.produto_repository import cadastrar_produto, listar_produtos
nome_arquivo = "produtos.csv"

while True:
    print("****************** M E N U ******************")

    print("1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Editar Produto")
    print("4. Remover Produto")
    print("5. Criar Pedido")
    print("6. Sair")

    try:
        opcao = int(input("Opção: "))
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")
        continue
    
    if opcao == 1:
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        produto = cadastrar_produto(nome_arquivo, nome, preco)
        print("Produto cadastrado com sucesso!")

    elif opcao == 2:
        produtos = listar_produtos(nome_arquivo)
        for produto in produtos:
            print(f"[{produto.id}] | Nome: {produto.nome} | Preço: {produto.preco}")
        print("Produtos listados com sucesso!")

    elif opcao == 6:
        print("Obrigado por usar o sistema! Até mais.")
        break
    else:
        print("Entrada inválida! Digite um número inteiro.")
    