"""
Tuplas

Tuplas sao bastante parecidas com listas
Existem basicamente 2 diferenças basicas:
1 - As tuplas sao representadas por parenteses ()

2-  As tuplas sao imutaveis: Isso significa que ao se criar uma tupla ela nao muda. Toda
operação em uma tupla gera uma nova tupla.

# Cuidado 1: As tuplas sao representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# Cuidado 2: Tuplas com elemento

tupla3 = (4)  # Isso nao é uma tupla
print((tupla3))

print(type(tupla3))

tupla4 = (4,)  # Isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))

# Conclusao: Podemos concluir que tuplas sao definidas pelo uso de virgula e nao parenteses

(4) - nao é tupla
4, - é tupla
(4,) - é tupla

# Podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de Tupla

tupla = ('Yan Gomes', 'BOM AMSFOASDMF')
pessoa, jacare = tupla
print(pessoa)
print(jacare)

# OBS: gERA ERRO (ValueError) se colocarmos um numero diferente de elementos para desempacotar.
# Metodos para adiçao e remoçao de elementos nas tuplas nao existem, dado o fato das tuplas serem imutaveis

# Soma*, Valor Maximo, Valor Minimo* e Tamanho
# * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))  # Tamanho da tupla

# Cocatenaçao de Tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1+tupla2)  # Tuplas sao imutaveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2  # Tuplas sao imutaveis, mas podemos sobrescrever seus valores
print(tupla1)

# Verificar se determinado elemento esta contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)

# Iterando sobre uma tupla
tupla = (1, 2, 3)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elemento dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))

# O acesso a elementos de uma tupla tambem é semelhante a de uma lista

# Dicas na utilizaçao de tuplas
# Devemos utilizar tuplas SEMPRE que nao precisarmos modificar os dadods contidos em uma coleção
# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')


print(meses[5])

# Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i = i+1

# Verificamos em qual indice um elemento esta na tupla
print(meses.index('Junho', 6))

# Caso o elemento nao exista sera gerado erro

# Por que utilizar Tuplas?

# - Tuplas sao mais rapidas do que listas.
# - Tuplas deixam seu codigo mais seguro*.

# *Isso porque trabalhar com elementos imutaveis tras segurança para o codigo.

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla  # Na tupla nao temos o problema de Shallow copy

print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra

print(type(nova))
print(tupla)
"""


