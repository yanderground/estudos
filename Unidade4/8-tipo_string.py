"""
Tipo String

Já vimos que em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '1234', 'a', 'True', '42.2'
- Estiver entre aspas duplas -> "uma string", "1234", "a", "True", "42.2"
- Estiver entre aspas triplas -> '''uma string''', '''1234''', '''a''', '''True''', '''42.2'''

nome = 'Yan Games'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Sarah \nAndreli'
print(nome)
print(type(nome))

nome = 'Sarah \"Andreli'
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) -> Transforma em uma lista de springs

print(nome[0:5]) # Slice de string

print(nome[6:11]) # Slice de string

# [   0   ,    1   ]
# ['Sarah', 'Linda']
print(nome.split()[0])

print(nome.split()[1])
"""
# - Estiver entre aspas duplas triplas -> """uma string""", """1234""", """a""", """True""", """42.2"""

#[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
#['S','a','r','a','h',' ','l','i','n','d','a']

nome = 'Sarah linda'
"""
[::-1] -> comece do primeiro elemento, va ate o ultimo elemento e inverta
"""
print(nome[::-1]) # Iversao da string Pythonico

print(nome.replace('a', 'i'))

print(type(nome))

texto = 'socorram me subino onibus em marrocos' # Palindromo
print(texto)
print(texto[::-1])
