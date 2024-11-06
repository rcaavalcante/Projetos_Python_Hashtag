import pandas as pd

# Importando bases de dados

funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('CadastroClientes.csv', sep=';')
servicos_df = pd.read_excel('BaseServi‡osPrestados.xlsx')

#

# 1
# Criando uma coluna com o salario total de cada funcionario e somando itens dessa coluna

funcionarios_df['Salario Total'] = (funcionarios_df['Salario Base'] + funcionarios_df['Impostos']
                                    + funcionarios_df['Beneficios'] + funcionarios_df['VT'] + funcionarios_df['VR'])

gasto_empresa_funcionarios = funcionarios_df['Salario Total'].sum()
print('O gasto total da empresa com funcionários foi de R${:,} reais'.format(gasto_empresa_funcionarios))

# 2
print(servicos_df[:0])
print(clientes_df[:0])
print(funcionarios_df[:0])
faturamento_cliente = servicos_df.merge(clientes_df, on='ID Cliente') # a tabela fato sempre deve receber a dimensao no .merge()
faturamento_cliente = faturamento_cliente[['ID Cliente', 'Valor Contrato Mensal', 'Tempo Total de Contrato (Meses)']]
faturamento_cliente['Faturamento total'] = faturamento_cliente['Valor Contrato Mensal'] * faturamento_cliente['Tempo Total de Contrato (Meses)']
faturamento_total = faturamento_cliente['Faturamento total'].sum()
#print('O faturamento total da empresa foi de: R${:,.2f}'.format(faturamento_total).replace(',','.'))

# 3
total_funcionarios = funcionarios_df['ID Funcionário'].count()
#print(total_funcionarios)

funcionarios_fecharam_contrato = len(servicos_df['ID Funcionário'].unique())
print('O percetual de funcionários que fecharam contrato foi de: {:.2%}'.format(funcionarios_fecharam_contrato/ total_funcionarios))

# 4
#forma 1
areas = funcionarios_df['Area'].unique()
#print(areas)

servicos_df1 = servicos_df.merge(funcionarios_df, on='ID Funcionário')
servicos_df1 = servicos_df1[['Codigo do Servico', 'ID Funcionário', 'ID Cliente', 'Area', 'Tempo Total de Contrato (Meses)']]
#print(servicos_df1[:0])
'''
Operacoes = 0
Logistica = 0
Administrativo = 0
Financeiro = 0
Comercial = 0
for i in servicos_df1['Area']:
    if i in areas:
        if i == 'Operações':
            Operacoes += 1
        elif i == 'Logística':
            Logistica += 1
        elif i == 'Administrativo':
            Administrativo += 1
        elif i == 'Financeiro':
            Financeiro += 1
        else:
            Comercial += 1
    else:
        print('Área não correspondente')
print('Total de contratos por área \nOperacoes: {}\nLogistica: {}\nAdministrativo: {}\nFinanceiro: {}\nComercial: {}'.format(Operacoes, Logistica, Administrativo, Financeiro, Comercial))
'''
#forma 2

contratos_area = servicos_df1['Area'].value_counts()
#print(contratos_area)

# 5
#forma 1
funcionarios_operacoes = 0
funcionarios_logistica = 0
funcionarios_administrativo = 0
funcionarios_financeiro = 0
funcionarios_comercial = 0
for i in funcionarios_df['Area']:
    if i in areas:
        if i == 'Operações':
            funcionarios_operacoes += 1
        elif i == 'Logística':
            funcionarios_logistica += 1
        elif i == 'Administrativo':
            funcionarios_administrativo += 1
        elif i == 'Financeiro':
            funcionarios_financeiro += 1
        else:
            funcionarios_comercial += 1
    else:
        print('Área não correspondente')
print('Total de funcionários por área \nOperacoes: {}\nLogistica: {}\nAdministrativo: {}\nFinanceiro: {}\nComercial: {}'
      .format(funcionarios_operacoes, funcionarios_logistica, funcionarios_administrativo, funcionarios_financeiro, funcionarios_comercial))

#forma2
funcionarios_area = funcionarios_df['Area'].value_counts()
#print(funcionarios_area)

# 6
ticket_médio_mensal = clientes_df['Valor Contrato Mensal'].mean()
print('O ticket médio mensal foi de: R${:,.2f}'.format(ticket_médio_mensal))
