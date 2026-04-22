"""
Segundo projeto de Fundamentos de Programação
David Gabriel Silva Santos
ist1107192
david.s.santos@tecnico.ulisboa.pt
10/11/2022
"""


def cria_gerador(b, s):
    """
    :param b: número inteiro positivo correspondente número de bits do gerador (32 ou 64)
    :param s: número inteiro positivo correspondente à seed ou estado inicial do gerador
    :return: gerador: lista contendo o número de bits e a seed
    Autor: David Santos
    """
    if not (isinstance(b, int) and isinstance(s, int) and s > 0 and (b == 64 or b == 32)):
        raise ValueError('cria_gerador: argumentos invalidos')
    elif (b == 32 and s > 0xFFFFFFFF) or (b == 64 and s > 0xFFFFFFFFFFFFFFFF):
        raise ValueError('cria_gerador: argumentos invalidos')
    return [s, b]


def cria_copia_gerador(g):
    """
    :param g: gerador
    :return: cópia do gerador
    Autor: David Santos
    """
    return g + []


def obtem_estado(g):
    """
    :param g: gerador
    :return: seed ou estado do gerador
    Autor: David Santos
    """
    return g[0]


def define_estado(g, s):
    """
    :param g: gerador
    :param s: número inteiro
    :return: altera a seed ou estado do gerador para s e devolve s
    Autor: David Santos
    """
    g[0] = s
    return s


def atualiza_estado(g):
    """
    :param g: gerador
    :return: atualiza o estado inicial do gerador com um número pseudoaleaório
    gerado a partir de um algoritmo xorshift e devolve esse número
    Autor: David Santos
    """
    if g[1] == 32:
        g[0] ^= (g[0] << 13) & 0xFFFFFFFF
        g[0] ^= (g[0] >> 17) & 0xFFFFFFFF
        g[0] ^= (g[0] << 5) & 0xFFFFFFFF
    elif g[1] == 64:
        g[0] ^= (g[0] << 13) & 0xFFFFFFFFFFFFFFFF
        g[0] ^= (g[0] >> 7) & 0xFFFFFFFFFFFFFFFF
        g[0] ^= (g[0] << 17) & 0xFFFFFFFFFFFFFFFF
    return g[0]


def eh_gerador(arg):
    """"
    :param arg: argumento de entrada
    :return: True se o argumento de entrada correponde a um TAD gerador
    caso contrário False
    Autor: David Santos
    """
    return isinstance(arg, list) and len(arg) == 2 and type(arg[0]) \
           == type(arg[1]) == int and (arg[1] == 32 or arg[1] == 64)


def geradores_iguais(g1, g2):
    """
    :param g1: gerador
    :param g2: gerador
    :return: True se ambos os parâmetros de entrada forem TADs geradores e forem iguais,
    caso contrário devolve False
    Autor: David Santos
    """
    return eh_gerador(g1) and eh_gerador(g2) and g1 == g2


def gerador_para_str(g):
    """
    :param g: gerador
    :return: string descrevendo o tipo de algoritmo gerador de números, com o número de bits,
    e o estado
    Autor: David Santos
    """
    return 'xorshift%d(s=%d)' % (g[1], obtem_estado(g))


def gera_numero_aleatorio(g, n):
    """
    :param g: gerador
    :param n: número inteiro positivo
    :return: atualiza o estado do gerador e devolve um número pseudoaleatório entre 1 e o
    número inteiro positivo de entrada
    Autor: David Santos
    """
    atualiza_estado(g)
    return 1 + (obtem_estado(g) % n)


def gera_carater_aleatorio(g, c):
    """
    :param g: gerador
    :param c: letra de A a Z
    :return: carater pseudoaleatório entre A e o parâmetro de entrada c, gerado a partir
    da atualização do estado do gerador g
    Autor: David Santos
    """
    letras = [chr(i) for i in range(ord('A'), ord(c) + 1)] #lista das letras entre A e a string c
    tamanho = len(letras)
    atualiza_estado(g)
    estado = obtem_estado(g)
    return letras[estado % tamanho]
    #retorna a letra que se encontra na posição calculada pelo resto da divisão entre a seed e o tamanho da lista de letras


