print('===---===---=== Dia do Programador ===---===---===')


def diaDoProgramador(ano):
    if ano < 1700 or ano > 2700:
        return 'Erro! Digite o ano entre 1700 e 2700'

    elif ano < 1918:
        if ano % 4 == 0:
            return 'O dia do Programador foi em 12.09.{} por ser um ano bissexto.'.format(ano)
        else:
            return 'O dia do Programador foi em 13.09.{}'.format(ano)

    elif ano > 1918:
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            return 'O dia do Programador foi em 12.09.{} por ser um ano bissexto.'.format(ano)
        else:
            return 'O dia do programador foi em 13.09.{}'.format(ano)

    else:
        return 'O dia do Programador foi em 26.09.{}'.format(ano)


def main():
    anoPretendido = int(input('\nInforme o ano entre 1700 e 2700 para saber o dia do Programador: '))
    data = diaDoProgramador(anoPretendido)
    print(data)


main()
