# Trabalho 1
# Nome do Estudante: Rafel Gonçalves da Silva

import random
import string
import os   # <--- import adicionado para lidar com caminhos poe alguma razão mesmo estando mesmo diretorio bnao estava achabdo

# -----------------------------------
# Co´DIGO AUXILIAR
# -----------------------------------

# Caminho absoluto do arquivo palavras.txt (sempre na mesma pasta do script)
BASE_DIR = os.path.dirname(__file__)
ARQUIVO_LISTA_PALAVRAS = os.path.join(BASE_DIR, "palavras.txt")

def carregar_palavras():
    """
    SAÍDA: lista, uma lista de palavras válidas.  As palavras
    são strings em letra minúscula.
    """
    print("Carregando lista de palavras de arquivo...")
    with open(ARQUIVO_LISTA_PALAVRAS, 'r', encoding="utf-8") as noArquivo:
        linha = noArquivo.readline()
    lista_de_palavras = linha.split()
    print(" ", len(lista_de_palavras), "palavras carregadas.")
    return lista_de_palavras

def escolhe_palavra(lista_de_palavras):
    """Retorna uma palavra aleatória da lista."""
    return random.choice(lista_de_palavras)

# -----------------------------------
# FIM DO CÓDIGO AUXILIAR
# -----------------------------------

lista_de_palavras = carregar_palavras()

def jogador_venceu(palavra_secreta, letras_escolhidas):
    """Retorna True se todas as letras da palavra já foram escolhidas."""
    for letra in palavra_secreta:
        if letra not in letras_escolhidas:
            return False
    return True

def progresso_atual_da_palavra(palavra_secreta, letras_escolhidas):
    """Mostra a palavra com letras adivinhadas e * para as não descobertas."""
    progresso = ''
    for letra in palavra_secreta:
        if letra in letras_escolhidas:
            progresso += letra
        else:
            progresso += '*'
    return progresso

def letras_ainda_disponiveis(letras_escolhidas):
    """Retorna as letras do alfabeto que ainda não foram escolhidas."""
    alfabeto = string.ascii_lowercase
    return ''.join([letra for letra in alfabeto if letra not in letras_escolhidas])

def forca(palavra_secreta, com_ajuda):
    """Jogo da forca interativo com ou sem ajuda."""
    print("Bem-vindo ao jogo da Forca!")
    print("A palavra secreta contém", len(palavra_secreta), "letras.")
    
    tentativas = 10
    letras_escolhidas = []
    
    while tentativas > 0 and not jogador_venceu(palavra_secreta, letras_escolhidas):
        print("\nVocê tem", tentativas, "tentativas restantes.")
        print("Letras disponíveis:", letras_ainda_disponiveis(letras_escolhidas))
        print("Palavra atual:", progresso_atual_da_palavra(palavra_secreta, letras_escolhidas))
        
        escolha = input("Escolha uma letra: ").lower()
        
        # Função de ajuda
        if escolha == '!' and com_ajuda:
            if tentativas >= 3:
                for letra in palavra_secreta:
                    if letra not in letras_escolhidas:
                        letras_escolhidas.append(letra)
                        tentativas -= 3
                        print("Letra revelada:", letra)
                        break
            else:
                print("Você não tem tentativas suficientes para usar a ajuda.")
            continue
        
        # Verificação de entrada válida
        if len(escolha) != 1 or not escolha.isalpha():
            print("Por favor, escolha uma única letra válida.")
            continue
        
        if escolha in letras_escolhidas:
            print("Você já escolheu essa letra. Tente outra.")
            continue
        
        letras_escolhidas.append(escolha)
        
        if escolha in palavra_secreta:
            print("Boa escolha! A letra", escolha, "está na palavra.")
        else:
            if escolha in 'aeiou':
                tentativas -= 2
                print("Letra incorreta! Você perdeu 2 tentativas por escolher uma vogal.")
            else:
                tentativas -= 1
                print("Letra incorreta! Você perdeu 1 tentativa por escolher uma consoante.")
    
    # Resultado final
    if jogador_venceu(palavra_secreta, letras_escolhidas):
        print("\nParabéns! Você adivinhou a palavra:", palavra_secreta)
    else:
        print("\nSuas tentativas acabaram. A palavra era:", palavra_secreta)

# Execução do jogo
if __name__ == "__main__":
    palavra_secreta = escolhe_palavra(lista_de_palavras)
    com_ajuda = True  # coloque False se não quiser ativar o "!"
    forca(palavra_secreta, com_ajuda)
