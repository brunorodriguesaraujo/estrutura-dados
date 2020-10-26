def mainWhile():
    n = int(input('Digite um número para cálculo de fatorial: '))
    c = n
    f = 1
    print('Fatorial de {}! = '.format(n), end='')
    while c > 0:
        f *= c
        c -= 1
    print('{}'.format(f))


mainWhile()


def mainFor():
    n = int(input('Digite um número para cálculo de fatorial: '))
    f = 1
    print('Fatorial de {}! = '.format(n), end='')
    for c in range(n, 1, -1):
        f *= c
    print(f)



mainFor()
