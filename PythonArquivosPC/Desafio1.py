# Desafio: Separar todos os arquivos de forma que cada arquivo esteja na pasta do estado correspondente aquele arquivo.

# Importando Módulos
from pathlib import Path
import shutil

# Descobrindo onde está nosso arquivo
caminho = Path.cwd()
#print(caminho)

# Navegando até uma pasta específica
caminho = Path('/Users/rafaellacavalcante/Documents/PythonCods/Codigos_hashtag/IntegraçãoPythonPastasPC/Arquivos_Lojas')
print(caminho)

# Listando todos os arquivos da Pasta Atual
arquivos = caminho.iterdir()

# Criando Pastas
estados = ['RJ', 'SP', 'MG', 'GO', 'AM']
for estado in estados:
    Path('PastaAuxiliar/{}'.format(estado)).mkdir()

# Separando os arquivos de acordo com o nome
for arquivo in arquivos:
    if arquivo.name[-4:] == '.csv':
        estado = arquivo.name[-6:-4]
        shutil.copy2(arquivo, Path('PastaAuxiliar/{}/{}'.format(estado,arquivo.name)))
    else:
        print('ERRO')


