import random
import time

#1
lista = []

for i in range(10):
    numero = random.randint(1, 100)
    lista.append(numero)

print("Lista gerada:")
print(lista)

#2
lista = []

for i in range(3):
    numero = int(input("Digite um número: "))
    lista.append(numero)

print("Lista:")
print(lista)

#3
frase = input("Digite uma frase: ")

lista = frase.split()

print("Lista de palavras:")
print(lista)

#4
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista.reverse()
print(lista)

#5
palavras = ["casa", "computador", "sol", "brotschneidenmaschine", "janela"]

maior = palavras[0]
menor = palavras[0]

for palavra in palavras:
    if len(palavra) > len(maior):
        maior = palavra

    if len(palavra) < len(menor):
        menor = palavra

print("Palavra mais longa:", maior)
print("Palavra mais curta:", menor)

#6
pares = []
impares = []

for i in range(1, 11):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

lista = pares + impares

print("Pares:", pares)
print("Ímpares:", impares)
print("Lista completa:", lista)

#7
lista = []

for i in range(1, 101):
    lista.append(i)

for numero in lista:
    if numero % 2 == 0:
        print(numero)
        time.sleep(0.2)

#8
lista = []
soma = 0

for i in range(1, 11):
    quadrado = i ** 2
    lista.append(quadrado)

for numero in lista: #numero vai receber cada valor que estiver na lista
    soma += numero

print("Lista:", lista)
print("Soma:", soma)

#9
letras = list("abcdefghijklmnopqrstuvwxyz")

random.shuffle(letras)

print(letras)

letra = input("Digite uma letra: ").lower()

while len(letra) != 1 or not letra.isalpha(): #para ver se há apenas uma letra ou se há de fato uma letra
    letra = input("Digite apenas UMA letra, sem números ou qualquer outro caractere: ").lower()

posicao = int(input("Digite a posição da letra: "))

if letras[posicao] == letra:
    print("Acertou!")
else:
    print("Errou!")
    print("A letra estava na posição:", letras.index(letra))

#10
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

jogador = "X"

for i in range(9):


    for linha in tabuleiro:
        print(linha)

    print("Jogador:", jogador)

    l = int(input("Linha: "))
    c = int(input("Coluna: "))


    if tabuleiro[l][c] == " ":
        tabuleiro[l][c] = jogador
    else:
        print("Lugar ocupado!")
        continue


    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] != " ":
        print(jogador, "venceu!")
        break

    elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] != " ":
        print(jogador, "venceu!")
        break

    elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] != " ":
        print(jogador, "venceu!")
        break


    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"
