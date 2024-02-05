"""
Ranges
- Precisamos conhecer o Loop for para usar os ranges.
- Precisamos conhecer o range para tranalhar com melhor com loops for.

Ranges sao utilizados para gerar sequencias numericas, nao de forma aleatoria,
mas sim de maneira especificada.

Formas gerais:

range(valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrao 0, e passo de 1 em 1)

# ex Forma 1
for num in range(11):
    print(num)

# EX forma 2
range(valor_de_inicio, valor_de_parada)

obs: valor_de_parada não inclusive ( inicio especificado pelo usuario, e passo de 1 em 1)

for num in range(1, 11): # o 1 foi especificado, por isso ele começa em 1 e nao em 0
    print(num)

# Ex Forma 3
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario)

for num in range(5, 55, 5):
    print(num)

# EX forma 4 (Inversa)
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario)

for num in range(10, -1, -5):
    print(num)

"""
