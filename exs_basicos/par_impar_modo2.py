numero = input("Digite um número inteiro: ")

try:
    numero = int(numero)
    if (numero % 2) == 0:
        print("Número PAR")
    else:
        print("Número ÍMPAR")
except:
    print("Não foi digitado um número inteiro")
