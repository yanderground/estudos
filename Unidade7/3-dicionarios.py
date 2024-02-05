"""
Dicionarios

OBS.: Em algumas linguagens de programção, os dicionarios Python sao conhecidos por mapas

Dicionarios Sao coleçoes do tipo chave/valor.

Dicionarios sao representados por {}.
print(type({}))

OBS.: Sobre Dicionarios
    - Chave e Valor sao separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

# Criação de Dicionarios

# Forma 1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'pa': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', pa='Paraguai')
print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 -  Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
# print(paises['ru'])
# Caso tentamos fazer o acesso utilizando uma chave que nao existe, teremos o erro KeyError

# Forma 2 - Acessando via get -  Recomendada

print(paises.get('br'))
print(paises.get('ru'))

# Caso o get nao encontre o objeto com a chave informada, será retornado o valor None e nao sera gerado KeyError

pais = paises.get('ru')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Nao encontrei o País')

# Podemos definir um valor padrao para caso nao encontremos o objeti com a chave informada
pais = paises.get('pa', 'Não Encontrado')

print(f'Encontrei o país {pais}')

# Podemos verificar se determinada chave se encontra em um dicionario

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos Utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionario, como chaves
# de dicionarios.

# Tuplas por exemplo sao bastante interessantes de serem utilizadas como chave de dicionarios, pois as mesmas
# sao imutaveis.
localidades = {
    (35.6895, 39.6917): 'Escritorio em Toquio',
    (40.7128, 74.0060): 'Escritorio em Nova Iorque',
    (37.7749, 122.4194): 'Escritorio em Sao Paulo',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1 - mais comum

receita['abr'] = 350

print(receita)

# Forma 2 - menos comum

novo_dado = {'mai': 500}
receita.update(novo_dado)  # receita.update({'mai': 500})
print(receita)

# Atualizando dados em um dicionario

# Forma 1

receita['mai'] = 550
print(receita)

# Forma 2

receita.update({'mai': 600})
print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionario é a mesma.
# CONCLUSAO 2: Em dicionarios, NÃO podemos ter chaves repetidas.

# Remover dados de um dicionario

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1 - mais comum

ret = receita.pop('mar')
print(ret)

print(receita)

# OBS 1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2

del receita['fev']
print(receita)

# Se a chave nao existir sera gerado um KeyError.
# OBS: Neste caso o valor nao é retornado.

"""

# Imagine que voce tem um comercio eletronico, onde temos um carrinho de compras na qual adicionamos produtos.
"""
Carrinho de compras:
    Produto 1:
        -nome;
        -quantidade;
        -preço;
    Produto 2:
        -nome;
        -quantidade;
        -preço;


# 1 - Poderiamos utilizar uma lista para isso? Sim

carrinho = []
# indice = [      0        , 1,    2   ]
produto1 = ['Playstation 5', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual é o indice de cada informação no produto.

# 2 - Poderiamos utilizar uma Tupla para isso? Sim

produto1 = ('Playstation 5', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teriamos que saber qual é o indice de cada informação no produto.

# 3 - Poderiamos utilizar um dicionario para isso? Sim

carrinho = []

produto1 = {'nome': 'Playstation 5', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto podemos ter
# a certeza sobre cada informaçao

# Metodos de dicionarios.

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionario (zerar dados)

d = dict(a=1, b=2, c=3)
d.clear()

print(d)

# Copiando um dicionario para outro
# Forma 1 # Deep Copy

novo = d.copy()
print(novo)

novo['d'] = 4

print(d)
print(novo)


# Forma 2 # Shallow Copy

novo = d
print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma nao usual de criaçao de dicionarios

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# OBS: O metodo FromKeys recebe dois parametros: um interavel e um valor.
# Ele vai gerar para cada valor do iteravel uma chave e ira atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)
"""


