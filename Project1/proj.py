#David Santos
#ist1107192
#david.s.santos@tecnico.ulisboa.pt
#Primeiro projeto de Fundamentos da Programação

# Exercício 1.

def limpa_texto(cadeia):
    """
    Esta função recebe uma cadeia de carateres, substitui todos os carateres
    ACSII por espaços em branco, e procede por substituir múltiplos espaços
    brancos consecutivos por apenas um. Por fim, remove os espaços em branco
    que possam estar no início e no final da cadeia, devolvendo um texto limpo.
    Autor: David Santos
    """
    cont, x, frase, carateres = 0, 0, "", '\t\n\v\f\r'
    while cont <= len(cadeia) - 1:
        frase += cadeia[cont]
        cont += 1
    while x <= len(frase) - 1:
        for i in carateres:
            if frase[x] == i:
                frase = frase.replace(frase[x], ' ')
        x += 1
    if '  ' in frase:
        while '  ' in frase:
            frase = frase.replace('  ', ' ')
    frase = frase.lstrip()
    frase = frase.rstrip()
    return frase


def corta_texto(cadeia, largura_coluna):
    """
    Esta função recebe uma cadeia de carateres limpa e
    devolve duas subcadeias de carateres limpas, separadas
    de acordo com a quantidade de carateres desde o início
    da cadeia até ao limite definido como largura da coluna.
    Autor: David Santos
    """
    if len(cadeia) == largura_coluna:
        return cadeia,
    l = cadeia.split()
    x, texto = 0, ''
    while x <= len(l) - 1:
        texto += str(l[x]) + ' '
        if len(texto) >= largura_coluna:
            break
        x += 1
    resultado = texto
    if len(resultado) > largura_coluna:
        result = resultado.replace(resultado.split()[-1], '')
    else:
        result = resultado
    resto = cadeia.replace(result.rstrip(), '')
    return (tuple((result.rstrip(), resto.lstrip())))


def insere_espacos(cadeia, largura_coluna):
    """
    Esta função recebe uma cadeia de carateres limpa e uma determinada
    largura de coluna e vai inserindo o número de espaços necessário à
    cadeia até que o seu comprimento seja igual à largura de coluna
    definida. Se o comprimento da cadeia introduzida for igual à largura
    de coluna pretendida, essa mesma cadeia é retornada sem espaços adi-
    cionais.
    Autor: David Santos
    """
    l, texto, length, cadeia1, cadeia2 = cadeia.split(), '', 0, (), ()
    if len(cadeia) == largura_coluna:
        return cadeia
    elif len(l) == 1 and len(cadeia) < largura_coluna:
        spaces_left = largura_coluna - len(cadeia)
        return (cadeia + spaces_left * ' ')
    elif len(l) == 2:
        for i in l:
            length += len(i)
        spaces_left = largura_coluna - length
        return (l[0] + spaces_left * ' ' + l[-1])
    elif len(cadeia) < largura_coluna and len(l) > 1:
        espaços_iniciais = len(l) - 1
        for i in l:
            length += len(i)
        spaces_needed = largura_coluna - length
        a, b = spaces_needed % espaços_iniciais, spaces_needed // espaços_iniciais
        if a != 0:
            for i in range(0, len(l) - 1):
                cadeia1 += (l[i] + b * ' ',)
            cadeia_final1 = cadeia1 + (l[-1],)
            restantes = spaces_needed - (espaços_iniciais * b)
            for x in range(0, restantes):
                cadeia2 += (cadeia1[x] + ' ',)
            cadeia_final = cadeia2 + cadeia_final1[x + 1:]
            for z in cadeia_final:
                texto += z
            return texto
        elif a == 0:
            for y in range(0, len(l) - 1):
                texto += l[y] + b * ' '
            cadeia_final = texto + l[-1]
            return (cadeia_final)


