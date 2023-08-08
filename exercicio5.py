'''Exercício 05
Implemente a função calcular_salario, que recebe o salário atual de um funcionário e retorna o 
salário com um reajuste de aumento, sendo que:
- Caso o salário seja maior que R$ 2.000,00, o funcionário receberá 7% de aumento.
- Caso contrário, o funcionário receberá 15% de aumento.'''

def calcular_salario (salario):
    if salario > 2000.0:
        reajuste = salario + (salario * (7/100))
    else:
        reajuste = salario + (salario * (15/100))
    return reajuste

salario = float(input("Insira o salário atual: "))
print(f"O salário com reajuste é de {calcular_salario (salario)}")

