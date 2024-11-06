import pandas as pd

clientes_df = pd.read_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/.venv/CodigosHashtag/AnaliseComPandas/Contoso - Clientes.csv', sep=';', encoding='cp1252')
clientes_df = clientes_df.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10' ], axis=1) # para tirar colunas (ou axis=0 para linhas)
clientes_df = clientes_df[['ÿID Cliente', 'E-mail']]
clientes_df = clientes_df.rename(columns={'ÿID Cliente': 'ID Cliente'}) #renomeando colunas
#print(clientes_df)

lojas_df = pd.read_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/.venv/CodigosHashtag/AnaliseComPandas/Contoso - Lojas.csv', sep=';', encoding='cp1252')
lojas_df = lojas_df[['ÿID Loja', 'Nome da Loja']]
lojas_df = lojas_df.rename(columns={'ÿID Loja': 'ID Loja'})
#print(lojas_df)

promocoes_df = pd.read_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/.venv/CodigosHashtag/AnaliseComPandas/Contoso - Promocoes.csv', sep=';', encoding='cp1252')
#print(promocoes_df)

vendas_df = pd.read_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/.venv/CodigosHashtag/AnaliseComPandas/Contoso - Vendas - 2017.csv', sep=';')
#print(vendas_df[:0]) # para ver os nomes das colunas

produtos_df = pd.read_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/.venv/CodigosHashtag/AnaliseComPandas/Contoso - Cadastro Produtos.csv', sep=';', encoding= 'cp1252')
produtos_df = produtos_df[['ID Produto', 'ÿNome do Produto']]
produtos_df = produtos_df.rename(columns={'ÿNome do Produto': 'Nome do Produto'})
#print(produtos_df)

# Mesclando tudo em 1 dataframe só para ficar intuitivo - método merge
# novo_dataframe = dataframe1.merge(dataframe2, on='coluna')

vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')
vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do Cliente'})

print(vendas_df[:0])