def cria_coordenada(col, lin):
    """
    :param col: letra entre A e Z representando a coluna de uma coordenada do campo
    :param lin: número inteiro entre 1 e 99 representando a linha de uma coordenada do campo
    :return: cordenada: tuplo de tamanho dois em que o primeiro e segundo elementos do tuplo
    correspondem à coluna e à linha do campo, respetivamente.
    Autor: David Santos
    """
    if not (isinstance(col, str) and isinstance(lin, int) and len(col) == 1 \
        and ord(col) >= 65 and ord(col) <= 90 and lin >= 1 and lin <= 99):
        raise ValueError('cria_coordenada: argumentos invalidos')
    return (col, lin)


def obtem_coluna(c):
    """
    :param c: coordenada
    :return: coluna da coordenada
    Autor: David Santos
    """
    return c[0]


def obtem_linha(c):
    """
    :param c: coordenada
    :return: linha da coordenada
    Autor: David Santos
    """
    return c[1]


def eh_coordenada(arg):
    """
    :param arg: argumento de entrada
    :return: True se o argumento de entrada correponde ao TAD de uma coordenada,
    caso contrário devolve False
    Autor: David Santos
    """
    return isinstance(arg, tuple) and len(arg) == 2 and isinstance(arg[0], str) and \
           isinstance(arg[1], int) and len(arg[0]) == 1 and ord(arg[0]) >= 65 and \
           ord(arg[0]) <= 90 and arg[1] >= 1 and arg[1] <= 99


def coordenadas_iguais(c1, c2):
    """
    :param c1: coordenada
    :param c2: coordenada
    :return: True se ambas coordenadas corresponderem ao TAD de uma coordenada e forem
    iguais, caso contrário devolve False
    Autor: David Santos
    """
    return eh_coordenada(c1) and eh_coordenada(c2) and c1 == c2


def coordenada_para_str(c):
    """
    :param c: coordenada
    :return: TAD coordenada transformada em string da seguinte forma:
    <string da coordenada> ::= <coluna> 0 <linha>|<coluna> <linha>
    Autor: David Santos
    """
    if obtem_linha(c) < 10:
        return ("%s0%d" % (obtem_coluna(c), obtem_linha(c)))
    else:
        return ('%s%d' % (obtem_coluna(c), obtem_linha(c)))


def str_para_coordenada(s):
    """
    :param s: string na forma <string da coordenada> ::= <coluna> 0 <linha>|<coluna> <linha>
    :return: TAD coordenada
    Autor: David Santos
    """
    if s[1] == '0':
        lin = int(s[2])
    else:
        lin = int(s[1:])
    return cria_coordenada(s[0], lin)


def c_cima(c):
    """
    :param c: coordenada
    :return: lista de tuplos com informação sobre as colunas
    e linhas acima da coordenada de entrada
    Autor: David Santos
    """
    linha = obtem_linha(c) - 1
    coluna = obtem_coluna(c)
    return [(chr(ord(coluna) - 1), linha), \
            (coluna, linha), (chr(ord(coluna) + 1), linha)]


def c_direita(c):
    """
    :param c: coordenada
    :return: lista de tuplos com informação sobre a coluna
    e a linha à direita da coordenada de entrada
    Autor: David Santos
    """
    return [(chr(ord(obtem_coluna(c)) + 1), obtem_linha(c))]


def c_baixo(c):
    """
    :param c: coordenada
    :return: lista de tuplos com informação sobre as colunas
    e linhas abaixo da coordenada de entrada
    Autor: David Santos
    """
    linha = obtem_linha(c) + 1
    coluna = obtem_coluna(c)
    return [(chr(ord(coluna) + 1), linha), \
            (coluna, linha), (chr(ord(coluna) - 1), linha)]


def c_esquerda(c):
    """
    :param c: coordenada
    :return: lista de tuplos com informação sobre a coluna
    e a linha à esquerda da coordenada de entrada
    Autor: David Santos
        """
    return [(chr(ord(obtem_coluna(c)) - 1), obtem_linha(c))]


