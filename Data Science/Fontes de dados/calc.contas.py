das = float(input('Valor da DAS: '))
gps = float(input('Valor da GPS: '))
contador = float(input('Valor do contador: '))
multa = str(input('Tem alguma multa a pagar? S / N: '))

soma_empresa = das + gps + contador

if multa in "S":
    while multa == "":
        multa = float(input('Valor da multa:'))
        soma_multas = multa + multa
        print('Valor a pagar de multa R$ {}'.format(soma_multas))
else:
    pass

print('Valor total: DAS, GPS e CONTADOR: R$ {:.2f}'.format(soma_empresa))


