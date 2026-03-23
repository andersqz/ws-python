from carro_dao import guardar_carro
from carro_dao import listar_carro
from carro_dao import alugar_carro
from carro_dao import remover_carro


while True:

    print("sistema de gerenciamento de carros em uma garagem")
    print("-" * 80)
    print("1. Guardar Carro")
    print("2. Listar Carro")
    print("3. Alugar Carro")
    print("4. Remover Carro")
    print("5. Sair")
    try:
        opcao = int(input("Opção: "))
    except ValueError:
        print("Digite um numero valido!")
        continue

    if opcao == 1:
        carro = guardar_carro()
    elif opcao == 2:
        carro = listar_carro()
    elif opcao == 3:
        carro = alugar_carro()
    elif opcao == 4:
        carro = remover_carro()
    elif opcao == 5:
        print("Obrigado por usar o sistema! Até mais.")
        break



    

    