def obtem_coordenadas_vizinhas(c):
    """
    :param c: coordenada
    :return: tuplo contendo as coordenadas à volta da coordenada de entrada pelo sentido horário
    Autor: David Santos
    """
    coordenadas = c_cima(c) + c_direita(c) + c_baixo(c) + c_esquerda(c)
    #lista de tuplos contendo toda a informação sobre as colunas e linhas à volta da coordenada de entrada
    #quer a informação seja válida ou não
    final = ()
    for i in coordenadas:
        try:
            final += (cria_coordenada(i[0], i[1]),)
            #cria as coordenadas vizinhas a partir da lista de tuplos 'coordenadas' filtrando os elementos da lista que não forem válidos
            #adiciona as coordenadas vizinhas ao tuplo de output
        except ValueError:
            del i
    return final


def obtem_coordenada_aleatoria(c, g):
    """
    :param c: coordenada
    :param g: gerador
    :return: coordenada aleatória resultado do geramento de uma coluna pseudoaleatória e de uma linha
    pseudoaleatória.
    Autor: David Santos
    """
    col = gera_carater_aleatorio(g, obtem_coluna(c))
    lin = gera_numero_aleatorio(g, obtem_linha(c))
    return cria_coordenada(col, lin)


def cria_parcela():
    """
    :return: parcela: lista de strings de tamanho dois em que a primeira string corresponde ao estado dessa
    parcela (tapada, limpa, ou marcada), começando com tapada, e a segunda corresponde à existência ou não de
    minas nessa parcela (com mina ou sem mina), começando sem mina.
    Autor: David Santos
    """
    return ['tapada', 'sem mina']


def cria_copia_parcela(p):
    """
    :param p: parcela
    :return: cópia da parcela
    Autor: David Santos
    """
    return p + []


def limpa_parcela(p):
    """
    :param p: parcela
    :return: muda o estado da parcela para limpa, e devolve a parcela
    Autor: David Santos
    """
    p[0] = 'limpa'
    return p


def marca_parcela(p):
    """
    :param p: parcela
    :return: muda o estado da parcela para marcada, e devolve a parcela
    Autor: David Santos
    """
    p[0] = 'marcada'
    return p


def desmarca_parcela(p):
    """
    :param p: parcela
    :return: muda o estado da parcela para tapada, e devolve a parcela
    Autor: David Santos
    """
    p[0] = 'tapada'
    return p


def esconde_mina(p):
    """
    :param p: parcela
    :return: altera o estado de existência ou não de mina da parcela para 'com mina'
    e devolve  a parcela.
    Autor: David Santos
    """
    p[1] = 'com mina'
    return p


def eh_parcela(arg):
    """
    :param arg: argumento de entrada
    :return: True se o argumento de entrada correponde a um TAD parcela, caso contrário
    devolve False
    Autor: David Santos
    """
    return isinstance(arg, list) and len(arg) == 2 and \
           type(arg[0]) == type(arg[1]) == str and (arg[0] == 'tapada' \
           or arg[0] == 'marcada' or arg[0] == 'limpa') and (arg[1] == \
           'sem mina' or arg[1] == 'com mina')


def eh_parcela_tapada(p):
    """
    :param p: parcela
    :return: True se a parcela corresponde a um TAD parcela e se o seu estado for tapada,
    caso contrário devolve False
    Autor: David Santos
    """
    return eh_parcela(p) and p[0] == 'tapada'


def eh_parcela_marcada(p):
    """
    :param p: parcela
    :return: True se a parcela corresponde a um TAD parcela e se o seu estado for marcada,
    caso contrário devolve False
    Autor: David Santos
    """
    return eh_parcela(p) and p[0] == 'marcada'


def eh_parcela_limpa(p):
    """
    :param p: parcela
    :return: True se a parcela corresponde a um TAD parcela e se o seu estado for limpa,
    caso contrário devolve False
    Autor: David Santos
    """
    return eh_parcela(p) and p[0] == 'limpa'


