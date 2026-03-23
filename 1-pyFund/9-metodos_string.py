
gameName = "Fifa 23"
gameDescription = """
Fifa 23 eh um jogo de futebol 
desenvolvido pela EA Sports 
e que possibilita jogar online ou localmente
"""


print(gameName.upper()) # upper() retorna a string maisucula
print(gameName.lower())# lower() retorna a string minuscula 
print(gameName.capitalize()) # capitalize() retorna a primeira letra maiuscula
print(gameName.title()) # retorna a primeira letra maiuscula
print(gameName.center(11, "-")) # retorna a string centralizada com caractere de preenchimento
print(gameName.find("i")) # retorna a posicao de determinado caractere
print(gameDescription.count("a"))
print(gameDescription.count("f"))
print(gameDescription.replace("Fifa", "Pes"))
print(gameDescription.split(','))

