"""
Tipo Float

Tipo real, decimal

Casa decimal

OBS: O separado de casas decimais na progrmaçao é o ponto e não a virgula.
"""

# ERRADO DO PONTO DE VISTA DO FLOAT MAS GERA UMA TUPLA
valor = 1, 44

print(valor)
print(type(valor))

# CERTO DO PONTO DE VISTA FLOAT

valor = 1.44
print(valor)
print(type(valor))

# É possivel fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter em floar para um int
"""
OBS: aA o converter valores float para inteiros, nos perdemos precisao
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com numeros complexos
variavel = 5j

