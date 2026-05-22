def main():

    #=================================================== EXERCÍCIOS DO SLIDE ================================================================

    # # 1
    # def imprimir_nome():
    #     nome = input("Escreva o seu nome: ")
    #     print(nome)

    # imprimir_nome()

    # 2
    # def maior(a, b, c):
    #     if a >= b and a >= c:
    #         return a
    #     elif b >= a and b >= c:
    #         return b
    #     else:
    #         return c
        
    # resultado = maior(10, 25, 7)
    # print(resultado)

    # # 3
    # def criar_vetor():
    #     vetor = [0, 0, 0, 0, 0]
    #     return vetor
    
    # v = criar_vetor()
    # print(v)

    # # 4
    # def media(lista):
    #     soma = sum(lista)
    #     quantidade = len(lista)
    #     return soma / quantidade
    
    # numeros = [10, 20, 67, 40]
    # print(media(numeros))

    # # 5
    # def inverter(texto):
    #     print(texto[::-1])

    # inverter("Python")

    # # 6
    # def imprime_diagonal(matriz):
    #     for i in range(3):
    #         print(matriz[i][i])
    
    # matriz = [
    # [1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9]
    # ]

    # imprime_diagonal(matriz)

    #=================================================== EXERCÍCIOS 08 DO PDF ================================================================

    # # 1

    # def soma_elementos(lista):
    #     soma = 0

    #     for numero in lista:
    #         soma += numero

    #     return soma
    
    # valores = [1, 2, 3, 4, 5]
    # print(soma_elementos(valores))

    # # 2
    # def e_palindromo(texto):
    #     texto_invertido = texto[::-1]

    #     if texto == texto_invertido:
    #         return True
    #     else:
    #         return False
        
    # print(e_palindromo("arara"))
    # print(e_palindromo("python"))

    # # 3
    # def maior_elemento(lista):
    #     maior = lista[0]

    #     for numero in lista:
    #         if numero > maior:
    #             maior = numero

    #     return maior
    
    # valores = [3, 8, 6, 6767, 7]
    # print(maior_elemento(valores))

    # # 4
    # def contar_caracteres(texto, caractere):
    #     contador = 0

    #     for letra in texto:
    #         if letra == caractere:
    #             contador += 1

    #     return contador
    
    # print(contar_caracteres("brotschneidenmaschine", "e"))

    # # 5
    # def soma(a, b):
    #     return a + b


    # def subtracao(a, b):
    #     return a - b


    # def multiplicacao(a, b):
    #     return a * b


    # def divisao(a, b):
    #     if b == 0:
    #         return "Não é possível dividir por zero"
    #     return a / b


    # def menu():
    #     print("\n=== CALCULADORA ===")
    #     print("1 - Soma")
    #     print("2 - Subtração")
    #     print("3 - Multiplicação")
    #     print("4 - Divisão")
    #     print("5 - Sair")


    # def calculadora():
    #     while True:
    #         menu()

    #         opcao = input("Escolha uma opção: ")

    #         if opcao == "5":
    #             print("Encerrando a calculadora...")
    #             break

    #         num1 = float(input("Digite o primeiro número: "))
    #         num2 = float(input("Digite o segundo número: "))

    #         if opcao == "1":
    #             print("Resultado:", soma(num1, num2))

    #         elif opcao == "2":
    #             print("Resultado:", subtracao(num1, num2))

    #         elif opcao == "3":
    #             print("Resultado:", multiplicacao(num1, num2))

    #         elif opcao == "4":
    #             print("Resultado:", divisao(num1, num2))

    #         else:
    #             print("Opção inválida")
    
    # calculadora()

main()