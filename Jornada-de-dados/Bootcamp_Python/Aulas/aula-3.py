# Introdução do Debugger, controle de fluxo, lista e dicionário.

x: int = 2

if x < 0:
    print('Negativo.')
elif x == 0:
    print ('Zero.')
elif x == 1:
    print ('Um.')
else:
    print ('Maior que um.')

# Inserimos o pointer na linha onde x = 2 para debugar o fluxo desde o início.
# Passo a passo vimos a execução do programa até o momento em que ele chegasse
# no else onde a execução seria feita.

for i in range (1,5):
    print(i)

# Debugando e iterando sobre um range
# Ele vai do primeiro número mas não chega no último 
# Output (1, 2, 3, 4)    

lista_jogos = ["Devil May Cry", "Resident Evil", "Silent Hill"]

for jogo in lista_jogos:
    print(jogo)

# Iterando e Debugando uma lista
# Ele imprime todos os itens da lista e depois finaliza a execução


