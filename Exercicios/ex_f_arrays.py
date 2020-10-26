def main():
    nome = str(input('Digite seu nome: ')).upper().strip()
    sobrenome = str(input('Digite seu sobrenome: ')).upper().strip()
    print(f'Olá {nome} {sobrenome}!')
    print('Digite 5 nomes, inclua o seu nome também!')
    nomes = []
    for i in range(0, 5):
        n = str(input('Digite o {}º nome: '.format(i+1))).upper().strip()
        nomes.append(n)
    print(nomes)
    pos = nomes.index(nome)
    nomes[pos] = sobrenome
    print(nomes)
main()