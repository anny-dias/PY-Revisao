'''Exercício 01
Implemente a função somar que recebe dois números e retorna o resultado da soma desses dois 
números.
Lembre-se que para retornar um resultado a função deve utilizar a instrução return.'''

def somar(num1, num2):
    soma = num1 + num2
    return soma
    

num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
print(f"O resultado da soma é de {somar(num1, num2)}")


