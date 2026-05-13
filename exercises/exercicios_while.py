=================================

'''numero = 1
while numero < 11:
    print(numero)
    numero += 1'''
    
=================================

'''numero = 10
while numero > 0:
    print(numero)
    numero -= 1'''

=================================

'''numero = int(input("Digite um número para obter sua tabuada: "))

if 1 <= numero <= 10:
    print(f"Tabuada do {numero}:")

    multiplicador = 0
    while multiplicador <= 10:
        r = numero * multiplicador
        print(f"{numero} * {multiplicador} = {r}")
        multiplicador += 1

else:
    print("Por favor, digite um número entre 1 e 10.")'''

=================================

'''palavra = input("Digite uma palavra (entre 3 e 10 letras): ")

while len(palavra) < 3 or len(palavra) > 10:
    print("Erro! A palavra deve ter entre 3 e 10 letras.")
    palavra = input("Digite novamente: ")

print("Palavra digitada:", palavra)
print("Quantidade de letras:", len(palavra))'''
        
=================================

'''nota = float(input("Insira a sua nota: "))

while nota < 0 or nota > 10:
    print("Nota inválida!")
    float(input("Tente novamente. Insira a sua nota: "))
    
print(f"Você tirou {nota}/10")'''

=================================

'''n = int(input("Digite um número inteiro n: "))

soma = 0
contador = 1

while contador <= n:
    soma =+ contador #vai adicionando o valor do contador na variável soma
    contador += 1 #vai aumentando o contador de 1 em 1, N vezes

print("Somatório: ", soma)'''

=================================


