numero = input("Digite um número inteiro: ")

if numero.isdecimal():
    numero = int(numero)
    if (numero % 2) == 0:
        print("Número PAR")
    else:
        print("Número ÍMPAR")
else:
    print("Não foi digitado um número inteiro")

