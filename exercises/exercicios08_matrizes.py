# 1
# matriz = []

# for l in range(5):
#     L = []
#     for c in range(5):
#         if l == c:
#             L.append(1)
#         else:
#             L.append(0)
#     matriz.append(L)

# print(matriz)
# print()

# for l in matriz:
#     print(l)


# 2
# matriz = []

# for l in range(4):
#     L = []
#     for c in range(4):
#         valor = int(input(f"Digite o valor para [{l}] [{c}]: "))
#         L.append(valor)
#     matriz.append(L)

# maior = matriz[0][0]
# l_maior = 0
# c_maior = 0

# for l in range(4):
#     for c in range(4):

#         if matriz[l][c] > maior:
#             maior = matriz[l][c]
#             l_maior = l
#             c_maior = c

# print("\nMatriz: ")

# for l in matriz:
#     print(l)

# print(f"\nMaior valor: {maior}")
# print(f"linha: {l_maior}")
# print(f"Coluna: {c_maior}")

# 3 -> assumindo que há apenas UMA maior nota
matriz = []

for l in range(5):
    aluno = []

    matricula = int(input("Digite o número da matrícula: "))
    aluno.append(matricula)

    media_provas = float(input("Digite a média das provas: "))
    aluno.append(media_provas)

    media_trabalhos = float(input("Digite a média dos trabalhos: "))
    aluno.append(media_trabalhos)

    nota_final = media_trabalhos + media_provas
    aluno.append(nota_final)

    # Adicionar o aluno na matriz
    matriz.append(aluno)


maior_nota = matriz[0][3]
matricula_maior = matriz[0][0]

for l in range(5):
    if matriz [l][3] > maior_nota:
        maior_nota = matriz[l][3]
        matricula_maior = matriz[l][0]

print("\nTabela de alunos")

for l in matriz:
    print(l)

print(f"\nMaior nota final: {maior_nota}")
print(f"Matrícula do aluno: {matricula_maior}")