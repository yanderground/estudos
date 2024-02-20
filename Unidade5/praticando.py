"""
pratica

# 1
a = 6
b = 5
if a > b:
    print("Variavel A maior ")
elif a == b:
    print("Variavel A igual a Variavel B")
elif a < b:
    print("Variavel B maior")
# 2
numero = float(input(f"Escreva um numero: "))
if numero > 0:
    raiz = numero * numero
    print(f'{raiz:.2f}')
else:
    print("Numero Invalido")

# 3
numero = float(input("digite um numero real: "))
if numero > 0:
    raiz = numero/2
    for k in range(20):  # metodo de newton para raiz quadrada
        raiz = (1/2)*(raiz + (numero/raiz))
    print(raiz)
else:
    print(numero * numero)

# 4
numero = float(input("DIgite um numero: "))
if numero > 0:
    quadrado = numero * numero
    print(f"Esse numero ao quadrado: {quadrado}")
    raiz = numero / 2
    for k in range(20):  # metodo de newton para raiz quadrada
        raiz = (1 / 2) * (raiz + (numero / raiz))
    print(f"A raiz do numero eh: {raiz}")
else:
    print("Numero não positivo")

# 5
numero = int(input("Escreva um numero inteiro: "))
if numero % 2 == 0:
    print("Numero par")
else:
    print("Numero impar")

# 6
num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite um segundo numero: "))
if num1 > num2:
    print(num1)
    num1 = num1 - num2
    print(num1)
else:
    print(num2)
    num2 = num2 - num1
    print(num2)

# 7
num1 = float(input("Digite um numero: "))
num2 = float(input("Digite um segundo numero: "))
if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
else:
    print("Numeros iguais")
# 8
nota1 = float(input("Nota 1:"))
nota2 = float(input("Nota 2:"))
if (0 <= nota1 <= 10) and (0 <= nota2 <= 10):
    media = (nota1 + nota2)/2
    print(f"Sua media: {media}")
else:
    print("Informe uma nota valida!")
# 9
salario = float(input("Digite seu salario: "))
prestacao = float(input("Digite o valor da Prestação do emprestimo: "))
salario = salario * 0.2 + salario
if prestacao > salario:
    print("Emprestimo não concedido")
else:
    print("Emprestimo concedido")

# 10
altura = float(input("Digite sua Altura: "))
sexo = input(f"Digite seu sexo (M ou F): ")
if sexo == 'M':
    peso = (72.7 * altura) - 58
    print(f"Seu peso 'ideal' eh: {peso:.2f}")
elif sexo == 'F':
    peso = (62.1 * altura) - 44.7
    print(f"Seu peso 'ideal' eh: {peso:.2f}")
else:
    print('Invalido')
"""

