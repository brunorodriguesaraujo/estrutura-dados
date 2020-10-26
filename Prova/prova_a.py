def numVelasAniversario(numVelas):
    velasAltura = []
    if numVelas < 1 or numVelas > 10 ** 5:
        return 'Erro'

    else:
        for i in range(0, numVelas):
            lista = int(input('Digite a altura da {} vela: '.format(i+1)))
            velasAltura.append(lista)
            if velasAltura[i] < 1 or velasAltura[i] > 10 ** 7:
                return 'Erro'
        maior = max(velasAltura)
        totalMaior = velasAltura.count(maior)
        return totalMaior



def main():
    
    num = int(input('Qual a idade da criança? '))
    a = numVelasAniversario(num)
    print('Números de velas com a altura máxima = {}'.format(a))


main()