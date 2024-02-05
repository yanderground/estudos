"""
Loop for

Loop-> é uma estrutura de repetição
For-> Uma dessas estruturas

C ou Java

for(int i = 0; i < 10; i++){
    //execuçao
}

python:

for item in interavel:
    //execuçao do loop


Utilizamos loops para iterar sobre squencias ou sobre valores iteraveis

Exemplos de iteraveis :
- String
    nome = 'Yan Gomes'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros =  range(1, 10)

# Ex de for 1:
# Iterando sobre uma string
for letra in nome:
    print(letra)

# Ex de for 2
# Iterando sobre uma lista
for numero in lista:
    print(numero)

# Exemplo de for 3 (iterando sobre um range

range(valor_incial, valor_final)
OBS: o valor final nao é inclusive.
1
2
3
4
5
6
7
8
9
10 - nao

for numero in range(1, 10):
    print(numero)

Enumerate:
(0, 'Y'), (1, 'a'), (2, 'n'), (3,' '), (4, 'G') ...)


for indice, letra in enumerate(nome):
    print(nome[indice])
for indice, letra in enumerate(nome):
    print(letra)
for _, letra in enumerate(nome):
    print(letra)
OBS: Quando nao precisamos de um valor, podemos descarta-lo utilizando um underline(_)

nome = 'Yan Gomes'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n} / {qtd} valor'))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Yan Gomes'
for letra in nome:
    print(letra, end = '') # End usado para nao pular a linha

tabelas de emojus unicode: http://apps.timwhitlock.info/emoji/tables/unicode

# Original: U+1F631
# Modificado: U0001F600

for _ in range(3):
    for num in range(1, 10):
        print('\U0001F412' * num)
"""
