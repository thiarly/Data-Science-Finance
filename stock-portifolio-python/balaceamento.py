import pandas as pd
import yfinance as yf

# Caminho da base de dados
base_dados = '/Users/thiarly/Library/CloudStorage/OneDrive-Personal/Control Personal/Finance/Carteiras de Investimentos/holding.xlsm'

# Lendo a aba cv do arquivo holding.xlsm
df = pd.read_excel(base_dados, sheet_name='cv', usecols="A:H")

# Calcular a quantidade total de cada ativo
df_total = df.groupby('ATIVO')['QUANTIDADE'].sum()

# Filtrando os ativos com quantidade maior ou igual a 1
df_total = df_total[df_total >= 1]

# Removendo ativos indesejados
ativos_remover = ['POUPANÇA', 'IRBR1', 'DOLAR', 'MXRF12', 'CDB DI INTER']
df_total = df_total[~df_total.index.isin(ativos_remover)]

# Convertendo a Series para DataFrame
df_total_acoes = df_total.reset_index()

# Obtendo a lista de tickers
tickers = [ativo + '.SA' for ativo in df_total_acoes['ATIVO']]

# Baixar os dados históricos de fechamento das ações
cotacao_atual = yf.download(tickers, period="1d")["Adj Close"]

# Ajustando o DataFrame cotacao_atual
cotacao_atual.columns = [col.replace('.SA', '') for col in cotacao_atual.columns]


print('\n')
print(cotacao_atual)

# Mesclando df_total_acoes e cotacao_atual
valor_carteira = df_total_acoes.merge(cotacao_atual.T, left_on='ATIVO', right_index=True)

# Multiplicando a quantidade de ações pelas cotações atuais
valor_carteira['Valor_Carteira'] = (valor_carteira.iloc[:, 2:].values * valor_carteira['QUANTIDADE'].values[:, None]).sum(axis=1).round(2)

# Formatando o valor da carteira com duas casas decimais, separador de milhares e separador decimal
valor_carteira['Valor_Carteira'] = valor_carteira['Valor_Carteira'].apply(lambda x: 'R$ {:,.2f}'.format(x).replace('.', '#').replace(',', '.').replace('#', ','))

# Ajustando o indice para comecar em 1
valor_carteira.index = valor_carteira.index + 1


# Calculando a soma total dos valores de cada ação
soma_total = valor_carteira['Valor_Carteira'].str.replace('R$', '').str.replace('.', '').str.replace(',', '.').astype(float).sum()

# Calculando a porcentagem de cada ativo com base no valor total
valor_carteira['Porcentagem'] = ((valor_carteira['Valor_Carteira'].str.replace('R$', '').str.replace('.', '').str.replace(',', '.').astype(float) / soma_total) * 100).round(2)

# Adicionando o símbolo de '%' na coluna 'Porcentagem'
valor_carteira['Porcentagem'] = valor_carteira['Porcentagem'].apply(lambda x: '{:.2f}%'.format(x))

# Renomeando as colunas para maiúsculo
valor_carteira = valor_carteira.rename(columns={'ATIVO': 'ATIVO', 'QUANTIDADE': 'QUANTIDADE', 'Valor_Carteira': 'VALOR_CARTEIRA', 'Porcentagem': 'PORCENTAGEM'})

# Exibindo o resultado de colunas especificas
#print(valor_carteira[['ATIVO', 'QUANTIDADE', 'VALOR_CARTEIRA', 'PORCENTAGEM']])

print(valor_carteira)

print('\n')

print('Soma Total: R$', '{:,.2f}'.format(soma_total).replace(',', '.'))

valor_carteira.to_excel('valor_carteira.xlsx', index=False)

# exportando para excel colunas expecificas
# valor_carteira[['ATIVO', 'QUANTIDADE', 'VALOR_CARTEIRA', 'PORCENTAGEM']].to_excel('valor_carteira.xlsx', index=False)
