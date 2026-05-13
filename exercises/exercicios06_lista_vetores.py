import time

#1
A = [1, 0, 5, -2, -5, 7]

soma = A[0] + A[1] + A[5]
print(f"A soma inicialmente equivale a {soma}")

A[4] = 100

for i in range (6):
    print(A[i])

#2
valores = [0] * 6

for i in range (6):
   valores[i] = int(input("Digite um valor inteiro: "))

print("\nValores lidos: ")

for i in range (6):
    print(valores[i])

#3
numeros = [0] * 10
quadrados = [0] * 10

for i in range(10):
    numeros[i] = float(input("Digite um número real qualquer: "))
    quadrados[i] = numeros[i] ** 2

print("\nNúmeros escolhidos: ")

for i in range(10):
    print(numeros[i])
    time.sleep(0.2)

print("\nRespectivos quadrados: ")
for i in range(10):
    print(quadrados[i])
    time.sleep(0.2)

#4
vetor = [0] * 8

for i in range(8):
    vetor[i] = int(input("Digite um valor: "))

x = int(input("Digite a posição X: "))
y = int(input("Digite a posição Y: "))

soma = vetor[x] + vetor[y]

print("Soma:", soma)

#5
vetor2 = [0] * 10
pares = 0

for i in range(10):
    vetor2[i] = int(input("Digite um valor: "))

    if vetor2[i] % 2 == 0:
        pares += 1

print("Quantidade de valores pares: ", pares)

#6
vetor3 = [0] * 10

for i in range(10):
    vetor3[i] = int(input("Digite um valor: "))

maior = vetor3[0]
menor = vetor3[0]

for i in range(10):
    if vetor3[i] > maior:
        maior = vetor[i]

    if vetor3[i] < menor:
        menor = vetor[i]

print("Maior valor:", maior)
print("Menor valor:", menor)

#7
vetor4 = [0] * 10

for i in range(10):
    vetor4[i] = int(input("Digite um número: "))

maior = vetor4[0]
posicao = 0

for i in range(10):
    if vetor4[i] > maior:
        maior = vetor4[i]
        posicao = i

print("\nVetor:")
print(vetor4)

print("Maior elemento:", maior)
print("Posição do maior elemento:", posicao)

#8
notas = [0] * 15
soma = 0

for i in range(15):
    notas[i] = float(input("Insira a nota obtida: "))
    soma += notas[i]

media = soma / 15

print("\nA média geral é igual a:", media)

#9
vetor5 = [0] * 10
negativos = 0
soma_positivos = 0

for i in range(10):
    vetor5[i] = float(input("Digite um número: "))

    if vetor5[i] < 0:
        negativos += 1

    if vetor5[i] > 0:
        soma_positivos += vetor[i]

print("Quantidade de números negativos:", negativos)
print("Soma dos números positivos:", soma_positivos)

#10
valores2 = [0] * 5
soma = 0

for i in range(5):
    valores2[i] = float(input("Digite um valor: "))
    soma += valores2[i]

maior = valores2[0]
menor = valores2[0]

for i in range(5):
    if valores2[i] > maior:
        maior = valores2[i]

    if valores2[i] < menor:
        menor = valores2[i]

media = soma / 5

print("\nValores lidos:")
print(valores2)

print("Maior valor:", maior)
print("Menor valor:", menor)
print("Média:", media)

#11
valores3 = [0] * 5

for i in range(5):
    valores3[i] = float(input("Digite um valor: "))

maior = valores3[0]
menor = valores3[0]
pos_maior = 0
pos_menor = 0

for i in range(5):
    if valores3[i] > maior:
        maior = valores3[i]
        pos_maior = i

    if valores3[i] < menor:
        menor = valores3[i]
        pos_menor = i

print("Maior valor:", maior)
print("Posição do maior valor:", pos_maior)

print("Menor valor:", menor)
print("Posição do menor valor:", pos_menor)