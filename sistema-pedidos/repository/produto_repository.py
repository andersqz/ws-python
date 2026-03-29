from models.Produto import Produto
import csv


def proximo_id(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            reader = csv.reader(arquivo, delimiter=";")
            linhas = list(reader)
            if not linhas: # m C++ ficaria if (linhas.size() == 0)
                return 1
            else:
                return int(linhas[-1][0]) + 1 # [-1] pega a ultima linha da lista de listas, [0] pega o primeiro indice da ultima linha
    except FileNotFoundError:
         return 1


def cadastrar_produto(nome_arquivo, nome, preco):
    novo_id = proximo_id(nome_arquivo)
    obj_produto = Produto(int(novo_id), nome, float(preco))

    with open(nome_arquivo, "a", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo, delimiter=";")
        writer.writerow([novo_id, obj_produto.nome, obj_produto.preco])
        
    return obj_produto

def listar_produtos(nome_arquivo):
    produtos = []

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        reader = csv.reader(arquivo, delimiter=";")
        for linha in reader:
            id, nome, preco = linha # desempacotamento dos dados
            obj_produto = Produto(int(id), nome, float(preco))
            produtos.append(obj_produto)
    return produtos
