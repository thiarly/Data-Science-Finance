import yfinance as yf


# Baixando cotações de ITUB4, entre 2015 e 2017
itub4 = yf.download('ITUB4.SA', start='2023-01-01', end='2023-08-01')

# Usando a classe Ticker
vale3 = yf.Ticker('VALE3.SA')

vale_informacoes = vale3.info
vale_splits_dividendos = vale3.actions
vale_dividendos = vale3.dividends
vale_institutional_holders = vale3.institutional_holders


for chave in vale_informacoes:
    print(chave, vale_informacoes[chave])