def justifica_texto(cadeia, largura_coluna):
    """
    Esta função recebe uma cadeia de carateres não vazia, limpa-a de todos
    carateres ASCII existentes e retorna a mesma cadeia cortada e espaçada
    segundo uma determinada largura de coluna. Se o comprimento da cadeia
    limpa for igual à largura de coluna definida, é retornada essa mesma
    cadeia.
    Autor: David Santos
    """
    if not (isinstance(cadeia, str) and isinstance(largura_coluna, int)):
        raise ValueError("justifica_texto: argumentos invalidos")
    if len(cadeia) == 0:
        raise ValueError("justifica_texto: argumentos invalidos")
    cadeia_limpa = limpa_texto(cadeia)
    if len(cadeia_limpa) == largura_coluna:
        return (cadeia_limpa)
    x = corta_texto(cadeia_limpa, largura_coluna)
    a, x1, texto_espaçado = (x[0],), (), ()
    while True:
        x = corta_texto(x[-1], largura_coluna)
        x1 += (x[0],)
        if x[0] == '':
            break
    cadeia_cortada = a + x1[:len(x1) - 1]
    for i in range(0, len(cadeia_cortada) - 1):
        texto_espaçado += (insere_espacos(cadeia_cortada[i], largura_coluna),)
    if len(cadeia_cortada[-1]) == largura_coluna:
        cadeia_justificada = texto_espaçado + cadeia_cortada[-1]
    elif len(cadeia_cortada[-1]) < largura_coluna:
        espaços_restantes = largura_coluna - len(cadeia_cortada[-1])
        cadeia_justificada = texto_espaçado + (str(cadeia_cortada[-1]) + espaços_restantes * ' ',)
    return cadeia_justificada


# Exercício 2.

def calcula_quocientes(info_piece, deputados):
    """
    Esta função recebe um dicionário, cujas chaves e valores,
    correspondem ao nome dos partidos e ao número de votos,
    respetivamente, num determinado território, e um número
    inteiro, que corresponde ao número de deputados desse
    território. Devolve um dicionário contendo as mesmas
    chaves do dicionário inicial, cada contendo uma lista com
    os quocientes calculados através do método de Hondt.
    Autor: David Santos
    """
    valores_quocientes, keys, tuplo_final = (), (), ()
    for i in info_piece.values():
        quocientes, divisor = [], 1
        while divisor <= deputados:
            divisões = i / divisor
            divisor += 1
            quocientes.append(divisões)
        valores_quocientes += (quocientes,)
    for l in info_piece.keys():
        keys += (l,)
    for l in range(0, len(info_piece)):
        tuplo_final += ((keys[l], valores_quocientes[l]),)
    final = dict(tuplo_final)
    return final


def retira_repetidos(lista):
    """
    Retira elementos repetidos de uma lista.
    Autor: David Santos
    """
    cont1 = 0
    while cont1 < (len(lista) - 1):
        cont2 = 0
        while cont2 < len(lista):
            if lista[cont1] == lista[cont2] and cont1 != cont2:
                del lista[cont2]
                cont2 -= 1
            cont2 += 1
        cont1 += 1
    return lista


def atribui_mandatos(info_piece, deputados):
    """
    Esta função recebe um dicionário com os votos apurados num
    determinado círculo eleitoral e devolve uma lista contendo
    os nomes dos partidos pela ordem que recebeu um mandato.
    Autor: David Santos
    """
    dic = calcula_quocientes(info_piece, deputados)
    partidos, votos, votos2, resultado, final = [], [], [], [], []
    for i, j in dic.items():
        partidos.append(i)
        votos.append(j)
    for i in votos:
        votos2.extend(i)
    votos2 = retira_repetidos(votos2)
    votos_ordenados = sorted(votos2, reverse=True)[:deputados]
    elementos = None
    for i in votos_ordenados:
        for j, k in enumerate(votos):
            if i in k:
                for x in range(0, len(votos)):
                    if i in votos[x] and k != votos[x]:
                        for y in enumerate(votos):
                            if k[0] > votos[x][0]:
                                elementos = y
                            elif k[0] < votos[x][0]:
                                elementos = j
                    else:
                        elementos = j
        resultado.append(elementos)
    for l in resultado:
        if l != None:
            final.append(partidos[l])
    return final


def obtem_partidos(info):
    """
    Esta função recebe um dicionário correspondente à informação
    sobre as eleições num território e devolve uma lista de todos
    os partidos que participaram nas eleições por ordem alfabética.
    Autor: David Santos
    """
    lista_inicial, partidos = [], []
    for i in info.values():
        for j in i.values():
            lista_inicial.append(j)
    for i in range(1, len(lista_inicial), 2):
        for j in (lista_inicial[i]):
            partidos.append(j)
    partidos = retira_repetidos(partidos)
    final = sorted(partidos)
    return (final)


