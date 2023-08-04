# tipos de dados
# int (inteiros)
a = 20
b = -10
c = 0 


# float (números reais)
a = 30.3
b = -3.5
c = 5.0


# str (string / texto)
a = 'Anny'
b = 'Exemplo'
c = '!@# 123'
c = ''' Exemplo
de string 
de multiplas 
linhas '''


# função type 
a = 4.5
print(type(a))
if type(a) == float:
    print('É um float')


# funções de conversão de tipos de dados 
a = 2
a = str(a)      #converte para str

a = '25'
a = int(a)      #converte para int

a = '4.56'
a = float(a)    #converte para float

a = 2
a = float(a)    #acrescenta casa decimal

a = 2.0
a = int(a)      #exclui casa decimal


# Operadores Aritméticos
print(2 + 3)        #soma
print(2 - 3)        #subtração
print(2 * 3)        #multiplicação
print(2 / 3)        #divisão
print(2 // 3)       #divisão inteira
print(2 % 3)        #resto da divisão
print(2 ** 3)       #potência


# Operadores Relacionais
print(2 == 2)       #igualdade
print(2 != 2)       #diferente
print(2 < 3)        #menor      
print(2 > 3)        #maior
print(2 <= 3)       #menor ou igual
print(2 >= 3)       #maior ou igual


# Operadores Lógicos
print(2 == 2 and 3 == 4)    #E
print(2 == 2 or 3 == 4)     #OU
print(not 2 == 2)           #NÃO

idade = 15
if idade < 18:
    print('menor')

if not idade >= 18:
    print('menor')


# Operações de entrada (input)
nome = input('Informe seu nome: ')
idade = int('Informe seu idade: ')
altura = float('Informe seu altura: ')


# Operações de saída (print)
nome = 'Anny'
idade = 17
print(nome, idade)
print('Seu nome é', nome, 'e sua idade é', idade, 'anos')
print('Seu nome é {} e sua idade é {} anos' .format(nome, idade))
print(f'Seu nome é {nome} e sua idade é {idade} anos')


# Estruturas de Decisão (if  elif  else)
#verficar se o número é par ou ímpar
numero = int(input('Número: '))
if numero % 2 == 0:
    print('Par')
else:
    print('Ímpar')

#verificar se o número é positivo, negativo ou zero
if numero > 0:
    print('Positivo')
elif numero < 0:
    print('Negativo')
else:
    print('Zero')


# Estrutura de seleção (match case)
opcao = int(input('Escolha uma opção (1, 2 ou 3): '))
match opcao:
    case 1:
        print('Opção 1')
    case 2:
        print('Opção 2')
    case 3:
        print('Opção 3')
    case _:
        print('Opção inválida')

# Estrutura de repetição (while)
#exibir os números inteiros de 1 a 10
cont = 1
while cont <= 10:
    print(cont)
    cont += 1

#solicitar 5 números e realizar o somatório dos números 
cont = 1
soma = 0
while cont <= 5:
    numero = int(input('Número: '))
    soma += numero      #somadora
    cont += 1           #contadora
print(f'Somatorio: {soma}')


# Estrutura de repetição (for)
#exibir os números inteiros de  a 10
for a in range(1, 11):
    print(a)

#solicitar 5 números e realizar o somatório dos números
soma = 0
for a in range(5):
    numero = int(input('Número'))
    soma += numero      #somadora
print(f'Somatório: {soma}')
