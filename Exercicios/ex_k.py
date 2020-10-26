n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)/ 2
if media == 10:
    print('Aprovado com distinção! sua média foi de {:.1f}'.format(media))
elif media >= 7:
    print('Aprovado! sua média foi de {:.1f}'.format(media))
else:
    print('Reprovado! sua média foi de {:.1f}'.format(media))

