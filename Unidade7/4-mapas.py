"""
Mapas -> Conhecidos em Python como Dicionarios

Dicionarios em Python sao representados por chaves {}

# Iterar sobre dicionarios

for chave in receita:
    print(chave)


for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi {receita[chave]}.')


# Acessando as chaves:

print(receita.keys())

for chave in receita.keys():  # Modo pythonico de fazer
    print(receita[chave])

# Acessando os valores:

print(receita.values())

for valor in receita.values():  # Modo pythonico
    print(valor)

# Desempacotamento de dicionarios
print(receita.items())

for chave, valor in receita.items():
    print(f'chave= {chave} e valor= {valor}')

# Soma*, Valor Maximo*, Valor Minimo*, Tamanho
# * Se os valores forem inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
"""
receita = {'Jan': 100, 'Fev': 250, 'Mar': 400}



