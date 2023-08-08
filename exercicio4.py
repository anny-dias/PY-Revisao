'''Exercício 04
Implemente a função media, que recebe três valores numéricos e retorna a média aritmética dos 
valores.'''

def media(num1, num2, num3):
    media = (num1 + num2 + num3) / 3
    return media

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
num3 = float(input("Insira o terceiro número: "))
print(f"A média aritmética dos valores é de {media(num1, num2, num3)}")

