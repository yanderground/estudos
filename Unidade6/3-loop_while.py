"""
Loop while

Forma geral
while expressao_booleana:
        //execuçao do loop

o bloco do while sera repetido enquanto a expressao booleana for verdadeira.

expressao booleana é toda expressao onde o resultado é verdadeiro ou falso.
Exemplo:

num = 5
num < 5

# ex 1:
num = 1

while num < 10:
    print(num)
    num = num + 1

# OBS: Em um loop while é importante que cuidemos do criterio de parada para nao causar um loop infinito.
# C ou Java

while(expressao){
    //execuçao
}
# do while

do{
    //execuçao
}while(expressao);

# Exemplo 2

resposta = ' '
while resposta != 'sim':
    resposta = input('Ja acabou jessica?')
    if resposta == 'nao':
        print('CABALOGOOOOOO')
print('grazadeus')


"""