def eh_parcela_minada(p):
    """
    :param p: parcela
    :return: True se a parcela corresponde a um TAD parcela e se o seu estado for marcada,
    caso contrário devolve False
    Autor: David Santos
    """
    return eh_parcela(p) and p[1] == 'com mina'


def parcelas_iguais(p1, p2):
    """
    :param p1: parcela
    :param p2: parcela
    :return: True se ambas as parcelas coorrespondem a TADs parcela e se forem parcelas iguais,
    caso contrário devolve False
    Autor: David Santos
    """
    return eh_parcela(p1) and eh_parcela(p2) and p1 == p2


def parcela_para_str(p):
    """
    :param p: parcela
    :return: símbolo correspondente ao estado da parcela:
            - '#' se a parcela for tapada
            - '@' se a parcela for marcada
            - '?' se a parcela for limpa e sem mina
            - 'X' se a parcela for limpa e com mina
    Autor: David Santos
    """
    if eh_parcela_tapada(p):
        return '#'
    elif eh_parcela_marcada(p):
        return '@'
    elif eh_parcela_limpa(p) and not eh_parcela_minada(p):
        return '?'
    elif eh_parcela_limpa(p) and eh_parcela_minada(p):
        return 'X'


def alterna_bandeira(p):
    """
    :param p: parcela
    :return: se a parcela for marcada desmarca a parcela e se for tapada marca a parcela devolvendo True
    para estes dois casos. Caso nenhum destes casos se verifique, não muda o estado da percela e devolve
    False.
    Autor: David Santos
    """
    if eh_parcela_marcada(p):
        desmarca_parcela(p)
        return True
    elif eh_parcela_tapada(p):
        marca_parcela(p)
        return True
    return False


def cria_campo(c, l):
    """
    :param c: número inteiro positivo correspondente à última coluna do campo
    :param l: número inteiro positivo correspondente à última linha do campo
    :return: campo: dicionário com comprimento igual à área do campo. Cada chave
    do dicionário corresponde a uma coordenada do campo e respetivos valores à
    parcela associada a essa coordenada.
    Autor: David Santos
    """
    if not (isinstance(c, str) and isinstance(l, int) and len(c) == 1 \
            and ord(c) >= 65 and ord(c) <= 90 and l >= 1 and l <= 99):
        raise ValueError('cria_campo: argumentos invalidos')
    campo = {cria_coordenada(chr(j), i): cria_parcela() for i in range(1, l + 1) for j in range(65, ord(c) + 1)}
    return campo


def coordenadas(m):
    """
    :param m: campo
    :return: lista com todas as coordenadas do campo
    Autor: David Santos
    """
    return [i for i in m.keys()]


def cria_copia_campo(m):
    """
    :param m: campo
    :return: cópia do campo
    Autor: David Santos
    """
    return {i: cria_copia_parcela(v) for i in m.keys() for v in m.values()}


def obtem_ultima_coluna(m):
    """
    :param m: campo
    :return: última coluna do campo
    Autor: David Santos
    """
    return obtem_coluna(coordenadas(m)[-1])


def obtem_ultima_linha(m):
    """
    :param m: campo
    :return: última linha do campo
    Autor: David Santos
    """
    return obtem_linha(coordenadas(m)[-1])


def obtem_parcela(m, c):
    """
    :param m: campo
    :param c: coordenada
    :return: parcela associada à coordenada de entrada no campo de entrada
    Autor: David Santos
    """
    return m[c]


def obtem_coordenadas(m, s):
    """
    :param m: campo
    :param s: string: 'limpas', 'tapadas', 'marcadas' ou 'minadas'
    :return: tuplo com todas as coordenadas do campo cujas parcelas
    são limpas ou tapadas ou marcadas ou minadas, dependendo do valor de s,
    em ordem ascendente de esquerda à direita e de cima a baixo das parcelas
    Autor: David Santos
    """
    c = coordenadas(m)
    if s == 'limpas':
        return tuple([i for i in c if eh_parcela_limpa(obtem_parcela(m, i))])
    elif s == 'tapadas':
        return tuple([i for i in c if eh_parcela_tapada(obtem_parcela(m, i))])
    elif s == 'marcadas':
        return tuple([i for i in c if eh_parcela_marcada(obtem_parcela(m, i))])
    elif s == 'minadas':
        return tuple([i for i in c if eh_parcela_minada(obtem_parcela(m, i))])


