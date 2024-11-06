import pandas as pd

vendas_vf = pd.read_csv(r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/.venv/CodigosHashtag/Contoso - Vendas - 2017.csv', sep=';')

#print(vendas_vf[['Numero da Venda', 'Data da Venda', 'ID Produto']])
#print(vendas_vf['Numero da Venda'][:1])

#vendas_vf.info()

lista_clientes = vendas_vf['ID Cliente']
print(lista_clientes)