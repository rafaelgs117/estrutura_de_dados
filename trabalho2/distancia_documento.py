# Trabalho 2
# Nome do Estudante: RAfael GOnçaves da sILVA

# Objetivo: testar a similaridade entre dois textos comparando diferentes tipos de estatística.

import string
import math


### Não MODIFIQUE ESTA FUNÇÃO
def carregar_arquivo(nome_arquivo):
    """
    ENTRADA:
        nome_arquivo: string, nome de arquivo a ler
    SAÍDA:
        string, conteúdo de arquivo
    """
    # print("Loading file %s" % nome_arquivo) - funciona se descomenta
    inFile = open(nome_arquivo, 'r') # abre o arquivo para leitura
    line = inFile.read().strip() # lê todo o conteúdo do arquivo e remove espaços em branco no início e fim
    for char in string.punctuation: # remove pontuação
        line = line.replace(char, "") # substitui cada caractere de pontuação por uma string vazia
    inFile.close() # fecha o arquivo
    return line.lower() # retorna o conteúdo do arquivo em letras minúsculas


### Problema 0: Preparar os Dados ###
def texto_para_lista(texto):
    """
    ENTRADA:
        texto: string com o texto de um arquivo. Você pode assumir que todas as letras
               são minúsculas
    SAÍDA:
        lista com as palavras da entrada, cada palavra é um elemento da lista
    """
    if texto == "": # verifica se o texto está vazio
        return [] # retorna uma lista vazia
    return texto.split() # divide o texto em palavras usando espaços em branco como delimitadores e retorna a lista de palavras

    


### Problema 1: Obter a frerquência ###
def obter_frequencia(iteravel):
    """
    ENTRADA:
        iteravel: uma lista de strings, todas com letras minúsculas
    SAÍDA:
        Um dicionário que mapeia strings para inteiros. Onde cada string é uma palavra de 'iteravel'. O inteiro associado a cada chave do dicionário
        é a frequência na qual ele aparece em 'iteravel'
    NOTA:
        Você pode assumir que os únicos tipos de espaçamento que existirão nos documentos
        serão espaços e quebras de linha. Não existirão TABs.
    """
    if len(iteravel) == 0: # verifica se o iterável está vazio
        return {} # retorna um dicionário vazio
    frequencia = {} # inicializa um dicionário vazio para armazenar a frequência das palavras
    for palavra in iteravel: # itera sobre cada palavra no iterável
        if palavra in frequencia: # verifica se a palavra já está no dicionário de frequência
            frequencia[palavra] += 1 # incrementa a contagem da palavra em 1
        else: 
            frequencia[palavra] = 1 # adiciona a palavra ao dicionário com uma contagem inicial de 1
    return frequencia
    


### Problema 2: Frequência de Letras ###
def obter_frequencia_letras(palavra):
    """
    ENTRADA:
        palavra: Uma string
    SAÍDA:
        dicionário que mapeia strings para inteiros onde
        cada string é uma letra de 'palavra' e o inteiro
        correspondente é a frequência daquela letra na palavra
    """
    frequencia = {} # inicializa um dicionário vazio para armazenar a frequência das letras
    for letra in palavra: # itera sobre cada letra na palavra
        if letra in frequencia: # verifica se a letra já está no dicionário de frequência
            frequencia[letra] += 1 # incrementa a contagem da letra em 1
        else:
            frequencia[letra] = 1 # adiciona a letra ao dicionário com uma contagem inicial de 1
    return frequencia # retorna o dicionário de frequência das letras



