import pandas as pd
from typing import List

'''
Função para gerar um único dataframe a partir de um lista de dataframes
    args: 
        df_list (List): estrutura de dados com todas as planilhas em formato dataframe
    return:
        (pd.DataFrame) : Dataframe pandas
'''
def concat_dataframes(df_list: List[pd.DataFrame])-> pd.DataFrame:
    return pd.concat(df_list, ignore_index=True)