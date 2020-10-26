def Primeiro(n1, n2):
    return (n1 * 2) + (n2 / 2)


def Segundo(n1, n3):
    return (n1 * 3) + n3


def Terceiro(n3):
    return (n3 ** 3)


def main():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    n3 = float(input('Digite um número real: '))

    resultado1 = Primeiro(n1, n2)
    resultado2 = Segundo(n1, n3)
    resultado3 = Terceiro(n3)
    print(resultado1, resultado2, resultado3)


main()