import os
os.system("cls || clear")
numero = 0

while True:
    numero = int(input('Digite um numero positivo: '))
    if numero < 0:
        break
    else:
        print('continue')