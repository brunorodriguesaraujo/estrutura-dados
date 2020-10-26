def main():
    numClientes = int(input('Número de clientes: '))
    c = 1
    somaTempo = 0

    while c < numClientes + 1:
        tempoEspera = float(input('Tempo de espera do {}º cliente: '.format(c)))
        c += 1
        somaTempo += tempoEspera
    mediaTempo = somaTempo / numClientes
    print('O tempo médio de espera é de {}'.format(mediaTempo))


main()
