# 1. Criar e imprimir uma matriz 3x3
M = []
for l in range (3):
    L = []
    for c in range(3):
        valor = int(input(f"Digite o valor para [{l}] [{c}]: "))
        L.append(valor)
    M.append(L)

print("\nMatriz: ")
for L in M:
    for valor in L:
        print(f"[{valor}]", end="")
    print()

# 2. Soma de todos os elementos
M = []
for l in range(3):
    L= []
    for c in range(3):
        valor = int(input(f"Digite o valor para [{l}] [{c}]: "))
        L.append(valor)
    M.append(L)

soma = 0
for L in M:
    for valor in L:
        soma += valor

print(f"Soma dos elementos: {soma}")

# 3. Encontrar o maior número
M = []
for l in range(3):
    L = []
    for c in range(3):
        valor = int(input(f"Digite o valor para [{l}] [{c}]: "))
        L.append(valor)
    M.append(L)

maior = M[0][0]
for L in M:
    for valor in L:
        if valor > maior:
            maior = valor 

print(f"Maior valor: {maior}")

# 4. Contar números pares
M = []
for l in range(3):
    L = []
    for c in range(3):
        valor = int(input(f"Digite o valor para [{l}] [{c}]: "))
        L.append(valor)
    M.append(L)

pares = 0
for L in M:
    for valor in L:
        if valor % 2 == 0:
            pares += 1

print(f"Quantidade de números pares: {pares}")

# 5. Soma de cada linha
M = []
for l in range(3):
    L = []
    for c in range(3):
        valor = int(input(f"Digite o valor para [{l}] [{c}]: "))
        L.append(valor)
    M.append(L)

print("\nSoma de cada linha: ")
soma = 0
for l in range(3):
    for c in range(3):
        soma += M[l][c]
    print(f"Soma da linha {l}: {soma}")

# 6. Soma de cada coluna
M = []
for l in range(3):
    L = []
    for c in range(3):
        valor = int(input(f"Digite o valor para [{l}] [{c}]: "))
        L.append(valor)
    M.append(L)

print("\nSoma de cada coluna:")
for c in range(3):
    soma = 0
    for l in range(3):
        soma += M[l][c]
    print(f"Soma da coluna {c}: {soma}")

# 7. Mostrar os elementos da diagonal principal
M = []
for l in range(3):
    L = []
    for c in range(3):
        valor = int(input(f"Digite o valor para [{l}] [{c}]: "))
        L.append(valor)
    M.append(L)

print("\nElementos da diagonal principal: ")
for l in range(3):
    for c in range(3):
        if l == c:
            print(f"[{M[l][c]}]", end=" ")
    print()

# 8. Soma da diagonal principal
M = []
for l in range(3):
    L = []
    for c in range(3):
        valor = int(input(f"Digite o valor para [{l}] [{c}]: "))
        L.append(valor)
    M.append(L)

soma = 0 
for l in range(3):
    for c in range(3):
        if l == c:
            soma += M[l][c]
print(f"Soma da diagonal principal: {soma}")

# 9. Multiplicar todos os elementos por um número
M = []
for l in range(3):
    L = []
    for c in range(3):
        valor = int(input(f"Digite o valor para [{l}] [{c}]: "))
        L.append(valor)
    M.append(L)

print("\nMatriz inicial: ")
for L in M:
    for valor in L:
        print(f"[{valor}]", end=" ")
    print()

numero = int(input("Digite um número para multiplicar: "))
for l in range(3):
    for c in range(3):
        M[l][c] *= numero

print("\nMatriz multiplicada: ")
for L in M:
    for valor in L:
        print(f"[{valor}]", end=" ")
    print()

# 10. Procurar um número na matriz e mostrar sua posição
M = []
for l in range(3):
    L = []
    for c in range(3):
        valor = int(input(f"Digite o valor para [{l}] [{c}]: "))
        L. append(valor)
    M.append(L)

numero_procurado = int(input("Digite o número que deseja procurar: "))

encontrado = False

for l in range(3):
    if numero_procurado in M[l]:
        for c in range(3):
            if M[l][c] == numero_procurado:
                print(f"O número {numero_procurado} foi encontrado na posição [{l}] [{c}]")
                encontrado = True
if not encontrado:
    print("Número não encontrado.")