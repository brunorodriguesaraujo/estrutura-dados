def mainFor():
    print('Utilizando o FOR')
    numClientes = int(input('Número de clientes: '))
    somaTempo = 0

    for c in range(1, numClientes + 1):
        tempoEspera = float(input('Tempo de espera do {}º cliente: '.format(c)))
        somaTempo += tempoEspera
    mediaTempo = somaTempo / numClientes
    print('O tempo médio de espera é de {}'.format(mediaTempo))


mainFor()


def mainWhile():
    print('\nUtilizando o while')
    numClientes = int(input('Número de clientes: '))
    c = 1
    somaTempo = 0

    while c < numClientes + 1:
        tempoEspera = float(input('Tempo de espera do {}º cliente: '.format(c)))
        c += 1
        somaTempo += tempoEspera
    mediaTempo = somaTempo / numClientes
    print('O tempo médio de espera é de {}'.format(mediaTempo))


mainWhile()
