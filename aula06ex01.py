#Escreva uma função que atenda à seguinte especificação:
#def conta_caracteres(s):    
#    ENTRADA: Uma string 's' com caracteres em letra minúscula
#    SAÍDA: Uma tupla onde o primeiro elemento é  o número de vogais e o segundo é o número de consoantes 
#    e ignorar espaços vazios

#Alguns exemplos do comportamento esperado:
#print(conta_caracteres("abcd")) # Deve imprimir (1, 3)
#print(conta_caracteres("zcght")) # Deve imprimir (0, 5)

def conta_caracteres(s):
    vogais = 'aeiou'
    consoantes = 'bcdfghjklmnpqrstvwx'
    num_vogais = 0
    num_consoantes = 0
    
    for char in s:
        if char in vogais:
            num_vogais += 1
        elif char in consoantes:
            num_consoantes += 1
            
            
    return (num_vogais, num_consoantes)

print(conta_caracteres("star tears")) # imprimi quantas vogais e consoantes tem na string exluindo espaço
print(conta_caracteres("alguma coisa aleatoria")) # mesma coisa que a de cima