def obtem_numero_minas_vizinhas(m, c):
    """
    :param m: campo
    :param c: coordenada
    :return: númro de coordenadas vizinhas à coordenada de entrada cujas parcelas têm mina,
    no campo de entrada
    Autor: David Santos
    """
    total_vizinhas = obtem_coordenadas_vizinhas(c)
    actual_vizinhas = [i for i in total_vizinhas if i in coordenadas(m)]
    #lista de todas as coordenadas vizinhas à coordenada c que pertencem ao campo
    c_minadas = obtem_coordenadas(m, 'minadas')
    return len([i for i in actual_vizinhas if i in c_minadas])
    #tamanho da lista formada por todas as coordenadas vizinhas de c cujas parcelas são minadas


def eh_campo(arg):
    """
    :param arg: argumento de entrada
    :return: True se o argumento de entrada corresponde a um TAD campo, caso contrário devolve False
    Autor: David Santos
    """
    return isinstance(arg, dict) and len(arg) > 0 and len([i for i in arg.keys()]) == \
    len([j for j in arg.values()]) == sum([eh_coordenada(i) for i in arg.keys()]) ==\
    sum([eh_parcela(j) for j in arg.values()])
    #Nas verificações que usam a função sum, está-se a usar uma lista que percorre todas as chaves do argumento de entrada
    #e outra lista que percorre todos os valores do argumento de entrada e devolve True ou False como elemento de cada uma
    #dessas listas de acordo com a função reconhecedora utilizada. Utilizar a função sum em cada uma dessas listas é equivalente
    #a contar quantos True é que essa lista tem. É verificada, assim, se todos os elementos de ambas as listas das chaves e dos
    #valores são válidos


def eh_coordenada_do_campo(m, c):
    """
    :param m: campo
    :param c: coordenada
    :return: True se a coordenada de entrada corresponde a um TAD coordenada e se pertence à lista de coordenadas
    do campo de entrada, caso contrário devolve False
    Autor: David Santos
    """
    return eh_coordenada(c) and c in coordenadas(m)


def campos_iguais(m1, m2):
    """
    :param m1: campo
    :param m2: campo
    :return: True caso ambos os campos corresponderem a um TAD campo e se forem iguais, caso contrário
    devolve False
    Autor: David Santos
    """
    return eh_campo(m1) and eh_campo(m2) and m1 == m2


def rodape(m):
    """
    :param m: campo
    :return: sequência de cruzes e traços
    (função auxiliar à função campo_para_str)
    Autor: David Santos
    """
    colunas = [chr(i) for i in range(65, ord(obtem_ultima_coluna(m)) + 1)]
    return '  +' + len(colunas) * '-' + '+'


def cabecario(m):
    """
    :param m: campo
    :return: cabeçário com sequência de letras correspondentes às colunas do campo
    (função auxiliar à função campo_para_str)
    Autor: David Santos
    """
    colunas = [chr(i) for i in range(65, ord(obtem_ultima_coluna(m)) + 1)]
    texto = ''
    for i in colunas:
        texto += i
    return '   %s\n%s\n' %(texto, rodape(m))


def opera_numero(i):
    """
    :param i: número inteiro positivo
    :return: string, <string> ::= 0 <i> | <i>
    (função auxiliar à função campo_para_str)
    Autor: David Santos
    """
    if i < 10:
        return '0%d' %(i)
    else:
        return str(i)


