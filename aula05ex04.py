def aplica(criterio, n):
    return criterio(n)

def par(n):
    return n % 2 == 0  
def impar(n):
    return n % 2 != 0

print('4 é par?')
print(aplica(par, 4))   #True

print('4 é impar?')
print(aplica(impar, 4)) #False

print('5 é par?')
print(aplica(par, 5))   #False

print('5 é impar?')
print(aplica(impar, 5)) #True

