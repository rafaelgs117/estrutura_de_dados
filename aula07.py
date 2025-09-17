#aula de hoje foi feita para resolver alguns problemas envolvendo tuplas,
#como adicionar um novo elemento a ela, usar o split para separa string mais informaç]ao no slide da aula 7
def ordena_palavras(frase):
    lista = list(frase) #converte string em lista
    lista = frase.split() #split separa a string em palavras
    lista.sort() #ordena a lista em ordem alfabética
    return lista

print(ordena_palavras('olha esta foto')) # se tudo estiver certo deve retornar ['esta', 'foto', 'olha']

#deve modificar L cada elemento 'e' em 'L' deve ser trocado por e*e
def lista_ao_quadrado(L):
    i = 0
    for elemento in L: #percorre cada elemento da lista
        L[i] = elemento * elemento #modifica o elemento na posição i

L = [1, 2, 3, 4, 5]
print(('antes: ', L)) #deve retornar [1, 2, 3, 4, 5]
lista_ao_quadrado(L)
print(('depois: ', L)) #deve retornar [1, 4, 9, 16, 25]

G = [1,2,3]
for i in range(len(G)):
    G.append(i)
print(G)