def campo_para_str(m):
    """
    :param m: campo
    :return: string correspondente à representação visual do campo
    Exemplo: campo com 5 colunas e 5 linhas:
    (' ABCDE\n +-----+\n01|#####|\n02|#####|\n03|#####|\n04|#####|\n05|#####|\n +-----+')
    Autor: David Santos
    """
    texto_final, u_linha, u_coluna = '', obtem_ultima_linha(m), obtem_ultima_coluna(m)
    for i in range(1, u_linha + 1):
        texto1 = ''
        for j in range(65, ord(u_coluna) + 1):
            coordenada = cria_coordenada(chr(j), i)
            parcela = obtem_parcela(m, coordenada)
            if eh_parcela_limpa(parcela) and not eh_parcela_minada(parcela):
                if obtem_numero_minas_vizinhas(m, coordenada) == 0:
                    elemento = ' '
                else:
                    elemento = str(obtem_numero_minas_vizinhas(m, coordenada))
            else:
                elemento = parcela_para_str(parcela)
            texto1 += elemento
        texto_final += '%s|%s|\n' % (opera_numero(i), texto1)
    return cabecario(m) + texto_final + rodape(m)


def coloca_minas(m, c, g, n):
    """
    :param m: campo
    :param c: coordenada
    :param g: gerador
    :param n: número inteiro positivo correspondante ao número de minas que o campo vai ter
    :return: campo com n coordenadas minadas geradas aleatoriamente pelo gerador, espalhadas pelo campo
    Autor: David Santos
    """
    vizinhas_e_c = [c] + [cor for cor in obtem_coordenadas_vizinhas(c) if eh_coordenada_do_campo(m, c)]
    while n > 0:
        minadas = obtem_coordenada_aleatoria(cria_coordenada(obtem_ultima_coluna(m), obtem_ultima_linha(m)), g)
        if minadas not in vizinhas_e_c and eh_coordenada_do_campo(m, minadas) and not eh_parcela_minada(obtem_parcela(m, minadas)):
            #se esta condição se verificar, é escondida uma mina nesta parcela e decrementa-se o valor de n para que, assim, o número
            #de vezes é escondida uma mina na parcela de uma coordenada que respeite estas condições seja igual a n
            esconde_mina(obtem_parcela(m, minadas))
            n = n - 1
    return m


def limpa_campo(m, c):
    """
    :param m: campo
    :param c: coordenada
    :return: campo com todas as parcelas limpas até chegar a uma coordenada em que pelo menos uma das suas
    vizinhas seja minada
    Autor: David Santos
    """
    if eh_parcela_limpa(obtem_parcela(m, c)):
        return m
    if not eh_parcela_marcada(obtem_parcela(m, c)):
        limpa_parcela(obtem_parcela(m, c))
    if obtem_numero_minas_vizinhas(m, c) == 0:
        t = [cor for cor in obtem_coordenadas_vizinhas(c) if eh_coordenada_do_campo(m, cor)]
        #lista com as coordenadas vizinhas à coordenada c que pertencem ao campo
        for cor in t:
            if eh_parcela_tapada(obtem_parcela(m, cor)):
                m = limpa_campo(m, cor)
    return m


def jogo_ganho(m):
    """
    :param m: campo
    :return: True se as condições do campo forem suficientes para que ocorra a vitória, caso contrário
    devolve False
    Autor: David Santos
    """
    area = obtem_ultima_linha(m) * (ord(obtem_ultima_coluna(m)) - ord('A') + 1)
    return area - len(obtem_coordenadas(m, 'limpas')) == len(obtem_coordenadas(m, 'minadas'))


def verifica_input(string):
    """
    :param string: coordenada em formato string
    :return: True se string for uma coordenada em formato string, caso contrário devolve False
    Autor: David Santos
    """
    if isinstance(string, str) and len(string) == 3 and ord(string[0]) >= 65 \
    and ord(string[0]) <= 90 and ord(string[1]) >= 48 and ord(string[1]) <= 57 and \
    ord(string[2]) >= 48 and ord(string[2]) <= 57:
        if string[1:] == '00':
            return False
        return True
    return False


