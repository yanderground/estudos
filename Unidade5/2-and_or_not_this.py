"""
estruturas logicas: and, or, not, is

operadores unarios:
    -not, is
operadores binarios:
    -and, or

regras de funcionamento:

Para o AND ambos os valores precisam ser true
Para o OR , um ou outro precisa ser TRUE
Para o NOT, o valor do booleano é invertido, ou seja se for TRUE vira FALSE, se for false vira true
Para o IS, o valor é comparado com um segundo valor.

"""
ativo = True
logado = False

if ativo:
    print("bem vindo usuario")
else:
    print("voce precisa ativar sua conta, por favor cheque seu email")

#ativo é true?
print(ativo is True)
