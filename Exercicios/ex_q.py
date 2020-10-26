def main():
    n = int(input('Qual o valor você quer para a tabuada: '))
    for c in range(0, 11):
        r = n * c
        print('{} x {} = {}'.format(n, c, r))


main()

