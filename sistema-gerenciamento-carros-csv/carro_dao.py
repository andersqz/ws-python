from carro import Carro
import csv

def proximo_id():
    try:
        with open("carros.csv", "r", encoding="utf-8") as arquivo:
            reader = csv.reader(arquivo, delimiter=";")
            linhas = list(reader)
            if not linhas: # m C++ ficaria if (linhas.size() == 0)
                return 1
            else:
                return int(linhas[-1][0]) + 1 # [-1] pega a ultima linha da lista de listas, [0] pega o primeiro indice da ultima linha
    except FileNotFoundError:
         return 1

def guardar_carro():
        print("===== ALUGUEL DE CARRO =====")
        
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        cor = input("Cor: ")
        ano = input("Ano de fabricação: ")
        id = proximo_id()

        meu_carro = Carro(marca, modelo, cor, ano)

        with open("carros.csv", "a", newline="", encoding="utf-8") as arquivo:
                writer = csv.writer(arquivo, delimiter=";")
                writer.writerow([id, meu_carro.marca, meu_carro.modelo, meu_carro.cor, meu_carro.ano, meu_carro.alugado])

        print("Carro cadastrado com sucesso!")
        return meu_carro

def listar_carro():
    print("===== LISTA DE CARRO =====")

    try:
        with open("carros.csv", "r", encoding="utf-8") as arquivo:
                reader = csv.reader(arquivo, delimiter=";")
                for linha in reader:
                    id, marca, modelo, cor, ano, alugado = linha # isso aqui 'desempacota' os campos/atributos
                    print(f"[{id}]| Marca: {marca}| Modelo: {modelo}| Cor: {cor}| Ano: {ano}| Status: {"Alugado" if alugado == "True" else "Disponível"}")
                    print("-" * 80)
    except FileNotFoundError:
          print("Nenhum carro cadastrado.")
            

def alugar_carro():
    print("===== ALUGUEL DE CARRO =====")
    with open("carros.csv", "r", encoding="utf-8") as arquivo:
         reader = csv.reader(arquivo, delimiter=";")
         for linha in reader:
              id, marca, modelo, cor, ano, alugado = linha
              print(f"[{id}]| Marca: {marca}| Modelo: {modelo}| Cor: {cor}| Ano: {ano}| Status: {"Alugado" if alugado == "True" else "Disponível"}")
              print("-" * 80)
    id_buscado = int(input("Digite o ID do carro: "))

    with open("carros.csv", "r", encoding="utf-8") as arquivo:
         reader = csv.reader(arquivo, delimiter=";")
         linhas = list(reader) # recebe o reader, que é a variavel que recebeu o arquivo, em forma de uma lista de listas

    encontrado = False
    for linha in linhas:
         if int(linha[0]) == id_buscado:
              encontrado = True
              if linha[5] == "True":
                  print("Esse carro já está alugado!")
              else:
                  linha[5] = "True"
                  with open("carros_alugados.csv", "a", newline="", encoding="utf-8") as arquivo:
                       writer = csv.writer(arquivo, delimiter="")
                       writer.writerow(linha)
                  print("Carro alugado com sucesso!")
              break
    if not encontrado:
         print("Carro não encontrado!")
         return

    with open("carros.csv", "w", newline="", encoding="utf-8") as arquivo:
         writer = csv.writer(arquivo, delimiter=";")
         writer.writerows(linhas)

def remover_carro():
    print("===== ALUGUEL DE CARRO =====")
    with open("carros.csv", "r", encoding="utf-8") as arquivo:
         reader = csv.reader(arquivo, delimiter=";")
         for linha in reader:
              id, marca, modelo, cor, ano, alugado = linha
              print(f"[{id}]| Marca: {marca}| Modelo: {modelo}| Cor: {cor}| Ano: {ano}| Status: {"Alugado" if alugado == "True" else "Disponível"}")
              print("-" * 80)
    id_buscado = int(input("Digite o ID do carro: "))

    with open("carros.csv", "r", encoding="utf-8") as arquivo:
         reader = csv.reader(arquivo, delimiter=";")
         linhas = list(reader)

    encontrado = False
    for linha in linhas:
        if int(linha[0]) == id_buscado:
            encontrado = True
            with open("carros_removidos.csv", "a", newline="", encoding="utf-8") as arquivo:
                writer = csv.writer(arquivo, delimtier=";")
                writer.writerow(linha)
            print(f"Carro [{linha[1]}] removido com sucesso!")
            break
        if not encontrado:
             print("Carro não encontrado na garagem!")
             return
        
        linhas = [linha for linha in linhas if int(linha[0]) != id_buscado]

        with open("carros.csv", "w", newline="", encoding="utf-8") as arquivo:
             writer.csv.writer(arquivo, delimtier=";")
             writer.writerows(linhas)
            