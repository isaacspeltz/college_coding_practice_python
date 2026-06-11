import random
import time

linhas = 5
colunas = 10
quant_navios = 5

AGUA = '.'
NAVIO = '.'
ACERTO = 'X'
ERRO = 'O'


def digitar(texto):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()


def pausar(segundos=0.5):
    time.sleep(segundos)


def criar_tabuleiro():
    tabuleiro = []

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(AGUA)
        tabuleiro.append(linha)

    return tabuleiro


def mostrar_cabecalho():
    print(" ", end=" ")
    for c in range(colunas):
        print(c, end=" ")
    print()


def mostrar_tabuleiro(tabuleiro):
    i = 0
    for linha in tabuleiro:
        print(str(i), end=" ")
        for item in linha:
            print(item, end=" ")
        print()
        i += 1


def exibir_tabuleiros(tab_comp, navios_comp, tab_jogador, navios_jogador):
    digitar("\nTabuleiro do Computador")
    mostrar_cabecalho()
    mostrar_tabuleiro(tab_comp)
    print("-" * 34)
    digitar("Embarcacoes restantes: " + str(navios_comp))

    digitar("\nTabuleiro do Jogador")
    mostrar_cabecalho()
    mostrar_tabuleiro(tab_jogador)
    print("-" * 34)
    digitar("Embarcacoes restantes: " + str(navios_jogador))


def posicionar_jogador(tabuleiro):
    posicoes = []
    contador = 0

    while contador < quant_navios:
        try:
            linha = int(input("Embarcacao " + str(contador + 1) + " - Linha: "))
            coluna = int(input("Embarcacao " + str(contador + 1) + " - Coluna: "))
        except ValueError:
            digitar("Digite apenas numeros.")
            continue

        if linha < 0 or linha >= linhas:
            digitar("Linha invalida.")
            continue

        if coluna < 0 or coluna >= colunas:
            digitar("Coluna invalida.")
            continue

        if (linha, coluna) in posicoes:
            digitar("Posicao ocupada.")
            continue

        tabuleiro[linha][coluna] = NAVIO
        posicoes.append((linha, coluna))
        contador += 1

    return posicoes


def posicionar_computador(tabuleiro):
    posicoes = []
    contador = 0

    while contador < quant_navios:
        linha = random.randint(0, linhas - 1)
        coluna = random.randint(0, colunas - 1)

        if (linha, coluna) not in posicoes:
            tabuleiro[linha][coluna] = NAVIO
            posicoes.append((linha, coluna))
            contador += 1

    return posicoes


def ataque_jogador(tab_oculto, tab_exibicao, posicoes, atacadas):
    valido = False

    while valido == False:
        try:
            linha = int(input("Qual linha deseja atacar? "))
            coluna = int(input("Qual coluna deseja atacar? "))
        except ValueError:
            digitar("Digite apenas numeros.")
            continue

        if linha < 0 or linha >= linhas:
            digitar("Linha invalida.")
            continue

        if coluna < 0 or coluna >= colunas:
            digitar("Coluna invalida.")
            continue

        if (linha, coluna) in atacadas:
            digitar("Voce ja atacou essa posicao.")
            continue

        valido = True

    atacadas.add((linha, coluna))

    if (linha, coluna) in posicoes:
        posicoes.remove((linha, coluna))
        tab_oculto[linha][coluna] = AGUA
        tab_exibicao[linha][coluna] = ACERTO
        digitar("Acertou! Restam " + str(len(posicoes)) + " embarcacoes inimigas.")
    else:
        tab_exibicao[linha][coluna] = ERRO
        digitar("Errou!")


def ataque_computador(tab_oculto, tab_exibicao, posicoes, atacadas):
    valido = False

    while valido == False:
        linha = random.randint(0, linhas - 1)
        coluna = random.randint(0, colunas - 1)

        if (linha, coluna) not in atacadas:
            valido = True

    atacadas.add((linha, coluna))

    digitar("Computador escolheu a linha " + str(linha))
    digitar("Computador escolheu a coluna " + str(coluna))

    if (linha, coluna) in posicoes:
        posicoes.remove((linha, coluna))
        tab_oculto[linha][coluna] = AGUA
        tab_exibicao[linha][coluna] = ACERTO
        digitar("Computador acertou! Restam " + str(len(posicoes)) + " embarcacoes suas.")
    else:
        tab_exibicao[linha][coluna] = ERRO
        digitar("Computador errou!")


def jogar():
    tab_oculto_jogador = criar_tabuleiro()
    tab_oculto_comp = criar_tabuleiro()

    tab_exibicao_jogador = criar_tabuleiro()
    tab_exibicao_comp = criar_tabuleiro()

    posicoes_jogador = posicionar_jogador(tab_oculto_jogador)
    posicoes_comp = posicionar_computador(tab_oculto_comp)

    atacadas_jogador = set()
    atacadas_comp = set()

    turno = 0

    while len(posicoes_jogador) > 0 and len(posicoes_comp) > 0:
        exibir_tabuleiros(
            tab_exibicao_comp,
            len(posicoes_comp),
            tab_exibicao_jogador,
            len(posicoes_jogador)
        )

        if turno == 0:
            ataque_jogador(
                tab_oculto_comp,
                tab_exibicao_comp,
                posicoes_comp,
                atacadas_jogador
            )
            turno = 1
        else:
            ataque_computador(
                tab_oculto_jogador,
                tab_exibicao_jogador,
                posicoes_jogador,
                atacadas_comp
            )
            turno = 0

    if len(posicoes_comp) == 0:
        digitar("Parabens! Voce venceu!")
    else:
        digitar("O computador venceu!")


jogar()
