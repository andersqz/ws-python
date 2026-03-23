
'''name = "Fifa 23"

# pega o caractere localizado no indice 0 
# e guarda em char ele retornado em minusculo
char = name[0].lower()

# nem_name recebe a string name aonde 
# tiver char, ele substitui por '$'
new_name = name.replace(char, '$')

# new name recebe a concatenação de strings
# de char['f' minusculo] mais a 
# new_name[do indice 1 pra frente]
new_name = char + new_name[1:]

print(new_name)'''

st1 = 'cab' # zyb
st2 = 'zyx' # cax

new_st1 = st2[:2] + st1[2:]
new_st2 = st1[:2] + st2[2:]
print(new_st1 + ' ' + new_st2)


