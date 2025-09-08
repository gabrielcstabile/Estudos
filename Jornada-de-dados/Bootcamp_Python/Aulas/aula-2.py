# Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo

try:
    n1: int = int(input("Insira um nº inteiro: "))
    n2: int = int(input("Insira o 2º nº inteiro: "))
    resultado: int = n1 // n2
    print (resultado)
except ZeroDivisionError:
    print("Não pode dividir um número por zero.")
except KeyboardInterrupt:
            print("\n Operação cancelada pelo usuário (Ctrl + C).")
            exit(1)  
except TypeError as e:
       print(e)