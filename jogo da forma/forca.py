# Trabalho 1
# Nome do Estudante: Rafael Gonçalves da Silva

import os # tive que importar python nao achava o arquivo com as palavra
import random
import string

# -----------------------------------
# CÓDIGO AUXILIAR
# -----------------------------------

# Carrega a lista de palavras do arquivo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_LISTA_PALAVRAS = os.path.join(BASE_DIR, "palavras.txt")

def carregar_palavras(): # funcao para carregar a lista com as palavras
    """
    SAÍDA: lista, uma lista de palavras válidas.  As palavras
    são strings em letra minúscula.
    """
    print("Carregando lista de palavras de arquivo...")

    try:
        with open(ARQUIVO_LISTA_PALAVRAS, 'r', encoding="utf-8") as noArquivo:
            linha = noArquivo.read()   # le todo o conteudo
            lista_de_palavras = linha.split()  # separa por espaços ou quebras de linha
            print(" ", len(lista_de_palavras), "palavras carregadas.")
            return lista_de_palavras
    except FileNotFoundError:
        print(f"Erro: o arquivo '{ARQUIVO_LISTA_PALAVRAS}' não foi encontrado.") # se nao achar o arquivo de texto da esse erro
        print("Coloque o arquivo palavras.txt na mesma pasta do forca.py e tente novamente.")
        exit()


def escolhe_palavra(lista_de_palavras): # funcao que vai escolher a palavra usando random para sortear
    """
    ENTRADA: 'lista_de_palavras': uma lista de palavras (strings)
    SAÍDA: Uma palavra escolhida da lista
    """
    return random.choice(lista_de_palavras)

# -----------------------------------
# FIM DO CÓDIGO AUXILIAR
# -----------------------------------

# Carrega a lista de palavras para ser acessível de qualquer parte do programa
lista_de_palavras = carregar_palavras()

def jogador_venceu(palavra_secreta, letras_escolhidas): # verifica se o jogador venceu o jogo
    """
    ENTRADA: 'palavra_secreta', uma string em letras minúsculas que o usuário
             deve adivinhar
             'letras_escolhidas': lista de letras minúsculas que o jogador
             escolheu até agora para adivinhar a palavra
    SAÍDA: True, se todas as letras de 'palavra_secreta' estão em 
           'letras_escolhidas' e False caso contrário
    """
    for letra in palavra_secreta:
        if letra not in letras_escolhidas:
            return False
    return True
    


def progresso_atual_da_palavra(palavra_secreta, letras_escolhidas): # monstra como esta o progresso do jogo monstrando as letras acertada e como * as letras erradas
    """
    ENTRADA: 'palavra_secreta', string em letra minúscula que usuário está
             adivinhando.
             'letras_escolhidas', uma lista de letras minúsculas que o jogador
             escolheu até agora
    SAÍDA: Uma string formada por letras e asteriscos (*) que representam letras
           na palavra secreta que ainda não foram adivinhadas
    """
    progresso = ''
    for letra in palavra_secreta:
        if letra in letras_escolhidas:
            progresso += letra
        else:
            progresso += '*' # letra nao descoberta
    return progresso


def letras_ainda_disponiveis(letras_escolhidas): # MOSTRA AS LETRAS QUE AINDA NAO FORAM ESCOLHIDAS
    """
    ENTRADA: 'letras_escolhidas', lista de letras minúsculas que o usuário
             escolheu até agora.
    SAÍDA: Uma string formada por todas as letras que ainda não foram escolhidas.
           As letras devem ser retornadas em ordem alfabética.
    """
    alfabeto = string.ascii_lowercase # mostrra o alfabeto em letrasd minsculas
    return ''.join([letra for letra in alfabeto if letra not in letras_escolhidas])



def forca(palavra_secreta, com_ajuda): # 
    """
    ENTRADA: 'palavra_secreta', uma string representando uma palavra a ser
             adivinhada
             'com_ajuda', um valor booleano que ativa a funcionalidade de ajuda
             se verdadeiro

    Isso inicia um jogo interativo de Forca.

    * No começo do jogo, deixe o usuário saber quantas letras
      a string 'palavra_secreta' contém e quantas tentativas ele tem de
      escolher letras.

    * O usuário deve começar com 10 tentativas.

    * Antes de cada rodada, você deve mostrar ao usuário quantas tentativas
      ele ainda tem  e as letras que ele ainda não escolheu.

    * Peça ao usuário para escolher uma letra por rodada. Lembre-se de
      checar se o usuário realmente está inserindo uma só letra (ou
      o caractere de ajuda  '!' se a funcionalidade de ajuda está ativa)

    * Se o usuário escolher uma consoante incorreta, ele perde UMA tentativa,
      mas se ele escolher uma vogal incorreta (a, e, i, o, u),
      então ele perde DUAS tentativas.

    * O usuário deve receber informações imediatamente
      após cada tentativa de escolher uma letra para que ele saiba
      se a letra escolhida aparece na palavra secreta.

    * Depois de cada escolha, você deve mostrar ao usuário a palavra
      parcialmente adivinhada até agora.

    -----------------------------------
    A funcionalidade 'com_ajuda' 
    -----------------------------------
    * Se a escolha for o símbolo !, você deve revelar ao usuário uma das letras
      faltantes da palavra ao custo de 3 tentativas. Se o usuário não tem
      3 tentativas restantes, imprima uma mensagem de aviso. Do contrário,
      adicione esta letra à lista de letras adivinhadas e continue jogando
      normalmente.
    """
    print("Bem-vindo ao jogo da Forca!")
    print("A palavra secreta contém", len(palavra_secreta), "letras.") # diz quantas letras ten a oalavra
    
    tentativas = 10
    letras_escolhidas = []
    
    while tentativas > 0 and not jogador_venceu(palavra_secreta, letras_escolhidas): #continua o jogo se o jogador tiver chances e não ter ganhado
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



# Quando você terminar a função 'forca', vá até o fim do arquivo descomentando
# as linhas indicadas para poder testar seu jogo

if __name__ == "__main__":
    # Para testar seu jogo, descomente as seguintes 3 linhas:

    # palavra_secreta = escolhe_palavra(lista_de_palavras)
    # com_ajuda = False
    # forca(palavra_secreta, com_ajuda)

    # Depois que você implementar a funcionalidade 'com_ajuda', mude
    # o valor de 'com_ajuda' acima para e tente testar usando "!" como
    # letra escolhida!

    palavra_secreta = escolhe_palavra(lista_de_palavras)
    com_ajuda = True  # coloque False se não quiser ativar o "!"
    forca(palavra_secreta, com_ajuda)
