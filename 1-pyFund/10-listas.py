'''
gameFifa = ["Fifa 23", 2023, 300.00, True]
print(gameFifa)

gameList = ["Residente Evil", "Stars Wars Jedi Survivor", 
            "The Legend of Zelda", "Read Dead 2", "God Of War 2018"]
print(gameList)

# buscar os dois primeiros itens da lista
print(gameList[0:2]) # busca indice[0] e indice[1]


# buscar o ultimo item da lista
print(gameList[-1])


# buscar jogos ate uma determinada posicao
print(gameList[:3]) # busca do indice[0] ate o indice[2]

# buscar jogos de uma posicao em diante
print(gameList[1:3])
'''


gameList = ["Residente Evil", "Stars Wars Jedi Survivor", 
            "The Legend of Zelda", "Read Dead 2", "God Of War 2018", 
            "Hytale"]


# 1 tamanho da lista
print(len(gameList))

#2 - recuperar um item da lista pelo indice
print(gameList.index("Hytale"))

# 3 - Incluir um item ao final da lista
print(gameList.append("GTA V"))

# 4 - ordenar a lista
gameList.sort()
print(gameList)

# 5 - copiar os itens de uma lista para outra
gameReset = gameList.copy()
gameReset.remove("Star wars Jedi Survivor")
print(gameReset)

# 6 - zera a lista
gameList.clear()
print(gameList)


