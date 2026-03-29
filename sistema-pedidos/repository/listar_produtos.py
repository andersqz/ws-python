from models.Produto import Produto
import csv

def listar_produtos(nome_arquivo):
    produtos = []

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        reader = csv.reader(arquivo, delimiter=";")
        for linha in reader:
            id, nome, preco = linha # desempacotamento dos dados
            obj_produto = Produto(int(id), nome, float(preco))
            produtos.append(obj_produto)
    return produtos
