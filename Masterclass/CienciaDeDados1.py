# Importar Bibliotecas e Bases de Dados
import pandas as pd
import pathlib
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

meses = {'jan': 1, 'fev': 2, 'mar': 3, 'abr': 4, 'mai': 5, 'jun': 6, 'jul': 7, 'ago': 8, 'set': 9, 'out': 10, 'nov': 11, 'dez': 12}
caminho_bases = pathlib.Path(r'/Users/rafaellacavalcante/Documents/PythonCods/Codigos_hashtag/ProjetoAirbnb/dataset')
base_airbnb = pd.DataFrame()

# Percorrendo a lista com todos os arquivos e adicionando coluna de mes e ano
for arquivo in caminho_bases.iterdir():
    nome_mes = arquivo.name[:3]
    mes = meses[nome_mes]
    ano = int(arquivo.name[-8:-4])
    df = pd.read_csv(caminho_bases / arquivo.name, low_memory=False)
    df['Ano'] = ano
    df['Mes'] = mes
    base_airbnb = base_airbnb._append(df)

# Como temos muitas colunas, o modelo pode acabar ficando lento, por isso vamos excluir as desnecessárias
base_airbnb.head(1000).to_csv('/Users/rafaellacavalcante/PycharmProjects/pythonProject/CodigosHashtag/Masterclass/teste.csv', sep=';')

# Depois da análise qualitativa das colunas, levando em conta os critérios definidos, ficamos com as colunas seguintes
colunas = ['host_response_time','host_response_rate','host_is_superhost','host_listings_count','latitude','longitude','property_type','room_type','accommodates','bathrooms','bedrooms','beds','bed_type','amenities','price','security_deposit','cleaning_fee','guests_included','extra_people','minimum_nights','maximum_nights','number_of_reviews','review_scores_rating','review_scores_accuracy','review_scores_cleanliness','review_scores_checkin','review_scores_communication','review_scores_location','review_scores_value','instant_bookable','is_business_travel_ready','cancellation_policy','Ano','Mes']

# Definindo o novo DataFrame atualizado somente com as colunas de interesse
base_airbnb = base_airbnb.loc[:,colunas]
print(len(list(base_airbnb.columns)))

# Tratando os valores Null/NaN
print(base_airbnb.isnull().sum())

# Visualizando os dados, percebemos que existe uma grande disparidade em dados faltantes. As colunas com mais de 300.000 valores NaN foram excluídas da análise
# Para as outras colunas, como temos muitos dados (mais de 900.000 linhas), vamos excluir as linhas que contém dados NaN
for coluna in base_airbnb:
    if base_airbnb[coluna].isnull().sum() > 300000:
        base_airbnb = base_airbnb.drop(coluna, axis=1)
print(base_airbnb.isnull().sum())

# Teste de solução
base_airbnb = base_airbnb.dropna()

# Verificar tipos de dados em cada coluna e ver se esta correto
print(base_airbnb.shape)

# Mas o que é Object? Vamos printar a primeira linha da tabela para confirmar:
print(base_airbnb.iloc[0])

# Após a análise de cada linha, vimos que o 'price' e o 'extra people' estão em formatos errados. Por isso vamos ajustar para os formatos certos:
#price
base_airbnb['price'] = base_airbnb['price'].str.replace('$', '')
base_airbnb['price'] = base_airbnb['price'].str.replace(',', '')
base_airbnb['price'] = base_airbnb['price'].astype(np.float32, copy=False)

#extra_people
base_airbnb['extra_people'] = base_airbnb['extra_people'].str.replace('$', '')
base_airbnb['extra_people'] = base_airbnb['extra_people'].str.replace(',', '')
base_airbnb['extra_people'] = base_airbnb['extra_people'].astype(np.float32, copy=False)
print(base_airbnb.info())

# Análise exploratória de dados
#display(base_airbnb)

print(base_airbnb.corr()) # ERRO