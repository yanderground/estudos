"""
# 1
num = 10
print(num)

# 2
num = 1.5
print(num)

# 3

num1 = int(input("Digite um número "))
num2 = int(input("Digite um número "))
num3 = int(input("Digite um número "))

soma = num1 + num2 + num3

print(f'A soma desses numeros eh = {soma}')

# 4

numf = 3.5
quadrado = numf * numf
print(float(quadrado))

# 5
numreal = 5.5
quinta = 5.5/5
print(float(quinta))

# 6

celcius = float(input(f'Informe os graus Celcius: '))
fahrenheit = celcius * (9.0 / 5.0) + 32.0
print(f'Convertido para Fahrenheit: {fahrenheit} graus')

# 7
fahrenheit = float(input('Digite quantos graus Fahrenheit: '))
c = (5.0 * (fahrenheit - 32.0))/9.0
print(f'Convertido para Celcius: {c} graus')

# 8

k = float(input('Digite os graus em Kelvin: '))
c = k - 273.15
print(f'Convertido para Celcius: {c} graus')

# 9
c = float(input('Digite os Graus em Celcius: '))
k = c + 273.15
print(f'Convertido para Kelvins: {k} graus')

# 10
kmh = 100.0
ms = kmh/3.6
print(f'100 kilometros por hora (km/h) para metros por segundo (m/s): {ms}')

# 11
ms = 27.77
kmh = ms * 3.6
print(f'Convertendo 27.77m/s para km/h ficará = {kmh}')

# 12
milhas = 6.2
km = 1.61 * milhas
print(f'6.2 milhas para km : {km:.2f} km')  # FORMATAÇÃO DE NUMERO REAL

# 13
km = 10
milhas = (km/1.61)
print(f'10 km convertido para milhas : {milhas:.2f} milhas')

# 14
graus = 120
rad = graus * (3.14/180)
print(f'120 graus convertidos para radianos : {rad}')

# 15
rad = 3
graus = rad * (180/3.14)
print(f'radianos para graus: {graus}')

# 16
pol = 50
cm = pol * 2.54
print(f'polegadas para centimetros: {cm}')

# 17
cm = 127
pol = cm/2.54
print(f'127 centimetros para polegadas: {pol}')

# 18
mcub = 30.55
li = 1000 * mcub
print(f'30.55m³ para litros são: {li}')

# 19
li = 1000
mcub = li/1000
print(f'1000 litros para m³ são: {mcub}')

# 20
kg = 70
lb = kg/0.45
print(f'70kg para libras são: {lb}')

# 21
lb = 100
kg = lb * 0.45
print(f'100lbs para kilogramas: {kg}')

# 22
jar = 20
m = 0.91 * jar
print(f'10 jardas para metros: {m} metros')

# 23
m = 30
jar = m/0.91
print(f'30 metros para jardas: {jar:.2f} jardas')

# 24
mqua = 200
acre = mqua * 0.000247
print(f'200m² convertido em acres: {acre}')

# 25
acres = 2
mqua = acres * 4048.58
print(f'2 acre convertido em m²: {mqua}m²')

# 26
mqua = 10000
hec = mqua * 0.0001
print(f'10000m² para hectares: {hec}')

# 27
hec = 4
mqua = hec * 10000
print(f'4 hectares equivale a {mqua}m²')

# 28
a = 10
b = 20
c = 30
soma = (a*a) + (b*b) + (c*c)
print(soma)

# 29
n1 = 8
n2 = 7.5
n3 = 10
n4 = 6.4
media = (n1 + n2 + n3 + n4)/4
print(media)

# 30
real = float(input('Coloque o valor em Real: R$'))
cota = float(input('Coloque a cotação atual do Dólar: R$'))
conversao = real / cota
print(f'A conversão de real para Dólar é: $ {conversao:.2f}')

# 31
numero = 10
print(numero - 1)
print(numero + 1)

# 32
num = 5
soma = ((num*3)+1) + ((num*2)-1)
print(soma)

# 33
lado = float(input('Escreva o valor do lado do quadrado:'))
area = lado * lado
print(f'Area do quadrado: {area}')

# 34
raio = float(input('Escreva o raio do circulo: '))
area = 3.141592 * (raio*raio)
print(f'A area do circulo é: {area}')

# 35
a = float(input('Escreva o cateto 1 do triângulo: '))
b = float(input('Escreva o cateto 2 do triângulo: '))
hipotenusa = ((a * a) + (b * b)) ** 0.5
print(f'{hipotenusa:.2f}')

# 36
altura = float(input('Digite a altura do cilindro circular: '))
raio = float(input('Digite o raio do cilindro circular: '))
volume = 3.141592 * (raio*raio) * altura
print(f'O volume do cilindro é: {volume:.1f} m³')
"""


