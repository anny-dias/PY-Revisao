'''Exercício 02
Implemente a função quadrado que recebe um número e retorna o resultado desse número ao 
quadrado.'''

def quadrado(num):
    quadrado = num ** 2
    return quadrado

num = float(input("Insira um número: "))
print(f"O resultado é {quadrado(num)}")


