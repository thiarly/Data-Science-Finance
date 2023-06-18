import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import warnings

# Caminho da base de dados
base_dados = '/Users/thiarly/Library/CloudStorage/OneDrive-Personal/Control Personal/Finance/Carteiras de Investimentos/holding.xlsm'
# Lendo a aba cv do arquivo holding.xlsm
df = pd.read_excel(base_dados, sheet_name='cv', usecols="A:H")
print(df)

#print('Criando tabela com colunas para cada ativo e indexando por data')
table_ticket = pd.pivot_table(df, values='QUANTIDADE', index=['DATA'], columns=df['ATIVO'].str.upper(), aggfunc=np.sum, fill_value=0)
print(table_ticket)

#print('Criando tabela com os preços de compra e venda')
table_price = pd.pivot_table(df, values='PREÇO', index=['DATA'], columns=df['ATIVO'].str.upper(), fill_value=0)
print(table_price)

#print('Baixando as cotações das ações:')
prices = yf.download(tickers=(table_ticket.columns+'.SA').to_list(), start=table_ticket.index[0], rounding=True)['Adj Close']
prices.columns = prices.columns.str.rstrip('.SA')
prices.dropna(how='all', inplace=True)
# print(prices)
# try:
#   prices.to_excel('prices.xlsx')
#   print('Tabela de histórico de cotações baixada com sucesso e gerado o arquivo.')
# except Exception as e:
#   print('Ocorreu algum erro ao baixar as cotações e gerar o arquivo.')
#   print('Detalhe do erro:', e)
# time.sleep(5)

trades = table_ticket.reindex(index=prices.index)
trades.fillna(value=0, inplace=True)
#print(trades)

aportes = (trades * table_price).sum(axis=1)
#print(aportes)

posicao = trades.cumsum()
#print(posicao) 

carteira = posicao * prices
carteira['saldo'] = carteira.sum(axis=1)

print(carteira)

#####################################################
plt.plot(carteira['saldo'])
plt.xlabel('Índice')
plt.ylabel('Saldo')
plt.title('Gráfico de Saldo')
plt.grid(True)
plt.show()

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_colwidth', 100)
#####################################################


for i, data in enumerate(aportes.index):
  if i == 0:
    carteira.at[data, 'vl_cota'] = 1
    carteira.at[data, 'qtd_cotas'] = carteira.loc[data]['saldo'].copy()
  
  else:
    if aportes[data] != 0:
      carteira.at[data, 'qtd_cotas'] =  carteira.iloc[i-1]['qtd_cotas'] + (aportes[data] / carteira.iloc[i-1]['vl_cota'])
      carteira.at[data, 'vl_cota']   =  carteira.iloc[i]['saldo'] / carteira.at[data, 'qtd_cotas']
      carteira.at[data, 'retorno']   = (carteira.iloc[i]['vl_cota'] / carteira.iloc[i-1]['vl_cota']) -1 
    else:
      carteira.at[data, 'qtd_cotas'] = carteira.iloc[i-1]['qtd_cotas']
      carteira.at[data, 'vl_cota']   = carteira.iloc[i]['saldo'] / carteira.at[data, 'qtd_cotas']
      carteira.at[data, 'retorno']   = (carteira.iloc[i]['vl_cota'] / carteira.iloc[i-1]['vl_cota']) -1 


# print(carteira)
# carteira.to_excel('carteira.xlsx')
# carteira['vl_cota'].plot();
# plot.show()