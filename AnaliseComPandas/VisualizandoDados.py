import pandas as pd
import matplotlib.pyplot as mtplb

clientes_df = pd.read_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/.venv/CodigosHashtag/AnaliseComPandas/Contoso - Clientes.csv', sep=';', encoding= 'cp1252')
clientes_df = clientes_df.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10' ], axis=1) # para tirar colunas (ou axis=0 para linhas)
clientes_df = clientes_df[['ÿID Cliente', 'E-mail']]
clientes_df = clientes_df.rename(columns={'ÿID Cliente': 'ID Cliente'}) #renomeando colunas

lojas_df = pd.read_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/.venv/CodigosHashtag/AnaliseComPandas/Contoso - Lojas.csv', sep=';', encoding= 'cp1252')
lojas_df = lojas_df[['ÿID Loja', 'Nome da Loja']]
lojas_df = lojas_df.rename(columns={'ÿID Loja': 'ID Loja'})

produtos_df = pd.read_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/.venv/CodigosHashtag/AnaliseComPandas/Contoso - Cadastro Produtos.csv', sep=';', encoding= 'cp1252')
produtos_df = produtos_df[['ID Produto', 'ÿNome do Produto']]
produtos_df = produtos_df.rename(columns={'ÿNome do Produto': 'Nome do Produto'})

vendas_df = pd.read_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/.venv/CodigosHashtag/AnaliseComPandas/Contoso - Vendas - 2017.csv', sep=';')
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')
vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do Cliente'})
#print(vendas_df[:0])

# Qual cliente comprou mais vezes?
# método .value_counts() para contar e .plot() para exibir o gráfico

'''
cliente_mais_comprou = vendas_df['E-mail do Cliente'].value_counts()
#print(cliente_mais_comprou)
cliente_mais_comprou[:5].plot(figsize=(15,10)) # mostrando somente os 5 primeiros registros
mtplb.show()
'''

# Qual loja que mais vendeu, em valor de vendas?

vendas_lojas = vendas_df.groupby('Nome da Loja').sum()
vendas_lojas = vendas_lojas[['Quantidade Vendida']]
print(vendas_lojas[-1:])

# Ordenando de acordo com a Qtde de vendas

'''
vendas_lojas = vendas_lojas.sort_values('Quantidade Vendida', ascending = False)
vendas_lojas[:5].plot(kind='bar')
mtplb.show()
'''

# Qual é o maior valor de vendas e de qual loja?

maior_valor = vendas_lojas['Quantidade Vendida'].max()
melhor_loja = vendas_lojas['Quantidade Vendida'].idxmax()
#print(maior_valor, melhor_loja)

# Qual produto menos vendeu?

pior_produto = vendas_df.groupby('Nome do Produto').sum()
pior_produto = pior_produto[['Quantidade Vendida']]
pior_produto = pior_produto.sort_values('Quantidade Vendida')
#print(pior_produto[:1])