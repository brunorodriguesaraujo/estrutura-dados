def main():
    print('=-=-=-PALÍNDROMO=-=-=-')
    num = int(input('Informe os números: '))
    inteiro = str(num)
    if num == inteiro[::-1]:
        print('PALÍNDROMO')
    else:
        print('NÃO É PALÍNDROMO')

main()