### Problema 3: Similaridade ###
def calcula_pontuacao_similaridade(dicionario1, dicionario2):
    """
    As chaves dos dicionários de entrada são compostas por letras minúsculas.

    ENTRADA:
        dicionario1: Dicionário com a frequência de letras da palavra1 ou texto1
        dicionario2: Dicionário com a frequência de letras da palavra2 ou texto2
    Saída:
        float, um número entre 0 e 1, inclusive
        representando o quão similares são as palavras/textos entre si

       As diferenças na frequência de letras/palavras é chamada de DIFF.

       DIFF é calculada somando os valores destes três cenários:

        * Se um elemento aparece em dicionario1 e dicionario2, o valor obtido dele
          é a diferença entre as frequências.
        * Se um elemento ocorre somente em dicionario1, seu valor obtido
          é a frequência em dicionario1
        * Se um elemento ocorre somente em dicionario2, seu valor obtido
          é a frequência em dicionario2

       A soma total de todas as frequências tanto em dicionario1 como
       em dicionario2 é chamada de ALL.

      O valor de retorno desta função será 1-(DIFF/ALL) arredondado para 
      2 casas decimais.
    """
    todas_chaves = set(dicionario1.keys()).union(set(dicionario2.keys())) # obtém todas as chaves únicas de ambos os dicionários
    diff = 0 # inicializa as variáveis para armazenar a diferença total
    all_freq = 0 # inicializa as variáveis para armazenar a diferença total e a soma total das frequências

    for chave in todas_chaves: # itera sobre cada chave única
        freq1 = dicionario1.get(chave, 0) # obtém a frequência da chave no dicionário1, ou 0 se não existir
        freq2 = dicionario2.get(chave, 0) # obtém a frequência da chave no dicionário2, ou 0 se não existir
        diff += abs(freq1 - freq2) # calcula a diferença absoluta entre as frequências e adiciona à diferença total
        all_freq += freq1 + freq2 # adiciona as frequências ao total de todas as frequências

    if all_freq == 0: # evita divisão por zero
        return 1.0 # se ambos os dicionários estiverem vazios, considera-os idênticos

    similaridade = 1 - (diff / all_freq) # calcula a similaridade como 1 menos a razão entre a diferença total e a soma total das frequências
    return round(similaridade, 2) # retorna a similaridade arredondada para 2 casas decimais



### Problema 4: Palavras mais frequentes  ###
def palavras_mais_frequentes(dicionario1, dicionario2):
    """
    As chaves dos dicionários de entrada são compostas por letras minúsculas.

    ENTRADA:
        dicionario1: Dicionário com a frequência de letras da palavra1 ou texto1
        dicionario2: Dicionário com a frequência de letras da palavra2 ou texto2
    SAÍDA:
        A lista das palavras mais frequentes nos dois dicionários

    A palavra mais frequente:
        * É baseada na combinação da frequência das palavras nos dois dicionários.
          Se uma palavra aparece nos dois, sua frequência deve ser considerada a
          soma da frequênca nos dois diconários.
        * As palavras mais frequentes não necessariamente aparecem em ambos os dicionários.
          Elas podem estar em só um deles.

    Se muitas palavras estiverem empatadas (tem a mesma frequência), retorne uma lista
    delas ordenada alfabeticamente.
    """
    frequencia_combinada = {} # inicializa um dicionário vazio para armazenar a frequência combinada das palavras

    for palavra, freq in dicionario1.items(): # itera sobre cada palavra e sua frequência no dicionário1
        frequencia_combinada[palavra] = frequencia_combinada.get(palavra, 0) + freq # adiciona a frequência da palavra ao dicionário combinado

    for palavra, freq in dicionario2.items(): # itera sobre cada palavra e sua frequência no dicionário2
        frequencia_combinada[palavra] = frequencia_combinada.get(palavra, 0) + freq # adiciona a frequência da palavra ao dicionário combinado

    if not frequencia_combinada: # verifica se o dicionário combinado está vazio
        return [] # retorna uma lista vazia

    max_frequencia = max(frequencia_combinada.values()) # encontra a frequência máxima entre todas as palavras
    palavras_mais_frequentes = [palavra for palavra, freq in frequencia_combinada.items() if freq == max_frequencia] # cria uma lista das palavras que têm a frequência máxima

    return sorted(palavras_mais_frequentes) # retorna a lista de palavras mais frequentes ordenada alfabeticamente



