import yfinance as yf


#Baixando Cotações IBOV
ibov = yf.download('^BVSP')
#print(ibov)

#Baixando cotação BBDC4, entre 2020 e 2023
bbdc4 = yf.download('BBDC4.SA', start = '2020-01-01', end='2023-03-14' )
#print (bbdc4)

# Baixando dados intraday, minuto a minuto de BBAS3, dos últimos 5 pregões
# Valid intervals: 1m,2m,5m,15m,30,60m,90m,1h,1d,5d,1wk,1mo,3mo
# Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max

bbas3 = yf.download('BBAS3.SA', interval='1m', period='5d')
#print(bbas3)

# Baixando várias empresas de uma vez. Método 1(Tickers separados por espaço)
jb = yf.download('JHSF3.SA BBDC4.SA', period='1y')
#print(jb)

# Baixando várias empresas de uma vez. Método 2 (Passando uma lista de tickers)
jb = yf.download(['JHSF3.SA', 'BBDC4.SA'])

# Alterando o método de agrupamento
# Group by 'ticker' or 'column' (default)
jb = yf.download('JHSF3.SA BBDC4.SA', group_by='ticker', period='1y')
#print(jb)


# Usando a classe Ticker

trpl4 = yf.Ticker('TRPL4.SA')
trpl4 = trpl4.actions
#print(trpl4)

# Consultando Dividendos
trpl4 = yf.Ticker('TRPL4.SA')
trpl4 = trpl4.dividends
#print(trpl4)

trpl4 = yf.Ticker('TRPL4.SA')
trpl4 = trpl4.info
#print(trpl4)


trpl4 = yf.Ticker('TRPL4.SA')
trpl4 = trpl4.institutional_holders
#print(trpl4)

trpl4 = yf.Ticker('TRPL4.SA')
trpl4 = trpl4.recommendations
print(trpl4)