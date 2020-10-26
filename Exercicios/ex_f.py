from math import ceil
area = float(input('Digite o tamanho da área a ser pintada: '))
litros = area / 3
lata = ceil(litros/18)
valor = lata * 80
print('Ao todo você vai precisar de {} lata(s) de tinta, o valor que você irá gastar é {:.2f}R$'.format(lata, valor))