### Problema 5: ENcontrando TF-IDF ###
# Referência: https://pt.wikipedia.org/wiki/Tf%E2%80%93idf
def obter_tf(arquivo):
    """
    ENTRADA:
        arquivo: Nome de arquivo na forma de string
    SAÍDA:
        Um dicionário mapeando cada palavra ao seu TF

    * TF é calculado como TF(i) = (número de vezes que a palavra 'i' aparece
        no documento) / (número total de palavras no documento)
    * Use a função obter_frequencia definida antes.
    """
    texto = carregar_arquivo(arquivo) # carrega o conteúdo do arquivo
    palavras = texto_para_lista(texto) # converte o texto em uma lista de palavras
    frequencia_palavras = obter_frequencia(palavras) # obtém a frequência de cada palavra no documento
    total_palavras = len(palavras) # calcula o número total de palavras no documento

    tf = {} # inicializa um dicionário vazio para armazenar o TF de cada palavra
    for palavra, freq in frequencia_palavras.items(): # itera sobre cada palavra e sua frequência
        tf[palavra] = freq / total_palavras # calcula o TF da palavra e armazena no dicionário

    return tf


def obter_idf(arquivos):
    """
    ENTRADA:
        arquivos: Lista de nomes de arquivos, onde cada nome é uma string
    SAÍDA:
       Um dicionário mapeando cada palavra a seu IDF

    * IDF é calculado como IDF(i) = log_10(número total de documentos / número de documentos 
      que possuem a palavra 'i' nele), onde log_10 é logaritmo base 10 e pode ser invocado
      com math.log10()

    """
    import math # importa o módulo math para usar a função log10
    total_documentos = len(arquivos) # calcula o número total de documentos
    frequencia_documentos = {} # inicializa um dicionário vazio para armazenar a frequência de documentos para cada palavra

    for arquivo in arquivos: # itera sobre cada arquivo na lista de arquivos
        texto = carregar_arquivo(arquivo) # carrega o conteúdo do arquivo
        palavras = set(texto_para_lista(texto)) # converte o texto em uma lista de palavras e cria um conjunto para evitar contagens duplicadas
        for palavra in palavras: # itera sobre cada palavra única no conjunto
            frequencia_documentos[palavra] = frequencia_documentos.get(palavra, 0) + 1 # incrementa a contagem de documentos para a palavra

    idf = {} # inicializa um dicionário vazio para armazenar o IDF de cada palavra
    for palavra, freq in frequencia_documentos.items(): # itera sobre cada palavra e sua frequência de documentos
        idf[palavra] = math.log10(total_documentos / freq) # calcula o IDF da palavra e armazena no dicionário

    return idf # retorna o dicionário de IDF


def obter_tfidf(arquivo_tf, arquivos_idf):
    """
        ENTRADA:
            arquivo_tf: nome de arquivo na forma de string (usado para calcular TF)
            arquivos_idf: lista de nomes de arquivos, onde cada um é uma string
            (usado para calcular IDF)
        SAÍDA:
           Uma lista ordenada de tuplas (em ordem crescente da pontuação TF-IDF), 
           onde cada tupla tem a forma (palavra, TF-IDF). Se duas palavras tiverem
           o mesmo TF-IDF, devem ser armazenadas em ordem alfabética.


        * TF-IDF(i) = TF(i) * IDF(i)
        """
    tf = obter_tf(arquivo_tf) # obtém o TF do arquivo especificado
    idf = obter_idf(arquivos_idf) # obtém o IDF dos arquivos especificados

    tfidf = {} # inicializa um dicionário vazio para armazenar o TF-IDF de cada palavra
    for palavra in tf: # itera sobre cada palavra no dicionário de TF
        tfidf[palavra] = tf[palavra] * idf.get(palavra, 0) # calcula o TF-IDF da palavra e armazena no dicionário

    lista_tuplas = list(tfidf.items()) # converte o dicionário de TF-IDF em uma lista de tuplas (palavra, TF-IDF)
    lista_tuplas.sort(key=lambda x: (x[1], x[0])) # ordena a lista de tuplas primeiro pelo valor TF-IDF e depois alfabeticamente pela palavra

    return lista_tuplas # retorna a lista ordenada de tuplas


