import os               # lib para manipular arquivos e pastas
import glob             # lib para listar arquivos 
import pandas as pd 
from typing import List
from pathlib import Path


'''
Função para ler arquivos da pasta data/input e retornar uma lista de dataframes
    args: 
        path_pasta_input (str): caminho para a pasta input com os arquivos
    return:
        (List) : lista de dataframes 
'''
def read_data_input(path: Path) -> List[pd.DataFrame]:
    all_files = list(path.glob("*.xlsx"))               # Buscar todos os arquivos excel na pasta do path

    dataframe_list: List[pd.DataFrame] = []
    for file in all_files:
        dataframe_list.append(pd.read_excel(file))
    
    return dataframe_list

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parents[2]      # a partir de onde o file extract.py está, transforma em caminho absoluto real (resolve symlinks) e sobe 2 níveis de diretório a partir desse arquivo, i.e. para irmos para o root do projeto (ETL-Consolidacao-Planilhas/)
    INPUT_PATH = BASE_DIR / "src" / "data" / "input"    # ou podemos escrever BASE_DIR.joinpath("src").joinpath("data").joinpath("input") 
    
    data_frame_list = read_data_input(INPUT_PATH)       # Caminho a partir do arquivo, não do terminal. Isso evitar confundir o caminho no terminal na hora de executar
    print(data_frame_list)

    # print("CWD:", Path.cwd())
    # print("INPUT EXISTS:", path.exists())
    # print("FILES:", list(path.glob("*.xlsx")))
