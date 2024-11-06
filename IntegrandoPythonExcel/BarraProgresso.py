import pandas as pd

# Importando arquivos

vendas_df = pd.read_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/.venv/CodigosHashtag/AnaliseComPandas/Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/.venv/CodigosHashtag/AnaliseComPandas/Contoso - Cadastro Produtos.csv', sep=';', encoding= 'cp1252')
lojas_df = pd.read_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/.venv/CodigosHashtag/AnaliseComPandas/Contoso - Lojas.csv', sep=';', encoding= 'cp1252')
clientes_df = pd.read_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/.venv/CodigosHashtag/AnaliseComPandas/Contoso - Clientes.csv', sep=';', encoding= 'cp1252')

# Limpando apenas as colunas que queremos

produtos_df = produtos_df[['ID Produto', 'ÿNome do Produto']]
lojas_df = lojas_df[['ÿID Loja', 'Nome da Loja']]
clientes_df = clientes_df.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10' ], axis=1) # para tirar colunas (ou axis=0 para linhas)
clientes_df = clientes_df[['ÿID Cliente', 'E-mail']]

# Mesclando e renomeando os DFs

produtos_df = produtos_df.rename(columns={'ÿNome do Produto': 'Nome do Produto'})
lojas_df = lojas_df.rename(columns={'ÿID Loja': 'ID Loja'})
clientes_df = clientes_df.rename(columns={'ÿID Cliente': 'ID Cliente'})

vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')
vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do Cliente'})

 #renomeando colunas

#print(vendas_df[:0])

# Corrigindo a qtde devolvida da loja de ID 222

from tqdm import tqdm

pbar =  tqdm(total = len(vendas_df['ID Loja']), position = 0, leave = True)

for i , id_loja in enumerate(vendas_df['ID Loja']):
    pbar.update()
    if id_loja == 222:
        vendas_df.loc[i, 'Quantidade Devolvida'] += 1

print(vendas_df)