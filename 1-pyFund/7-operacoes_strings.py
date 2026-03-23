

gameDescription = """
Fifa 23 eh um jogo de futebol 
desenvolvido pela EA Sports 
e que possibilita jogar online ou localmente
"""

gameName = "Fifa"
gameVersion = "23.0"
line = "="


# concatenação de strings
gameFullname = gameName + " " + gameVersion
print(gameFullname)
print(line * 25)


# multiplicação de strings
line = "="
print(line * 25)

# procura de palavra dentro de um texto
print("Fifa" in gameDescription)
print("fifa" in gameDescription)
print("Futebol" in gameDescription)
