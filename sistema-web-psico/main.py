from Paciente_dao import cadastro_paciente
from Paciente_dao import listar_pacientes
from Paciente_dao import editar_paciente
from Paciente_dao import remover_paciente

while True:
    print("sistema de gestão de clínicas")
    print("1. Cadastrar Paciente")
    print("2. Listar Pacientes")
    print("3. Editar Paciente")
    print("4. Remover Paciente")
    print("5. Sair do sistema ...")

    try:
        opcao = int(input("Opção: "))
    except ValueError:
        print("Digite um número válido.")
        continue

    if opcao == 1:
        obj_paciente = cadastro_paciente()
    elif opcao == 2:
        listar_pacientes()
    elif opcao == 3:
        editar_paciente()
    elif opcao == 4:
        remover_paciente()
    elif opcao == 5:
        print("Obrigado por usar o sistema! Até mais.")
        break
    else:
        print("Opção inválida por enquanto!")