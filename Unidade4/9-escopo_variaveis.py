"""
Escopo de variaveis

Dois casos de escopo:

1- Variaveis globais;
    - Variaveis globais sao reconhecidas, ou seja, seu escopo compreende, todo o programa.
2- Variaveis Locais;
    - Variaveis locais, sao reconhecidas apenas no bloco onde foram declaradas, ou seja,
    seu escopo está limitado ao bloco onde foi declarada.


Para declarar variaveis em Python fazemos:

nome_da_variavel =  valor_da_variavel

PyTHON É uma linguagem de tipagem dinamica. Isso significa que
ao declararmos uma variavel, nós nao colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor a mesma.

Exemplo em c:
int numero = 42;

Exemplo em Java:
int numero = 42;
"""
numero = 42  # Exemplo e variavel global
print(numero)
print(type(numero))

numero = 'Yan'
print(numero)
print(type(numero))

nao_existo = 'oI'
print(nao_existo)

numero = 42
# novo = 0

if numero > 10:
    novo = numero + 10  # VARIAVEL NOVO ESTA DECLARADA LOCALMENTE DENTRO DO BLOCO O IF. POrtanto, é local
    print(novo)
