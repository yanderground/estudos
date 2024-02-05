"""
PEP8 - Python Enhanced Proposal
São propostas de melhorias para linguagem Python
Zen of Python
import this

A ideia da PEP8 é que possamos escrever codigos Python de forma Pythônica.

[1] - Utilize Camel Case para nomes de classes;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minusculo separados por underline para funçoes ou variaveis;

def soma():
    pass


def soma_dois():


numero = 4
numero_impar = 5

[3] - Utilize 4 espaços para identação! (não use tab)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
-Separar funções e definiçõesde classecom duas linhas em branco;
-Metodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - Imports
- Imports devem ser sempre em linhas separadas;

#Import errado
 import sys, os

#Import certo
import sys
import os

#Não há problemas em utilizar:

from types import Stringtype, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda se fazer:

from types import(
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devemser colocados no topo do arquivo, logo depoisde quaisquer comentários ou docstrings
# e antes  de constantes ou variáveis globias.

[6] -Espaços em expressões e instruções

#Não faça:
funcao( algo[ 1 ], { outro: 2 } )

#Faça:

funcao(algo[1], {outro: 2})

#Não faça:

algo (1)

#Faça:

algo(1)

#Não faça:

dict  ['chave'] = list [indice]

#Faça:

dict['chave'] = list[indice]

#Não faça:

x              =  1
y              =  2
variavel_longa =  5

#Faça:

x = 1
y = 2
variavel_longa = 5

[7] Termine sempre uma instrução com uma nova linha

"""
import this
