
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import matplotlib
matplotlib.rcParams['figure.figsize'] = (16, 8)

#Importando a classe Timeseries de alpha_vantage.timeseries
from alpha_vantage.timeseries import TimeSeries

ALPHAVANTAGE_API_KEY = "02FTOCDGZQHVC0DR"

# Criando o objeto ts do tipo Timeseries
ts = TimeSeries(key=ALPHAVANTAGE_API_KEY, output_format='pandas')

#Pesquisando o código dos ativos com get_symbol_search()
pesquisa_get_symbol = ts.get_symbol_search('BBAS3.SAO')

#Obtendo os dados semanais do IBOV usando o get_weekly()
pesquisa_get_weekly = ts.get_weekly(symbol='IBOV.SAO')

#Obtendo os dados e metadados diários do IBOV usando get_daily() com outputsize='full'
#dado, meta_dados = ts.get_daily(symbol='IBOV.SAO', outputsize='full')
#Thank you for using Alpha Vantage! This is a premium endpoint.

# Exibindo os meta-dados
#meta_dados

# Plotando o gráfico do preço de fechamento
#dados['4. close'].plot()

# Importando TechIndicators de alpha_vantage.techindicators
from alpha_vantage.techindicators import TechIndicators

# Criando o objeto ti do TechIndicators
ti = TechIndicators (key=ALPHAVANTAGE_API_KEY, output_format='pandas')

# Obtendo os dados diários do Índice Bovespa 
#ibov = meta_ibov = ts.get_daily(symbol='IBOV.SAO', outputsize='full')
#Thank you for using Alpha Vantage! This is a premium endpoint.

# Obtendo as média móveis de 20 e 200 dias com get_sma() e o IFR de 14 dias com get_rsi()
# mm20 = ti.get_sma('IBOV.SAO', interval='daily') [0]
# mm200 = ti.get_sma('IBOV.SAO', interval='daily', time_period=200)[0]
# rsi = ti.get_rsi('IBOV.SAO', time_period=14)[0]
#Thank you for using Alpha Vantage! This is a premium endpoint.


# Plotando um gráfico com os indicadores Técnicos Baixados
# fig, ax = plt.subplots(2,1, sharex=True, figsize=(18,8))

# ax[0].set(ylabel="Pontos", title='Índice Bovespa')
# ax[0].plot(ibov['4. close'], label="IBOV")
# ax[0].plot(mm20, label='MM20')
# ax[0].plot(mm200, label='MM200')

# ax[1].set(ylabel="RSI")
# ax[1].plot(rsi)
# ax[1].axhline(70, color='red')
# ax[1].axhline(30, color='green')

# ax[0].legend();


# Importando FundamentalData de alpha_vantage.FundamentalData
from alpha_vantage.fundamentaldata import FundamentalData     

# Criando um objeto do tipo FundamentalData
fd = FundamentalData(key=ALPHAVANTAGE_API_KEY, output_format='pandas')

#Definindo o código da empresa
ticker = 'MSFT'

# Obtendo dados gerais da companhia com get_company_overview()
fd.get_company_overview(ticker)


bs = fd.get_balance_sheet_quarterly(ticker)
bs [0]