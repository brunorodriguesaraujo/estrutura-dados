valor1 = float(input('Qual o valor do produto? R$'))
valor2 = float(input('Qual o valor do produto? R$'))
valor3 = float(input('Qual o valor do produto? R$'))
menor = valor1
if valor1 > valor2 and valor2 < valor3:
    menor = valor2
elif valor3 < valor2 and valor3 < valor1:
    menor = valor3
print('O produto que você deve comprar é {:.2f}'.format(menor))