"""
Módulo Collections - Named Tuple
https://docs.python.org/pt-br/3/library/collections.html#collections.namedtuple

Recap Tupla:
tupla = (1, 2, 3)

print(tupla[1])

Named Tuple-> São Tuplas diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.

# Importando

from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1 -  Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 -

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

loki = cachorro(idade=5, raca='SRD', nome='Loki')
valentina = cachorro(idade=5, raca='Shih Tzu', nome='Valentina')

print(loki)
print(valentina)

# Acessando os dados
# Forma 1

print(loki[0])  # Idade
print(loki[1])  # Raça
print(loki[2])  # Nome

# Forma 2

print(valentina.idade)  # Idade
print(valentina.raca)  # Raça
print(valentina.nome)  # Nome

print(loki.index('SRD'))
print(loki.count('SRD'))

"""
