########### Início da Questão 01 #####################
nomeCompleto = "Carlos Eduardo Barbosa"
print("Resultado da questão 01 =", nomeCompleto)

########### Fim da Questão 01 ########################

########### Início da Questão 02 #####################
a = 2
b = 5

questao02 = 5*a * 3*b
print("Resultado da questão 02 =", questao02)

########### Fim da Questão 02 ########################

########### Início da Questão 03 #####################
a = 2
b = 5
c = 5

questao03 = a+b+c
print("Resultado da questão 03 =", questao03)

########### Fim da Questão 03 ########################

########### Início da Questão 04 #####################
print("Questão 04")
num01 = int(input("Digite o primeiro numero: "))
num02 = int(input("Digite o segundo numero: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")
questao04 = 0

if operacao == "+":
    questao04 = num01 + num02
    print("Resultado da questão 04 =", questao04)
elif operacao == "-":
    questao04 = num01 - num02
    print("Resultado da questão 04 =", questao04)
elif operacao == "*":
    questao04 = num01 * num02
    print("Resultado da questão 04 =", questao04)
elif operacao == "/":
    if num02 == 0:
        print("Impossível divisão por zero")
    else:
        questao04 = num01 / num02
        print("Resultado da questão 04 =", questao04)


########### Fim da Questão 04 ########################

########### Início da Questão 05 #####################
print("Questão 05")
print("a) Usando a instrução While:")
contador01 = 1
while(contador01 <=10):
    print(contador01)
    contador01 = contador01 + 1

print("\nb) Usando a instrução For e a função Range:")
for contador02 in range(1,11):
    print(contador02)

########### Fim da Questão 05 ########################

########### Início da Questão 06 #####################
print("\nQuestão 06")
print("\nb) Usando a instrução While:")
pares = 0
impares = 0
somaPares = 0
somaImpares = 0
contador03 = 1

while contador03 <= 10:
    if contador03 % 2 == 0:
        pares = pares + 1
        somaPares = somaPares + contador03
        contador03 = contador03 + 1
    else:
        impares = impares + 1
        somaImpares = somaImpares + contador03
        contador03 = contador03 + 1

print("Quantidade de pares é: ", pares)
print("A soma dos pares é: ", somaPares)

print("Quantidade de impares é: ", impares)
print("A soma dos impares é: ", somaImpares)

print("\nb) Usando a instrução For e as funções Range e Sum:")
contador04 = 1
os_pares = []
os_impares = []

for contador04 in range (1,11):
    if contador04 % 2 == 0:
        os_pares.append(contador04)
        continue
    else:
        os_impares.append(contador04)
        continue

qtde_pares = len(os_pares)
qtde_impares = len(os_impares)
Soma_pares = sum(os_pares)
Soma_impares = sum(os_impares)

print("Quantidade de pares é: ", qtde_pares)
print(os_pares)
print("A soma dos pares é: ", Soma_pares)

print("Quantidade de impares é: ", qtde_impares)
print(os_impares)
print("A soma dos impares é: ", Soma_impares)

########### Fim da Questão 06 ########################

########### Início da Questão 07 #####################
print("Questão 07")
print("7.a - Sem usar módulo math")
print("ax^2 + bx = c")
a = int(input("Digite o valor de 'a':"))
b = int(input("Digite o valor de 'b':"))
c = int(input("Digite o valor de 'c':"))

delta = b**2 - 4*a*c

if delta < 0:
    print("A equação não possui raizes reais")
elif delta == 0:
    x1 = -b/(2*a)
    print("A equação possui duas raízes reais iguais:", x1)
elif delta > 0:
    x1 = (-b + delta**0.5)/2*a;
    x2 = (-b - delta**0.5)/2*a;
    print("A equação possui duas raízes reais distintas:")
    print("Raiz um:", x1)
    print("Raiz dois:", x2)

import math

print("7.b - Usando módulo math")
print("ax^2 + bx = c")
a = int(input("Digite o valor de 'a':"))
b = int(input("Digite o valor de 'b':"))
c = int(input("Digite o valor de 'c':"))

delta = math.pow(b,2) - 4*a*c

if delta < 0:
    print("A equação não possui raizes reais")
elif delta == 0:
    x1 = -b/(2*a)
    print("A equação possui duas raízes reais iguais:", x1)
elif delta > 0:
    x1 = (-b + math.sqrt(delta))/2*a;
    x2 = (-b - math.sqrt(delta))/2*a;
    print("A equação possui duas raízes reais distintas:")
    print("Raiz um:", x1)
    print("Raiz dois:", x2)

########### Fim da Questão 07 ##############################

########### Início da Questão 08 ###########################
print("a) O que significa palavras reservadas em Python? "
      "Quais são as palavras reservadas no código acima?")

print("R- Palavras reservadas definem as regras e a estrutura da linguagem e não podem ser usadas como nomes de variáveis.\n"
      "   As palavras reservadas do código são: [def, if, return, else, math, sqrt, append]")

print("\nb) Qual a função de cada uma dessas palavras reservadas no código?")
print("R - def: Serve para declarar uma função.\n"
      "    if: Serve para gerar uma ação que é realizada se uma condição for satisfeita.\n"
      "    return: Serve para enviar o resultado da função de volta ao programa principal.\n"
      "    else: Se a condição do IF não for verdadeira, é a ação do else que será executada.\n"
      "    math: Invoca a biblioteca math, que possui funções matemáticas.\n"
      "    sqrt: Função matemática que retorna a raiz quadrada de um numero.\n"
      "    append: Serve para incluir um elemento no final de uma lista.")


import math

def bhaskara(a,b,c):
    delta = math.pow(b, 2) - 4 * a * c

    if delta < 0:
        return print("A equação não possui raizes reais")
    elif delta == 0:
        x1 = -b / (2 * a)
        print("A equação possui duas raízes reais iguais:", x1)
        return x1
    elif delta > 0:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (-b - math.sqrt(delta)) / 2 * a
        print("A equação possui duas raízes reais distintas:")
        print("x¹:", x1)
        print("x²:", x2)
        return x1
        return x2

a = int(input("Digite o valor de 'a':"))
b = int(input("Digite o valor de 'b':"))
c = int(input("Digite o valor de 'c':"))

bhaskara(a,b,c)

########### Fim da Questão 08 ##############################

########### Início da Questão 09 ###########################

s = "Mentorama"
maiuscula = s.upper()
invertida = maiuscula[::-1]

def vogais(string):
    vog = []
    for letra in string:
        if letra in 'AEIOU':
            vog.append(letra)
    return vog

print("a)", maiuscula)
print("b)", invertida)
print("c)", vogais(invertida))

########### Fim da Questão 09 #################################

########### Início da Questão 10 ##############################

nome = input("Informe o nome do usuário:")
sobrenome = input("Informe o sobrenome do usuário:")
idade = int(input("Informe a idade do usuário:"))
cidade = input("Informe a cidade do usuário:")
ddd = input("Informe o ddd da cidade do usuário:")
telefone = input("Informe o telefone do usuário:")

nome_completo = nome + sobrenome
telefone_completo = "(" + ddd + ") " + telefone[0:5] + "-" + telefone[5:10]

print("Nome: ", nome_completo)
print("Telefone: ", telefone_completo)
print("Idade: ", idade)
print("Cidade:", cidade)

########### Fim da Questão 10 #################################



