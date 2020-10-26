def salarioTotal(num_horas, valor_horas):
    return num_horas * valor_horas


def impostoRenda(sal_bruto):
    return sal_bruto * 11 / 100


def previdenciaSocial(sal_bruto):
    return sal_bruto * 8 / 100


def sindicato(sal_bruto):
    return sal_bruto * 5 / 100


def salarioLiquido(sal_bruto, imp, inss, sind):
    return sal_bruto - (imp + inss + sind)


def desconto(imp, inss, sind):
    return imp + inss + sind


def main():
    num_horas = int(input('Digite o número de horas trabalhadas no mês: '))
    valor_horas = float(input('Digite o valor de cada hora trabalhada: '))

    sal_bruto = salarioTotal(num_horas, valor_horas)
    imp = impostoRenda(sal_bruto)
    inss = previdenciaSocial(sal_bruto)
    sind = sindicato(sal_bruto)
    sal_liq = salarioLiquido(sal_bruto, imp, inss, sind)
    desc = desconto(imp, inss, sind)
    print('O seu salário bruto é {:.2f}R$'.format(sal_bruto))
    print('O desconto do IPRF foi de {:.2f}R$'.format(imp))
    print('O desconto do INSS foi de {:.2f}R$'.format(inss))
    print('O desconto do Sindicato foi de {:.2f}R$'.format(sind))
    print('O seu salário líquido é de {:.2f}R$'.format(sal_liq))
    print('O valor total dos descontos foi de {:.2f}R$'.format(desc))


main()
