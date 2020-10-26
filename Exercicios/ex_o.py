def mainFor():
    print('Utilizando o FOR')
    inicio = int(input('Informe o número de inicio da sequência: '))
    fim = int(input('Informe o número do fim da sequência: '))

    for c in range(inicio, fim + 1):
        print(c * c, end='|')


mainFor()


def mainWhile():
    print(end='\n')
    print('\nUtilizando o WHILE')
    inicio = int(input('Informe o número de inicio da sequência: '))
    fim = int(input('Informe o número do fim da sequência: '))
    c = inicio-1

    while c < fim:
        c += 1
        print(c*c, end='|')


mainWhile()
