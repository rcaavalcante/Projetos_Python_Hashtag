# Importando Módulos
from pathlib import Path

# Descobrindo onde está nosso arquivo
caminho = Path.cwd()
#print(caminho)

# Navegando até uma pasta específica
caminho = Path('/Users/rafaellacavalcante/Documents/PythonCods/Codigos_hashtag/IntegraçãoPythonPastasPC/Arquivos_Lojas')
#print(caminho)

# Listando todos os arquivos da Pasta Atual
arquivos = caminho.iterdir()

#for arquivo in arquivos:
 #   print(arquivo)

# Verificando se um arquivo existe no computador
if (caminho/Path('202001_Morumbi_SP.csv')).exists():
    print('Arquivo existe na pasta')

# Criando Pastas
#Path('PastaAuxiliar').mkdir()

# Criando Cópia
import shutil
arquivo_copiar = Path((caminho/Path('202001_Morumbi_SP.csv')))
arquivo_colar = Path('PastaAuxiliar')
#shutil.copy2(arquivo_copiar, arquivo_colar)

# Movendo arquivos: 2 formas (.rename ou .move)
#Path((caminho/'202001_Morumbi_SP.csv')).rename(caminho_novo/'202001_Morumbi_SP.csv')

shutil.move('/Users/rafaellacavalcante/PycharmProjects/pythonProject/.venv/CodigosHashtag/PythonArquivosPC/PastaAuxiliar/202001_Morumbi_SP.csv',
'/Users/rafaellacavalcante/PycharmProjects/pythonProject/.venv/CodigosHashtag/PythonArquivosPC/202001_Morumbi_SP.csv')

