"""
Recebendo dados do usurario

input() -> todo dado recebido via input é do tipo String

Em python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas Simples -> 'Yan Augusto'
- Aspas duplas -> "Yan Augusto"
- Aspas simples triplas -> '''Yan Augusto'''
"""
# - Aspas duplas triplas -> """ Yan Augusto"""

# Entrada de dados
# print("qual seu nome?")
# nome = input() #Input -> entrada de dados

nome = input('Qual seu nome? ' )

# exemplo de print 'antigo' v2.x
# print('Seja bem vindo(a) %s' % nome)

# Exemplo de print moderno v3.x
# print('Seja bem vindo(a) {0}'.format(nome))

# eXEMPLO de print mais atual v3.7
print(f'Seja bem vindo(a) {nome}')

# print("Qual sua idade? ")
# idade = input()

idade = int(input('Qual sua idade? '))

# processamento

# saida
# Exemplo de print antigo v2.x
# print('O %s tem %s anos' % (nome, idade))

# Exemplo de print moderno v3.x
# print('O {0} tem {1} anos'. format(nome, idade))

# eXEMPLO de print mais atual v3.7
print(f'O {nome} tem {idade} anos')

"""
# int(idade) => cast

cast é a 'conversao' de um tipo de dado para outro.
"""
print(f'O {nome} nasceu em {2023 - idade}')