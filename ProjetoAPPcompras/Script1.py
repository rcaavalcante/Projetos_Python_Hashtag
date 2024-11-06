# Importando os módulos
import json
import os
import time

# Criando funções básicas
def adiciona_item(compras, item, quantidade):
    compras[item] = quantidade

def remove_item(compras, item):
    if item in compras:
        del compras[item]

def visualiza_item(compras):
    for item, quantidade in compras.items():
        print(f'{item}: {quantidade}')
    print()
    print('Pressione Enter para continuar')
    input()

def salva_compras(compras, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(compras, arquivo)

def carregar_compras(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return json.load(arquivo)

# Definir a variável TERM para que seja possível limpar a tela com o os.system
os.environ['TERM'] = 'xterm'

# Criando funções principais
def gerenciar_compras(compras, nome_arquivo=None):
    while True:
        os.system("clear")
        print('1 Adicionar item')
        print('2 Remover item')
        print('3 Visualizar lista')
        print('4 Salvar e sair')
        print('5 Sair sem salvar')
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            item = input('Digite o nome do item: ')
            quantidade = int(input('Digite a quantidade: '))
            adiciona_item(compras, item, quantidade)
        elif escolha == '2':
            item = input('Digite o nome do item: ')
            remove_item(compras, item)
        elif escolha == '3':
            visualiza_item(compras)
        elif escolha == '4':
            if nome_arquivo is None:
                nome_arquivo = input('Digite o nome do arquivo para salvar: ')
            if not nome_arquivo.endswith('.json'):
                nome_arquivo += '.json'
            salva_compras(compras, nome_arquivo)
            break
        elif escolha == '5':
            break
        else:
            print('Escolha uma opção válida')
            time.sleep(1)

def main():
    while True:
        os.system("clear")
        print('1 Criar uma nova lista de compras')
        print('2 Carregar uma lista existente')
        print('3 Sair')
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            compras = {}
            gerenciar_compras(compras)
        elif escolha == '2':
            print('Listas disponíveis:')
            arquivos = [arquivo for arquivo in os.listdir() if arquivo.endswith('.json')]
            if not arquivos:
                print('Nenhuma lista encontrada')
                time.sleep(1)
                continue
            for i, arquivo in enumerate(arquivos, 1):
                print(f'{i} {arquivo}')
            escolha = int(input('Escolha uma lista para carregar (0 se nenhuma): '))
            if escolha == 0:
                continue
            if escolha < 0 or escolha > len(arquivos):
                print('Escolha uma opção válida')
                time.sleep(1)
                continue
            nome_arquivo = arquivos[escolha - 1]
            compras = carregar_compras(nome_arquivo)
            gerenciar_compras(compras, nome_arquivo)

        elif escolha == '3':
            break
        else:
            print('Escolha uma opção válida')
            time.sleep(1)

if __name__ == "__main__":
    main()