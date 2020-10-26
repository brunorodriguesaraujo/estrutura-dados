sexo = str(input('Digite seu sexo:[M/F] ')).strip().upper()
if sexo in 'Mm'[0]:
    print('Sexo masculino')
elif sexo in 'Ff'[0]:
    print('Sexo feminino')
else:
    print('Gênero inválido')