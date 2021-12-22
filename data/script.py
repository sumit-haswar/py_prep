import pandas as pd
import ast
from pandas import DataFrame


def load_dataframe(file_path: str) -> DataFrame:
    df = pd.read_excel(file_path, engine='openpyxl')

    playcount_column = []

    # iterate through data-frame rows
    for index, row in df.iterrows():
        cell_value = row['spotifyTracks']
        cell_dict = ast.literal_eval(cell_value)
        playcount_value = cell_dict["playcount"]
        playcount_column.append(playcount_value)

    # add new column with data to data-frame
    df['playcount'] = playcount_column

    return df


if __name__ == '__main__':
    df = load_dataframe('/Users/sumithaswar/Desktop/sample.xlsx')
    print(df)
