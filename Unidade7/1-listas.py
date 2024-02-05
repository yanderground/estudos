"""
Listas

Listas em python funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINAMICO e tambem de podermos colocar QUALQUER tipo de dado.

Linguagens C/java: Arrays
        -Possuem tamanho e tipo de dado fixo;
        Ou seja, nestas lingugagens se voce criar um array do tipo int e com tamanho 5, este array
        sera SEMPRE do tipo inteiro e poderá ter SEMPRE no maximo 5 valores.

Ja em Python:

- Dinamico: Por que nao possuem tamanho fixo; Ou seja podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python sao representadas por colchetes: []

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['Y', 'a', 'n', ' ', 'G', 'o', 'm', 'e', 's']

lista3 = []

lista4 = list(range(11))

lista5 = list('Yan Goooooomes')

# Podemos facilmente checar se determinado valor esta contido na lista
num = 7
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'nAO encontrei o {num}')

# Podemos facilmente ordenar uma lista

lista1.sort()
print(lista1)

# Podemos facilmente contar o numero de ocorrencias de um valor em uma lista
print(lista1.count(1))
print(lista5.count('o'))

# Adicionar elementos em listas

Para adicionar elementos ou valores em listas, utilizamos a funçao append

print(lista1)
lista1.append(42)
print(lista1)
# OBS: com append nos so conseguimos adicionar um elemento por vez
# lista1.append(12, 34, 56) # Erro

lista1.append([8, 3, 1])  # Coloca a lista como elemento unico (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei')
else:
    print('Nao encontrei')

lista1.extend([123, 44, 67])  # Coloca cada elemetno da lista com valor adicional a lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do indice
# Isso nao substitui o valor inicial, o mesmo sera deslocado para a direita da lista.
lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos facilmente juntar 2 listas
lista1 = lista1 + lista2
# lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista usando reverse
# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)
# Forma 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista

lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista5))

# Podemos remover facilmente o ultimo elemento de uma lista
# O pop nao somente remove o ultimo elemento mas tambem o retorna
print(lista5)
lista5.pop()
print(lista5)
# Podemos remover um elemento pelo indice
# OBS: os elementos a direita deste indice serao deslocados para a esquerda
# OBS: Se nao houver elemento no indice informado, teremos o erro IndexError
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para lista

# Exemplo 1

curso = 'Programaçao python: essencial'
print(curso)
curso = curso.split()
print(curso)

# Obs: Por padrao o Split separa os elementos da lista pelo espaço entre elas

# Exemplo 2

curso = 'Programaçao,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string
lista6 = ['Programaçao', 'em', 'Python:', 'Essencial']
print(lista6)

# Abaixo dizemos: pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo dizemos: pega a lista6, coloca cifrao entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista6 = [1, 2.34, True, 'Yan', 'D.', [1, 2, 3], 43723857835]
print(lista6)
print(type(lista6))

# Iterando sobre listas
# Ex 1 -  utilizando for
soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# Ex 2 - Utilizando while
carrinho = []
produto = ''
while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para 'sair': ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

# Utilizando variaveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada
#           0         1         2       3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o indice negativo, pense na lista como um circulo, onde
# o final de um elemento esta ligado ao inicio da lista

print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde
# print(cores[-5])  # ERRO, pois nao existe indice -5

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice,'-', cor)

# Lista aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# Metodos nao tao importantes mas tambem uteis
# Encontrar o indice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual indice da lista esta o valor 6?
print(numeros.index(6))

# Em qual indice da lista esta o valor 9?
print(numeros.index(9))

# print(numeros.index(19)) gera erro pois nao existe esse valor na lista

# OBS: caso nao tenha este elemento na lista, sera apresentado erro

# Obs: Retorna o indice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1))  # buscando a partir do indice 1
print(numeros.index(5, 2))  # buscando a partir do indice 2
print(numeros.index(5, 3))  # buscando a partir do indice 3
# print(numeros.index(5, 4))  # buscando a partir do indice 4 # Erro

# OBS: caso nao tenha este elemento na lista, sera apresentado erro

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6))  # Buscar o indice do valor 8, entre os indices 3 a 6

# Revisao de slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Trabalhando com slice de lista com o parametro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:])  # Iiniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parametro 'fim'

print(lista[:2])  # Começa em 0, pega ate o indice 2 - 1
print(lista[:4])  # Começa em 0, pega ate o indice 4 - 1
print(lista[1:3])  # Começa em 1, pega ate o indice 3 - 1

# Trabalhando com slice de lista com o parametro 'passo'
print(lista[1::2])  # Começa em 1, vai ate o final, de 2 em 2

print(lista[::2])  # Começa em 0, vai ate o final, de 2 em 2

# Invertendo valores em uma lista

nomes = ['YAN', 'GOMES']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['YAN', 'GOMES']

nomes.reverse()
print(nomes)

# Soma*, Valor Maximo*, Valor Minimo*, Tamanho
# * Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # Soma
print(max(lista))  # Maximo valor
print(min(lista))  # Minimo Valor
print(len(lista))  # Tamanho da lista

# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas

lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

# Se tivermos um numero diferente de elementos na lista ou variaveis para receber os dados,
# teremos ValueError

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()  # Copia

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista,
# mas elas ficaram totalmente independentes, ou seja, modificando uma lista, nao afeta a outra
# Isso em Python é chamado de Deep Copy ou Copia Profunda

# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista  # Copia tambem

print(nova)

nova.append(4)

print(lista)
print(nova)
# Veja que utilizamos a copia via atribuiçao e copiamos os dados da lista para a nova lista, mas
# apos realizar modificaçao em uma das listas, essa modificaçao se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy.
"""
