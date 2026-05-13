#1
'''contador = 0

for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print(i)
        contador += 1

print(f"Quantidade de números: {contador}")'''

n = 0

while True:
        n = int(input("Digite um número inteiro positivo: "))
        if n > 0:
            break
        else:
            print("Número inválido! Digite um valor positivo.")

soma = 0
expressao = ""

for i in range(1, n + 1):
    soma += i
    
    if i == n:
        expressao += str(i)
    else:
        expressao += str(i) + " + "

# Resultado final
print(f"{expressao} = {soma}")
