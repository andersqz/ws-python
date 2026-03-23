
gamesSet = {"Residente Evil", "Stars Wars Jedi Survivor", 
            "The Legend of Zelda", "Read Dead 2", "God Of War 2018", 
            "Hytale"}
print(gamesSet)

# 1 - buscar tamanho do set
print(len(gamesSet))

# 2 - True e 1 sao considerados o mesmo valor
exampleSet = {"Fifa", True, 1, 90.50}
print(exampleSet)

# 3 - Adicionar item de outro set
gamesSet.update(exampleSet)
gamesSet.remove(True)
gamesSet.remove(90.50)
print(gamesSet)











# - nao possibilita recuperar valores via fatiamento ou slice


