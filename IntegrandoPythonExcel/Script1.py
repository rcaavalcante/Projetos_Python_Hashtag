import pandas as pd

tabela = pd.read_excel('Produtos3.xlsx')
print(tabela)

# Atualizando o imposto dos Serviços e consequentemente o Preco final

tabela.loc[tabela['Tipo']=='Serviço', 'Multiplicador Imposto'] = 1.5


tabela['Preço Base Reais'] = tabela['Preço Base Original'] * tabela['Multiplicador Imposto']

tabela.to_excel('Produtos3.xlsx', index=False) #index = false para nao salvar os indices como uma coluna na tabela nova
