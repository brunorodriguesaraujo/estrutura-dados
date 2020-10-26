def main():
    registros = []
    for i in range(0, 5):
        nomes = str(input('Digite o {}º nome: '.format(i+1)))
        registros.append(nomes)
        print(nomes)
    nome = str(input('Digite outro nome: '))
    registros.append(nome)
    outroNome = str(input('Digite mais um nome: '))
    registros.insert(2, outroNome)
    print(registros)


main()