def turno_jogador(m):
    """
    :param m: campo
    :return: marca ou limpa a parcela de uma coordenada, num campo de entrada, dependendo do input do jogador. Devolve
    True sempre que se marca uma parcela, e sempre que se limpa uma coordenada, se a parcela dessa coordenada não for
    minada, limpa-se o campo até chegar a uma coordenada minada e se a parcela da coordenada for minada, limpa essa
    parcela e devolve False.
    Autor: David Santos
    """
    acao = input('Escolha uma ação, [L]impar ou [M]arcar:')
    while not (acao == 'L' or acao == 'M'):
        acao = input('Escolha uma ação, [L]impar ou [M]arcar:')
    cor = input('Escolha uma coordenada:')
    while not verifica_input(cor):
        cor = input('Escolha uma coordenada:')
    while not eh_coordenada_do_campo(m, str_para_coordenada(cor)):
        cor = input('Escolha uma coordenada:')
    coordenada = str_para_coordenada(cor)
    if acao == 'M':
        alterna_bandeira(obtem_parcela(m, coordenada))
        return True
    elif acao == 'L':
        if eh_parcela_minada(obtem_parcela(m, coordenada)):
            limpa_parcela(obtem_parcela(m, coordenada))
            return False
        limpa_campo(m, coordenada)
        return True


def minas(c, l, n, d, s):
    """
    :param c: letra de A a Z correspondente à última coluna do campo
    :param l: número inteiro positivo correspondente à última linha do campo
    :param n: número inteiro positivo correspondente ao número de minas para o jogo
    :param d: dimensão do gerador (32 bits ou 64 bits)
    :param s: estado inicial do gerador

    Esta função cria um campo com os parâmetros de entrada c e l e cria um gerador para gerar n coordenadas
    minadas com os parâmetros de entrada d e s. Enquanto a condição de vitória não se verificar a função é turno_jogador
    será corrida e será mostrada a representação gráfica do campo de minas em cada turno até perder ou ganhar o jogo.

    :return: Se for limpa uma parcela com mina, perde-se o jogo e devolve False, se todas as parcelas limpas se encontram
    sem minas o jogo é ganho e devolve True
    Autor: David Santos
    """
    try:
        campo = cria_campo(c, l)
        g = cria_gerador(d, s)
    except ValueError:
        raise ValueError('minas: argumentos invalidos')
    n_coluna = ord(c) - ord('A') + 1
    if not (isinstance(n, int) and n >= 1 and n <= (n_coluna * l) - 9): #há no máximo 9 coordenadas vizinhas para cada coordenada
        raise ValueError('minas: argumentos invalidos')
        #o número de minas não pode ser maior que a diferença entre o produto do número de linhas com o número de colunas e 9
    print('   [Bandeiras %d/%d]\n%s' %(len(obtem_coordenadas(campo, 'marcadas')), n, campo_para_str(campo)))
    start = input('Escolha uma coordenada:')
    #input inicial para começar o jogo
    while not verifica_input(start):
        start = input('Escolha uma coordenada:')
    while not eh_coordenada_do_campo(campo, str_para_coordenada(start)):
        start = input('Escolha uma coordenada:')
    start = str_para_coordenada(start)
    coloca_minas(campo, start, g, n)
    limpa_campo(campo, start)
    if not jogo_ganho(campo):
        #não se verificam condições de vitória
        while not jogo_ganho(campo):
            print('   [Bandeiras %d/%d]\n%s' % (len(obtem_coordenadas(campo, 'marcadas')), n, campo_para_str(campo)))
            if turno_jogador(campo):
            # seguir para o turno seguinte se não for limpa nenhuma coordenada minada enquanto não existirem condições para a vitória
                continue
            print('   [Bandeiras %d/%d]\n%s\nBOOOOOOOM!!!' % (len(obtem_coordenadas(campo, 'marcadas')), n, campo_para_str(campo)))
            #se a condição acima não se verificar é porque foi limpa uma coordenada minada e BOOOOOOOOM derrota
            return False
    #já se verificam condições para a vitória
    print('   [Bandeiras %d/%d]\n%s\nVITORIA!!!' % (len(obtem_coordenadas(campo, 'marcadas')), n, campo_para_str(campo)))
    return True

if __name__ == "__main__":
    minas('Z', 5, 6, 32, 2)
