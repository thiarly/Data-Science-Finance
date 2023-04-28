"""SISTEMA GERENCIADO DE SÉRIES TEMPORAIS DO BACEN (SGS)
https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries

Endereço padrão da API:
http://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados?formato=json&dataInicial={dataInicial}&dataFinal={dataFinal}

https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial={dataInicial}&dataFinal={dataFinal}"""

# Importando bibliotecas
import pandas as pd
from datetime import date

def consulta_bc(codigo_serie, dataInicial='01/01/1900',  dataFinal=date.today().strftime('%d/%m/%Y')):  
  url = f'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados?formato=json&dataInicial={dataInicial}&dataFinal={dataFinal}'
  df = pd.read_json(url)
  df['data'] = pd.to_datetime(df['data'], dayfirst=True)
  df.set_index('data', inplace=True)
  return df

# ipca = consulta_bc(443)
# print(ipca)

ipca = consulta_bc(433)
print(ipca)