from livro import Livro
import csv

def proximo_id():
    try:
        with open("livros.csv", "r", encoding="utf-8") as arquivo:
            reader = csv.reader(arquivo, delimiter=";")
            linhas = list(reader)
            if not linhas:
                return 1
            else:
                return int(linhas[-1][0]) + 1
    except FileNotFoundError:
        return 1
    

def guardar_livro():
    print("===== cadastro de livro no acervo =====")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    anoLancamento = int(input("Ano de lancaçmento: "))
    id = proximo_id()

    meu_livro = Livro(titulo, autor, anoLancamento)

    with open("livros.csv", "a", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo, delimiter=";")
        writer.writerow([id, meu_livro.titulo, meu_livro.autor, meu_livro.anoLancamento, meu_livro.alugado])

    print("Livro cadastrado com sucesso!")
    return meu_livro


def listar_livro():
    print("===== lista de livros no acervo =====")

    try:
        with open("livros.csv", "r", encoding="utf-8") as arquivo:
            reader = csv.reader(arquivo, delimiter=";")
            for linha in reader:
                id, titulo, autor, anoLancamento, alugado = linha
                print(f"{id} | Título: {titulo} | Autor: {autor} | Ano de Lançamento: {anoLancamento} | Status: {"Alugado" if alugado == "True" else "Disponível"}")
                print("*" * 80)
    except FileNotFoundError:
        print("Nenhum livro cadastrado no acervo!")


def alugar_livro():
        print("===== aluguel de livros no acervo =====")
        with open("livros.csv", "r", encoding="utf-8") as arquivo:
            reader = csv.reader(arquivo, delimiter=";")
            for linha in reader:
                id, titulo, autor, anoLancamento, alugado = linha
                print(f"[{id}] | Título: {titulo} | Autor: {autor} | Ano de lançamento: {anoLancamento} | Status: {"Alugado" if alugado == "True" else "Disponível"}")
                
        indice = int(input("Escolha um livro para alugar pelo índice: "))

        with open("livros.csv", "r", encoding="utf-8") as arquivo:
            reader = csv.reader(arquivo, delimiter=";")
            linhas = list(reader)

        encontrado = False
        for linha in linhas:
            if int(linha[0]) == indice:
                encontrado = True
                if linha[4] == "True":
                    print(f"Livro {linha[1]} já está alugado!")
                else:
                    linha[4] = "True"
                    with open("livros_alugados.csv", "a", newline="", encoding="utf-8") as arquivo:
                        writer = csv.writer(arquivo, delimiter=";")
                        writer.writerow(linha)
                    print("Livro alugado com sucesso")
                break
        if not encontrado:
            print("Livro não encontrado!")
            return
        
        with open("livros.csv", "w", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo, delimiter=";")
            writer.writerows(linhas)
     
def remover_livro():
        print("===== remoção de livros no acervo =====")
        with open("livros.csv", "r", encoding="utf-8") as arquivo:
            reader = csv.reader(arquivo, delimiter=";")
            for linha in reader:
                id, titulo, autor, anoLancamento, alugado = linha
                print(f"[{id}] | Título: {titulo} | Autor: {autor} | Ano de lançamento: {anoLancamento} | Status: {"Alugado" if alugado == "True" else "Disponível"}")
                
        indice = int(input("Escolha um livro para remover do acervo pelo índice: "))

        with open("livros.csv", "r", encoding="utf-8") as arquivo:
            reader = csv.reader(arquivo, delimiter=";")
            linhas = list(reader)

        encontrado = False
        for linha in linhas:
            if int(linha[0]) == indice:
                encontrado = True
                with open("livros_removidos.csv", "a", newline="", encoding="utf-8") as arquivo:
                    writer = csv.writer(arquivo, delimiter=";")
                    writer.writerow(linha)
                print(f"Livro [{linha[1]}] removido do acervo!")
                break
        if not encontrado:
            print("Livro não encontrado no acervo!")
            return
        
        # estrutura for para remover da lista a linha desejada
        for i in range(len(linhas)): # equivale ao for(int i = 0; i < linhas.size(); i++)
            if int(linhas[i[0]]) == indice:
                linhas.pop(i) # o pop remove o elemento no indice 'i' da lista, igual o erase do c++
                break

        # outra forma de escrever o for acima pra remover a linha da lista
        # e também sendo uma forma mais Pythonica é a forma abaixo:
        # linhas = [linha for linha in linhas if int(linha[0]) != indice]
        # significa: (pegue cada linha de linhas, mas só se o ID dela for diferente do indice buscado)

        # with open abre o arquivo e fecha automaticamente
        # aqui ele ta reescrevendo o arquivo sem a linha removida
        with open("livros.csv", "w", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo, delimiter=";")
            writer.writerows(linhas)
                