def obtem_resultado_eleicoes(info):
    """
    Esta função recebe um dicionário com a informação sobre as eleições num
    território com vários círculos eleitorais. Retorna uma lista de tuplos
    em que cada tuplo contém o nome do partido, o número de deputados desse
    partido e o número total de votos que esse partido obteve por esta ordém.
    Cada tuplo dentro da lista está ordenado por ordem decrescente de deputados
    e caso haja mais do que um partido com o mesmo número de deputados, a ordenação
    é feita por ordem decrescente de votos.
    Autor: David Santos
    """
    if not isinstance(info, dict):
        raise ValueError("obtem_resultado_eleicoes: argumento invalido")
    elif len(info) == 0:
        raise ValueError("obtem_resultado_eleicoes: argumento invalido")
    for i, j in info.items():
        if len(j) != 2:
            raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        elif not (isinstance(i, str) and isinstance(j, dict)):
            raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        tuplo_key, tuplo_val = (), ()
        for k, l in j.items():
            tuplo_key += (k,)
            tuplo_val += (l,)
        if len(tuplo_key) != len(tuplo_val) != 2:
            raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        if tuplo_key[0] != 'deputados' or tuplo_key[1] != 'votos':
            raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        if not (isinstance(tuplo_val[0], int) and isinstance(tuplo_val[-1], dict)):
            raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        for m, n in tuplo_val[-1].items():
            if not (isinstance(m, str) and isinstance(n, int)):
                raise ValueError("obtem_resultado_eleicoes: argumento invalido")
    lista_deputados, lista_mandatos, soma_votos, resultado = [], [], [], []
    for i in info.values():
        lista_val = []
        for j in i.values():
            lista_val.append(j)
        lista_deputados.extend(atribui_mandatos(lista_val[-1], lista_val[0]))
    lista_ref = obtem_partidos(info)
    for i in lista_ref:
        lista_mandatos.append(lista_deputados.count(i))  # lista que contém o número de deputados por cada partido
    l, votos, total = (), (), ()
    for i in info.values():
        for j in i.values():
            l += (j,)
    for x in range(1, len(l), 2):
        votos += (l[x],)
    for i in lista_ref:
        lista_votos = []
        for j in votos:
            for k, l in j.items():
                if k == i:
                    lista_votos.append(l)
        total += (lista_votos,)
    for i in total:
        soma_votos.append(sum(i))  # lista que contém a soma total dos votos de cada partido
    fim, fim2 = len(lista_mandatos), len(soma_votos)
    while fim > 1:
        trocou = False
        x = 0
        while x < (fim - 1):
            if lista_mandatos[x] < lista_mandatos[x + 1]:  # ordenar por ordem decrescente de número de deputados
                trocou = True
                [lista_mandatos[x], lista_mandatos[x + 1]] = [lista_mandatos[(x + 1)], lista_mandatos[x]]
                [lista_ref[x], lista_ref[x + 1]] = [lista_ref[(x + 1)], lista_ref[x]]
                [soma_votos[x], soma_votos[x + 1]] = [soma_votos[(x + 1)], soma_votos[x]]
            x += 1
        if not trocou:
            break
        fim -= 1
    while fim2 > 1:
        trocou = False
        x = 0
        while x < (fim2 - 1):
            if lista_mandatos[x] == lista_mandatos[x + 1] and soma_votos[x] < soma_votos[\
                x + 1]:  # ordenar por ordem decrescente de número de votos
                trocou = True
                [soma_votos[x], soma_votos[x + 1]] = [soma_votos[(x + 1)], soma_votos[x]]
                [lista_mandatos[x], lista_mandatos[x + 1]] = [lista_mandatos[(x + 1)], lista_mandatos[x]]
                [lista_ref[x], lista_ref[x + 1]] = [lista_ref[(x + 1)], lista_ref[x]]
            x += 1
        if not trocou:
            break
        fim2 -= 1
    for x in range(0, len(lista_ref)):
        result = (lista_ref[x], lista_mandatos[x], soma_votos[x])
        resultado.append(result)
    return (resultado)


# Exercício 3.

def produto_interno(tuplo1, tuplo2):
    """
    Esta função recebe dois tuplos de reais e retorna
    o produto interno entre estes.
    Autor: David Santos
    """
    produto = 0
    for i in range(0, len(tuplo1)):
        produto += float(tuplo1[i] * tuplo2[i])
    return produto


