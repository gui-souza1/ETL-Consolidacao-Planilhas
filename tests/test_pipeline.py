import pandas as pd
from src.pipeline.transform import concat_dataframes


def teste_concatenacao_lista_dataframes():
    # Arrange
    df_1 = pd.DataFrame({"id": [1, 2], "value": [10, 20]})
    df_2 = pd.DataFrame({"id": [3], "value": [30]})
    arrange = pd.concat([df_1, df_2], ignore_index=True)

    # Act
    act = concat_dataframes([df_1, df_2])

    # Assert
    assert arrange.equals(act)
    