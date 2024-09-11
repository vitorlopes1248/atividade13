# Crie um programa que receba um número do usuário e informe se ele é positivo, negativo ou zero.

numero = int(input("digite seu numero: "))

if numero<=-1:
    print("O numero é negativo!")

elif numero == 0:
    print("O seu numero é zero!")

elif numero>=1:
    print("Seu numero é positivo")
    