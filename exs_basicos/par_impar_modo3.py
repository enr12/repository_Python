a = float(input("Digite um número: "))
# Não tem validação para letra
if a % 1 == 0:
    if a % 2 == 0:
        print("O número é par.")
    else:
        print("O número é impar.")
else:
    print("Não é um número inteiro.")
