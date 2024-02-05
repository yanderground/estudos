"""
Tipo booleano

Algebra Booleana, criada por george Boole

2 constantes, verdadeiro ou falso

True -> Verdadeiro
False -> Falso

errado:

true, false

Certo:

True, False
"""

ativo = False

print(ativo)

"""
Operaçoes basicas:
"""

# Negaçao (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado sera falido,
se for falso o resultado sera verdadeiro. Ou seja, sempre o contrario.
"""
print(not ativo)

logado = False

# Ou (or)
"""
É uma operação binaria, ou seja, depende de dois valores. Ou um ou outro deve ser veradeiro

True or True = True
True or False = True
False or True = True
False or False = False
"""
print(ativo or logado)

# E (and)
"""
Tambem é uma operação binaria, ou seja, depende de dois valores. Ambos os
valores devem ser verdadeiro.

True and True -> True
True and False -> False
False and True -> False
False and False -> True
"""

