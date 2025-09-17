def faz_duas_vezes(n,fn):
    return fn(fn(n)) # chama a função fn duas vezes

print(faz_duas_vezes("bom dia", lambda x: x + x))
print()
#--------- TUPLAS ---------

te = () # tupla vazia, tupla é uma estrutura de dados imutável
ts =(2, ) # tupla com um elemento, precisa da vírgula
t = (2, "fmp", 3) # tupla com três elementos

print(ts) # tuplas são imprimidas sempre com parênteses ex: (2,)
print()

#--------- Indices e Fatiamento ---------

seq = (2, 'a', 4, (1,2)) # tuplas podem ser concatenadas
print(len(seq)) # tamanho da tupla
print(seq[3]) # aimprime a tupla interna
print(seq[-1]) # imprime o último elemento
print(seq[3][0]) # aimprime valor 1 da tupla interna
#print(seq[4]) # erro de índice
print()

#--------- titullo temporario ---------



