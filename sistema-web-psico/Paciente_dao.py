from Paciente import Paciente
import csv

def proximo_id():
    try:
        with open("pacientes.csv", "r", encoding="utf-8") as arquivo:
            reader = csv.reader(arquivo, delimiter=";")
            linhas = list(reader)
            if not linhas: # m C++ ficaria if (linhas.size() == 0)
                return 1
            else:
                return int(linhas[-1][0]) + 1 # [-1] pega a ultima linha da lista de listas, [0] pega o primeiro indice da ultima linha
    except FileNotFoundError:
         return 1

def cadastro_paciente():
    print("===== ÁREA DE CADASTRO DE PACIENTES =====")
    
    nome = input("Nome do paciente: ")
    email = input("Email do paciente: ")
    numero = int(input("Número do paciente: "))
    endereco = input("Endereço do paciente: ")
    id = proximo_id()

    obj_paciente = Paciente(nome, email, numero, endereco)

    with open("pacientes.csv", "a", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo, delimiter=";")
        writer.writerow([id, obj_paciente.nome, obj_paciente.email, obj_paciente.numero, obj_paciente.endereco])

    print("Paciente cadastrado com sucesso!")
    return obj_paciente

def listar_pacientes():
        print("===== LISTA DE PACIENTES =====")

        try:
             with open("pacientes.csv", "r", encoding="utf-8") as arquivo:
                  reader = csv.reader(arquivo, delimiter=";")
                  for linha in reader:
                       id, nome, email, numero, endereco = linha
                       print(f"[{id}] | Nome: {nome} | E-mail: {email} | Telefone: {numero} | Endereço: {endereco}")
                       print("-" * 160)
        except FileNotFoundError:
             print("Nenhum paciente cadastrado!")


def editar_paciente():
    print("===== EDITAR PACIENTE =====")
    with open("pacientes.csv", "r", encoding="utf-8") as arquivo:
        reader = csv.reader(arquivo, delimiter=";")
        for linha in reader:
            id, nome, email, numero, endereco = linha
            print(f"[{id}] | Nome: {nome} | E-mail: {email} | Telefone: {numero} | Endereço: {endereco}")
            print("-" * 160)

    id_buscado = int(input("Digite o ID do paciente que deseja editar: "))

    with open("pacientes.csv", "r", encoding="utf-8") as arquivo:
        reader = csv.reader(arquivo, delimiter=";")
        linhas = list(reader)

    encontrado = False
    for linha in linhas:
        if int(linha[0]) == id_buscado:
            encontrado = True

            id, nome, email, numero, endereco = linha
            print(f"\nPaciente encontrado: [{id}] | Nome: {nome}")
            print("O que deseja alterar? ")
            print("1 - Nome")
            print("2 - E-mail")
            print("3 - Número de telefone")
            print("4 - Endereço")

            opcao = int(input("Opção: "))

            if opcao == 1:
                new_name = input("Novo nome: ")
                linha[1] = new_name
            elif opcao == 2:
                new_email = input("Novo e-mail: ")
                linha[2] = new_email
            elif opcao == 3:
                new_numero = int(input("Novo número: "))
                linha[3] = new_numero
            elif opcao == 4:
                new_endereco = input("Novo endereço: ")
                linha[4] = new_endereco

    with open("pacientes.csv", "w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo, delimiter=";")
        writer.writerows(linhas)
    print("Edição efetuada com sucesso!")

def remover_paciente():
    print("===== REMOÇÃO DE PACIENTE =====")

    with open("pacientes.csv", "r", encoding="utf-8") as arquivo:
        reader = csv.reader(arquivo, delimiter=";")
        for linha in reader:
            id, nome, email, numero, endereco = linha
            print(f"[{id}] | Nome: {nome} | E-mail: {email} | Telefone: {numero} | Endereço: {endereco}")
            print("-" * 160)
    id_buscado = int(input("Digite o ID do paciente que deseja remover: "))

    with open("pacientes.csv", "r", encoding="utf-8") as arquivo:
        reader = csv.reader(arquivo, delimiter=";")
        linhas = list(reader)

    encontrado = False
    for linha in linhas:
        if int(linha[0]) == id_buscado:
            encontrado = True
            with open("pacientes_removidos.csv", "a", newline="", encoding="utf-8") as arquivo:
                writer = csv.writer(arquivo, delimiter=";")
                writer.writerow(linha)
            print(f"Paciente {linha[1]} removido com sucesso!")
            break

    if not encontrado:
        print("Paciente não localizado!")
        return
        
    linhas2 = [l for l in linhas if int(l[0]) != id_buscado]

    with open("pacientes.csv", "w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo, delimiter=";")
        writer.writerows(linhas2)