def verifica_convergencia(A, C, x, precisao):
    """
    Esta função recebe 3 tuplos de igual dimensão e um real
    correspondentes à matriz de entrada, o vetor de constantes,
    a solução atual, e a precisão pretendida. Se, para todas as
    linhas da matriz , o valor absoluto da diferença do produto
    entre linha da matriz e a solução atual, com a mesma linha do
    vetor de constantes for menor que a precisão pretendida, a
    função retorna True. Caso contrário retorna False.
    Autor: David Santos
    """
    verdade = 0
    for i in range(0, len(A)):
        fxi = produto_interno(A[i], x)
        if bool(abs(fxi - C[i]) < precisao) == True:
            verdade += 1
    if verdade == len(A):
        return True
    else:
        return False


def retira_zeros_diagonal(A, C):
    """
    Esta função recebe dois tuplos correpondantes à matriz de entrada
    e ao vetor de constantes. Se a matriz recebida não tiver zeros nas
    diagonais, retorna a matriz e o vetor de constantes assim como estão.
    Caso contrário as linhas da matriz e do vetor de constantes serão
    trocadas até não haver mais zeros nas diagonais.
    Autor: David Santos
    """

    def nº_zeros_diagonal(A):
        zeros_diagonal = 0
        for i in range(0, len(A)):
            if A[i][i] == 0:
                zeros_diagonal += 1
        return zeros_diagonal

    if nº_zeros_diagonal(A) == 0:
        return (A, C)
    else:
        lista_A, lista_C = list(A), list(C)
        while nº_zeros_diagonal(lista_A) != 0:
            for i in range(0, len(A) - 1):
                lista_A[i], lista_A[i + 1] = lista_A[i + 1], lista_A[i]
                lista_C[i], lista_C[i + 1] = lista_C[i + 1], lista_C[i]
            A_final, C_final = tuple(lista_A), tuple(lista_C)
        return (A_final, C_final)


def eh_diagonal_dominante(A):
    """
    Esta função recebe um tuplo correspondente à matriz de entrada.
    Se, para todas as linhas da matriz, o valor absoluto da diagonal
    de uma determinada linha for maior ou igual à soma do módulo dos
    restantes valores da mesma linha, retorna True. Caso contrário,
    retorna False.
    Autor: David Santos
    """

    def soma_exceto_elemento(tuplo, indice):
        lista, soma = list(tuplo), 0
        lista.pop(indice)
        for i in lista:
            soma += abs(i)
        return (soma)

    acontece = 0
    for i in range(0, len(A)):
        if abs(A[i][i]) >= soma_exceto_elemento(A[i], i):
            acontece += 1
    if acontece == len(A):
        return True
    else:
        return False


def resolve_sistema(A, C, precisao):
    """
    Esta função recebe um dois tuplos correspondentes à matriz de entrada, A, e ao vetor
    de constantes, C, respetivamente e um número real correspondente à precisão do
    resultado. De seguida, esta função resolve a matriz, utilizando o método de Jacobi,
    e o algoritmo termina quando o erro das equações efetuadas for inferior à precisão
    inserida.
    Autor: David Santos
    """
    if not (isinstance(A, tuple) and isinstance(C, tuple) and isinstance(precisao, float)):
        raise ValueError("resolve_sistema: argumentos invalidos")
    for i in A:
        comprimento_linhas = len(i)
        if not isinstance(i, tuple):
            raise ValueError("resolve_sistema: argumentos invalidos")
        for l in i:
            if not (isinstance(l, int) or isinstance(l, float)):
                raise ValueError("resolve_sistema: argumentos invalidos")
        if comprimento_linhas != len(A):
            raise ValueError("resolve_sistema: argumentos invalidos")
    if len(C) != len(A):
        raise ValueError("resolve_sistema: argumentos invalidos")
    for y in C:
        if not (isinstance(y, int) or isinstance(y, float)):
            raise ValueError("resolve_sistema: argumentos invalidos")
    if eh_diagonal_dominante(A) is False:
        raise ValueError("resolve_sistema: matriz nao diagonal dominante")
    troca = retira_zeros_diagonal(A, C)
    matrix, constant = troca[0], troca[-1]
    x = []
    alcançe = len(matrix)
    for i in range(0, alcançe):
        x += [0]
    while verifica_convergencia(matrix, constant, tuple(x), precisao) is False:
        for l in range(0, alcançe):
            x[l] = x[l] + (constant[l] - produto_interno(matrix[l], tuple(x))) / matrix[l][l]
    resultado = tuple(x)
    return resultado
