from extract import read_data_input    # com o arquivo __init__.py agora o Python reconhece nosso arquivo extract.py como módulo
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]  # a partir de onde o file extract.py está, transforma em caminho absoluto real (resolve symlinks) e sobe 2 níveis de diretório a partir desse arquivo, i.e. para irmos para o root do projeto (ETL-Consolidacao-Planilhas/)
INPUT_PATH = BASE_DIR / "src" / "data" / "input"

dfs = read_data_input(INPUT_PATH)
print(dfs)