# 📊 Data Science for Finance

# 📚 Bibliotecas Necessárias

Este curso utiliza várias bibliotecas Python amplamente conhecidas e utilizadas na área de Data Science e Finanças. Abaixo, você encontrará uma lista das bibliotecas necessárias e uma breve descrição de cada uma:

1. **NumPy** - Uma biblioteca fundamental para computação numérica em Python, que oferece suporte a arrays multidimensionais, funções matemáticas de alto nível e geração de números aleatórios.

2. **Pandas** - Uma biblioteca poderosa e flexível para manipulação e análise de dados em Python, que oferece estruturas de dados como DataFrames e Series, facilitando a manipulação de dados tabulares.

3. **Matplotlib** - Uma biblioteca de visualização de dados em Python, que permite criar gráficos e visualizações estáticas, animadas e interativas.

4. **Plotly** - Uma biblioteca de gráficos interativos para Python, que permite criar visualizações de dados sofisticadas e interativas, como gráficos de linha, de barras, de dispersão, entre outros.

5. **MPL Finance** - Uma extensão do Matplotlib voltada especificamente para a visualização de dados financeiros, como gráficos de candlestick (velas) e gráficos de médias móveis.

6. **NumPy Financial** - Uma biblioteca de funções financeiras baseada em NumPy que fornece funções úteis para cálculos financeiros, como valor presente líquido, taxa interna de retorno e amortização de empréstimos.

7. **pandas-datareader** - Uma biblioteca que permite extrair dados financeiros de várias fontes na web, como Yahoo Finance, Alpha Vantage e Banco Central do Brasil, diretamente para um DataFrame do Pandas.

8. **Quandl** - Uma biblioteca para acessar a plataforma Quandl, que fornece dados financeiros, econômicos e alternativos de várias fontes.

9. **FinQuant** - Uma biblioteca para construção e análise de portfólios financeiros com foco na Otimização de Média-Variância de Markowitz.

10. **PyPortfolioOpt** - Uma biblioteca para otimização de portfólios financeiros que implementa algoritmos clássicos de otimização de média-variância e modernos, como Black-Litterman e Hierarchical Risk Parity.

11. **SQLAlchemy** - Uma biblioteca de mapeamento objeto-relacional (ORM) que permite trabalhar com bancos de dados SQL de maneira mais fácil e orientada a objetos.

12. **Requests** - Uma biblioteca popular para fazer solicitações HTTP em Python, usada para acessar APIs e extrair dados da web.

Para instalar todas essas bibliotecas, você pode utilizar o comando `pip`:


## Lista de Aulas

### 01 - Python Básico
1. Introdução ao Python
2. Operadores Matemáticos e Expressões
3. Variáveis
3b. Prática – O Valor do Dinheiro no Tempo
4. Listas
5. Tuplas
6. Dicionários
7. Estruturas Condicionais
8. Estruturas de Repetição
9. Funções
10. Módulos

### 02 - NumPy
1. NumPy Arrays
2. Indexação e Seleção
3. Operações
4. NumPy Financial

### 03 - Pandas
1. Introdução
2. Seleção
3. Seleção
4. Tratando Dados Faltantes
5. GroupBy
6. Concat
7. Merge
8. Join
9. Ordenação e Filtragem
10. Tabelas Dinâmicas com o Google Colab

### 04 - Fontes de Dados Financeiros
1. Yahoo Finance
2. Alpha Vantage
3. Banco Central do Brasil
4. Pandas DataReader
5. Quandl
6. Tesouro Nacional

### 05 - Visualização de Dados Financeiros
1. MatPlotLib – Parte 1
2. MatPlotLib – Parte 2
3. Plotly – Parte 1
4. Plotly – Parte 2
5. MPL Finance

### 06 - Python Avançado
1. List Comprehensions
2. Funções Lambda
3. Argumentos Flexíveis
4. Erros e Exceções
5. Iteradores

### 07 - Fundamentos de Finanças com Python
1. Retorno
2. Retorno Simples vs Retorno Log
3. Retorno Acumulado
4. Retorno Médio
5. Retornos Diários
6. Retornos Mensais
7. Retornos Trimestrais
8. Retornos Anuais e Janelas de Retornos
9. Retorno Acumulado
10. Janelas de Retornos em Reais
11. Medidas Estatísticas
12. Medidas de Volatilidade e Risco
13. Normalização

### 08 - Exemplos Práticos
1. Mapa de Correlação IBOV
2. IBOV Dolarizado
3. IBOV Deflacionado
4. IBOV vs CDI
5. Retorno e Volatilidade das ações do IBRX 50

### 09 - Portfólio e Modelo de Markowitz
1. Portfolio com Pesos Iguais
2. Retorno Ponderado
3. Matriz de Retornos e Volatilidade
4. Fronteira Eficiente para dois Ativos (gráfico)
5. Formulação Matemática de Retorno Esperado e Volatilidade
6. Fronteira Eficiente para dois Ativos (código)
7. Simulação de Monte Carlo
8. Sharpe Ratio
9. Fronteira Eficiente para Portfolio de vários Ativos
10. FinQuant
11. BackTesting – Preparando a Base de Dados
12. Otimizando para Máximo Sharpe-Ratio e Mínima Volatilidade
13. Backtesting das Carteiras Otimizadas

### 10 - Modelos Quant para Construção de Portfolios
1. Modelos Matemáticos
2. Distribuição Normal
3. Demonstração – Probabilidade com Python
4. Modelos de Retorno – Gráficos
5. Modelos de Retorno – Cálculo Estatístico
6. Otimização Média-Variância (PyPortfolioOpt)
7. CAPM
8. Calculando os Betas dos Ativos
9. Otimização por CAPM
10. Black-Litterman – Teoria
11. Black-Litterman na Prática
12. Black-Litterman – Idzorek, Matriz P e Vetor Q
13. Modelos de Risco
14. Backtesting dos Modelos – Preparando a Base de Dados e Calculando as Carteiras Ótimas
15. BackTesting dos Modelos – Construindo e Executando o Processo de Teste

### 11 - Projeto de Dados (ETL) - Curva de Juros
1. Visão Geral e Processo de ETL
2. Conhecendo a fonte e os dados
3. Processo de Extração de Dados
4. Criando API e Banco de Dados SQL
5. Carregando os Dados
6. Automatizando o processo de ETL
7. Alterando o código pra rodar na nuvem
8. Colocando o script em produção
9. Criando cliente para consumir nossa API
