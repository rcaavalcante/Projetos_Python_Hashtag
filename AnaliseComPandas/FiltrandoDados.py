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

# Qual o percentual das vendas que foi devolvida?

qtde_vendida = vendas_df['Quantidade Vendida'].sum()
#print(qtde_vendida)

qtde_devolvida = vendas_df['Quantidade Devolvida'].sum()
#print(qtde_devolvida)

#print('O percentual devolvido foi de: {:.2%}'.format(qtde_devolvida / qtde_vendida))

# Qual seria o valor desse percentual para a Loja Contoso Europe Online?

percentual_europe = vendas_df[vendas_df['ID Loja'] == 306]
qtde_vendida_europe = percentual_europe['Quantidade Vendida'].sum()
qtde_devolvida_europe = percentual_europe['Quantidade Devolvida'].sum()
print('O percentual devolvido foi de: {:.2%}'.format(qtde_devolvida_europe / qtde_vendida_europe))

# O ideal é colocar os parâmetros em variáveis como boa prática
# Exemplo: Quais lojas Contoso Europe Online não tiveram devoluções?

loja306 = vendas_df['ID Loja'] == 306
qtde_devolvida_0 = vendas_df['Quantidade Devolvida'] == 0
qtde_devolvida_europe2 = vendas_df[loja306 & qtde_devolvida_0]
print(qtde_devolvida_europe2)
