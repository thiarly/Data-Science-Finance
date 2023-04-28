#Importando apenas o função pd do pandas
import pandas as pd

#Exemplo de dados
valor_inicial = 1000
valor_final = 1500
dividendos = [50, 60, 30]
duracao = 3 # anos


#Criar um DataFrame Pandas com os fluxos de caixa.
df = pd.DataFrame({"Dividendos": dividendos})


rentabilidade_cotizada = ((valor_final + df["Dividendos"].sum()) / valor_inicial) ** (1 / duracao) -1
rentabilidade_cotizada = rentabilidade_cotizada * 100
print('{:.2f}%'.format(rentabilidade_cotizada))