if __name__ == "__main__":
    pass
    ###############################################################
    ## Descomente as linhas abaixo para testar a implementação   ## ESSA PARTE JA ME FOI PASSADO PRONTA FIZ APENAS UMAS MUDANÇAS NA PARTE DE DIRETORIO_TESTE E tf_arquivo
    ###############################################################

    ## Teste do Problema 0: Preparar dados
    diretorio_teste = "C:/Users/Rafa/OneDrive/Área de Trabalho/trabalho2/testes/testes_estudantes" + "/" # 
    ola_mundo, ola_amigo = carregar_arquivo(diretorio_teste + 'ola_mundo.txt'), carregar_arquivo(diretorio_teste + 'ola_amigos.txt')
    mundo, amigo = texto_para_lista(ola_mundo), texto_para_lista(ola_amigo)
    print(mundo)      # Deve imprimir ['olá', 'mundo', 'olá']
    print(amigo)     # Deve imprimir ['olá', 'amigos']

    ## Testes Problema 1: Obter frequências
    diretorio_teste = "C:/Users/Rafa/OneDrive/Área de Trabalho/trabalho2/testes/testes_estudantes" + "/"
    ola_mundo, ola_amigo = carregar_arquivo(diretorio_teste + 'ola_mundo.txt'), carregar_arquivo(diretorio_teste + 'ola_amigos.txt')
    mundo, amigo = texto_para_lista(ola_mundo), texto_para_lista(ola_amigo)
    freq_mundo_mundo = obter_frequencia(mundo)
    freq_amigo_mundo = obter_frequencia(amigo)
    print(freq_mundo_mundo)    # Deve imprimir {'olá': 2, 'mundo': 1}
    print(freq_amigo_mundo)   # Deve imprimir {'olá': 1, 'amigos': 1}

    # Testes Problema 2: Frequencia de letras
    freq1 = obter_frequencia_letras('berro')
    freq2 = obter_frequencia_letras('sois')
    print(freq1)      #  Deve imprimir {'b': 1, 'e': 1, 'r': 2, 'o': 1}
    print(freq2)      #  Deve imprimir {'s': 2, 'o': 1, 'i': 1}

    ## Testes Problema 3: Similaridade
    diretorio_teste = "C:/Users/Rafa/OneDrive/Área de Trabalho/trabalho2/testes/testes_estudantes" + "/"
    ola_mundo, ola_amigo = carregar_arquivo(diretorio_teste + 'ola_mundo.txt'), carregar_arquivo(diretorio_teste + 'ola_amigos.txt')
    mundo, amigo = texto_para_lista(ola_mundo), texto_para_lista(ola_amigo)
    freq_mundo_mundo = obter_frequencia(mundo)
    freq_amigo_mundo = obter_frequencia(amigo)
    freq_palavra1 = obter_frequencia_letras('pato')
    freq_palavra2 = obter_frequencia_letras('sois')
    freq_palavra3 = obter_frequencia('nuh')
    similaridade_palavra1 = calcula_pontuacao_similaridade(freq_palavra1, freq_palavra1)
    similaridade_palavra2 = calcula_pontuacao_similaridade(freq_palavra1, freq_palavra2)
    similaridade_palavra3 = calcula_pontuacao_similaridade(freq_palavra1, freq_palavra3)
    similaridade_palavra4 = calcula_pontuacao_similaridade(freq_mundo_mundo, freq_amigo_mundo)
    print(similaridade_palavra1)       # Deve imprimir 1.0
    print(similaridade_palavra2)       # Deve imprimir 0.25
    print(similaridade_palavra3)       # Deve imprimir 0.0
    print(similaridade_palavra4)       # Deve imprimir 0.4

    ## Testes Problema 4: Palavras mais comuns
    freq_dic1, freq_dic2 = {"ola": 5, "mundo": 1}, {"ola": 1, "mundo": 5}
    mais_frequente = palavras_mais_frequentes(freq_dic1, freq_dic2)
    print(mais_frequente)      # Deve imprimir ["mundo", "ola"]

    ## Testes Problema 5: Encontre TF-IDF
    tf_arquivo = diretorio_teste + 'ola_mundo.txt'
    idf_arquivos = [diretorio_teste + 'ola_mundo.txt', diretorio_teste + 'ola_amigos.txt']
    tf = obter_tf(tf_arquivo)
    idf = obter_idf(idf_arquivos)
    tf_idf = obter_tfidf(tf_arquivo, idf_arquivos)
    print(tf)     # Deve imprimir {'ola': 0.6666666666666666, 'mundo': 0.3333333333333333}
    print(idf)    # Deve imprimir {'ola': 0.0, 'mundo': 0.3010299956639812, 'amigos': 0.3010299956639812}
    print(tf_idf) # Deve imprimir [('ola', 0.0), ('mundo', 0.10034333188799373)]
