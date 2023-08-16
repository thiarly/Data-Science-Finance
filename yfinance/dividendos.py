import yfinance as yf


# Baixando cotações de ITUB4, entre 2015 e 2017
itub4 = yf.download('ITUB4.SA', start='2023-01-01', end='2023-08-01')

# Usando a classe Ticker
vale3 = yf.Ticker('VALE3.SA')

vale_informacoes = vale3.info
vale_splits_dividendos = vale3.actions
vale_dividendos = vale3.dividends
vale_institutional_holders = vale3.institutional_holders

stocks = ['BBAS3']# 'BBSE3','TRPL4', 'JHSF3','EGIE3', 'FLRY3','BBDC4', 'BBDC3','SAPR4', 'ITSA4','TAEE3', 'ABCB4','SANB3', 'PSSA3'
stocks = [item + '.SA' for item in stocks]

print('A taxa de dividendos é o total de dividendos esperados em um ano.')
for stock in stocks:
    info = yf.Ticker(stock).info
    div = info.get('dividendRate')
    print(stock, div)
    
print('\n')

print(' O rendimento do dividendo é uma relação financeira que mostra o quanto uma empresa paga em dividendos a cada ano em relação ao preço de suas ações.')
for stock in stocks:
    info = yf.Ticker(stock).info
    div = info.get('dividendYield')
    print(stock, div)
    
print('\n')

print(' A data ex-dividendo é a data em que os acionistas recém adquiridos não têm mais direito a receber o próximo dividendo.')
for stock in stocks:
    info = yf.Ticker(stock).info
    div = info.get('exDividendDate')
    print(stock, div)
    
print('\n')


print(' A taxa de distribuição é a porção dos ganhos que a empresa paga aos acionistas na forma de dividendos. ')
for stock in stocks:
    info = yf.Ticker(stock).info
    div = info.get('payoutRatio')
    print(stock, div)
    
print('\n')


print(' Essa é a média ponderada do dividendo da ação nos últimos 12 meses. ')
for stock in stocks:
    info = yf.Ticker(stock).info
    div = info.get('payoutRatio')
    print(stock, div)
    
print('\n')



print('O rendimento de dividendo anual dos últimos 12 meses é o rendimento total do dividendo recebido no último ano dividido pelo preço atual da ação.')
for stock in stocks:
    info = yf.Ticker(stock).info
    div = info.get('trailingAnnualDividendYield')
    print(stock, div)
    
print('\n')

print('O valor do último dividendo pago.')
for stock in stocks:
    info = yf.Ticker(stock).info
    div = info.get('lastDividendValue')
    print(stock, div)
    
print('\n')

print ('A data do último dividendo pago. ')
for stock in stocks:
    info = yf.Ticker(stock).info
    div = info.get('lastDividendDate')
    print(stock, div)
    
print('\n')


