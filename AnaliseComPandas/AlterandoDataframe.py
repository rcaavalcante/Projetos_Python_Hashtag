import pandas as pd

clientes_df = pd.read_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/CodigosHashtag/AnaliseComPandas/Contoso - Clientes.csv', sep=';', encoding= 'cp1252')
clientes_df = clientes_df.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10' ], axis=1) # para tirar colunas (ou axis=0 para linhas)
clientes_df = clientes_df[['ÿID Cliente', 'E-mail']]
clientes_df = clientes_df.rename(columns={'ÿID Cliente': 'ID Cliente'}) #renomeando colunas

lojas_df = pd.read_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/CodigosHashtag/AnaliseComPandas/Contoso - Lojas.csv', sep=';', encoding= 'cp1252')
lojas_df = lojas_df[['ÿID Loja', 'Nome da Loja']]
lojas_df = lojas_df.rename(columns={'ÿID Loja': 'ID Loja'})

produtos_df = pd.read_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/CodigosHashtag/AnaliseComPandas/Contoso - Cadastro Produtos.csv', sep=';', encoding= 'cp1252')
#produtos_df = produtos_df[['ID Produto', 'ÿNome do Produto']]
produtos_df = produtos_df.rename(columns={'ÿNome do Produto': 'Nome do Produto'})
#print(produtos_df[:0])

vendas_df = pd.read_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/CodigosHashtag/AnaliseComPandas/Contoso - Vendas - 2017.csv', sep=';')
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')
vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do Cliente'})
#print(vendas_df.info())

'''
Nota-se que as colunas de venda e envio não são reconhecidas como data, mas como objeto,
portanto, precisamos fazer a conversão 
'''

# Adicionando ou Modificando colunas
vendas_df['Data da Venda'] = pd.to_datetime(vendas_df['Data da Venda'], format = '%d/%m/%Y')
vendas_df['Ano da Venda'] = vendas_df['Data da Venda'].dt.year
vendas_df['Mês da Venda'] = vendas_df['Data da Venda'].dt.month
vendas_df[('Dia da Venda')] = vendas_df['Data da Venda'].dt.day
#print(vendas_df[:0])

# Modificando um valor especifico em uma tabela

#print(clientes_df.head()) # Método para mostrar as 5 primeiras listas
#print(clientes_df.tail()) # Método para mostrar as 5 últimas listas

'''
2 métodos para alterar valores específicos:
1. loc - permite pegar uma linha de acordo com o índice dela. Ele dá erro caso não encontre o índice. Isso é interessante principalmente quando o índice é uma informação relevante ao invés só do número do índice ou quando queremos pegar alguma linha específica do dataframe (ao invés de ir do início do dataframe até a linha 5, por exemplo).
        Também podemos usar como loc[índice_linha, índice_coluna] para acessar um valor específico e modificá-lo.
2. iloc - enxerga o dataframe como linhas e colunas e consegue pegar o valor com um número de linha e um número de coluna. Repara que ele não analisa o valor do índice da linha e da coluna, apenas a posição importa.
        Uso: iloc[num_linha, num_coluna]"
'''

# Alterando o indice da tabela para serem o Nome do produto, em vez de números começando no 0

produtos_df = produtos_df.set_index('Nome do Produto')
#print(produtos_df.head())

# Pegando o preço unitario por meio do loc e iloc
#print(produtos_df.loc['Contoso Optical Wheel OEM PS/2 Mouse E60 Grey', 'Preco Unitario'])
#print(produtos_df.iloc[2,5])

# Alterando preco unitario da tabela de um unico produto de indice determinado: Contoso Wireless Laser Mouse E50 Grey
# Forma 1
#produtos_df.loc['Contoso Wireless Laser Mouse E50 Grey', 'Preco Unitario'] = 23

# Forma 2
produtos_df.loc[produtos_df['ID Produto'] == 873, 'Preco Unitario'] = 23
#print(produtos_df.loc['Contoso Wireless Laser Mouse E50 Grey', 'Preco Unitario'])

# Transformando um dicionario em um dataframe
vendas_produtos = {'iphone': [558147, 951642], 'galaxy': [712350, 244295], 'ipad': [573823, 26964], 'tv': [405252, 787604], 'máquina de café': [718654, 867660], 'kindle': [531580, 78830], 'geladeira': [973139, 710331], 'adega': [892292, 646016], 'notebook dell': [422760, 694913], 'notebook hp': [154753, 539704], 'notebook asus': [887061, 324831], 'microsoft surface': [438508, 667179], 'webcam': [237467, 295633], 'caixa de som': [489705, 725316], 'microfone': [328311, 644622], 'câmera canon': [591120, 994303]}
vendas_produtos_df = pd.DataFrame.from_dict(vendas_produtos, orient='index')
vendas_produtos_df = vendas_produtos_df.rename(columns={0: 'Vendas 2019', 1: 'Vendas 2020'})
#print(vendas_produtos_df)

# Exportando o arquivo csv

#vendas_produtos_df.to_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/.venv/CodigosHashtag/AnaliseComPandas/Novo Vendas 2017.csv', sep=';', encoding='latin1')

df = pd.read_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/CodigosHashtag/AnaliseComPandas/Novo Vendas 2017.csv', sep=';', encoding='latin1')
print(df)
