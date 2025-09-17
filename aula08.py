def remove_tudo(L, e):
    #entrada lista L elemento e, saida nenhuma, remover todas as ocorrebcias de e em L
    while e in L:
        L.remove(e)
    return L # não nporecisa do return, mas é util para testes
#testes
L = [1, 2, 3, 4, 3, 5, 3]
print('print 1 rovome num 3: ',remove_tudo(L, 3)) # [1, 2, 4, 5]
print('print 2 usando pop: ',L.pop()) # pop remove e retorna o ultimo elemento da lista, o primeiro print ja removeu o 3 entao esse ira msotra 5

#sem return ficaria
#    while e in L:
#        L.remove(e)
#L = [1, 2, 3, 4, 3, 5, 3]
#remove_tudo(L, 3)
#print(L) # [1, 2, 4, 5]

# criando uma copia de L
L = [1, 2, 3, 4, 3, 5, 3]
L2 = L[:] # ou L2 = list(L)
remove_tudo(L2, 3)
print('')
print('print 3 L original: ',L) # [1, 2, 3, 4, 3, 5, 3]
print('print 4 L2 que foi uma copia de L: ',L2) # [1, 2, 4, 5]

#REMOVENDO ELEMENTOS DE UMA LISTA QUE ESTAO EM OUTRA LISTA
#forma incorreta
def remove_duplicado(L1, L3):
    for e in L1:
        if e in L3:
         L1.remove(e)

L1 = [1, 2, 3, 4, 3, 5, 3]
L3 = [3, 5]

print('')
remove_duplicado(L1, L3)
print('print 5 remove duplicado (incorreta): ',L1) # vai dar errado vai tira apenas o 3 numero 5 vai ficar
print('')
# agora a forma correta, decce criar uma copia de L1 e usar [] couchetes para criar a copia
def remove_duplicada(L1, L3):
   for e in L1[:]: # criando uma copia de L1
        if e in L3:
         L1.remove(e)

remove_duplicada(L1, L3)
print('print 6 remove duplicado certo: ',L1) # [1, 2, 4]
print('')

#
lista_antiga = [[1, 2], [3, 4], [5,"FMP"]]
lista_nova = lista_antiga # cria uma nova referencia para o mesmo objeto

lista_nova[2][1] = 6 #esta modificando o objeto que lista_nova e lista_antiga referenciam por que sao o mesmo objeto
print('lista nova: ',lista_nova) # [[1, 2], [3, 4], [5, 6]]
print('lista antiga: ',lista_antiga) # [[1, 2], [3, 4], [5, 6]]
print('')
# para criar uma copia de uma lista que contem outras listas, deve-se usar o metodo copy do modulo copy

import copy
lista_antiga = [[1, 2], [3, 4], [5,"FMP"]]
lista_nova = copy.copy(lista_antiga) # cria uma copia rasa (shallow copy)

lista_antiga.append([7, 8]) # adiciona um novo elemento a lista_antiga
lista_antiga[1][1] = 9 # modifica elemento das listas internas troca o 4 por 9, ambas as listas mesma caso da anterior são mesmo objeto

print('lista nova com copy: ',lista_nova) # [[1, 2], [3, 9], [5, 'FMP']]
print('lista antiga com copy: ',lista_antiga) # [[1, 2], [3, 9], [5, 'FMP'], [7, 8]]
print('')

#usando agora deepcopy
lista_antiga = [[1, 2], [3, 4], [5,"FMP"]]
lista_nova = copy.deepcopy(lista_antiga) # cria uma copia profunda (deep copy) é uma copia independente unica

lista_antiga.append([7, 8]) # adiciona um novo elemento a lista_antiga
lista_antiga[1][1] = 9 # modifica lista_antiga e troca o 4 por 9 agora modifica apenas a lista_antiga

print('lista nova com deepcopy: ',lista_nova) # [[1, 2], [3, 4], [5, 'FMP']]
print('lista antiga com deepcopy: ',lista_antiga) # [[1, 2], [3, 9], [5, 'FMP'], [7, 8]]