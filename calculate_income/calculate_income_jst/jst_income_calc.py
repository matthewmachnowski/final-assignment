from .load_data import load
import numpy as np


def income_jst(input_file):
    df = load.load(input_file)
    # Participation of territorial self-government units in PIT (percentages).
    participation_dict = {"75634": 5,
                          "75623": 1.6,
                          "75622": 10.25,
                          "75621": 39.34,
                          }

    for code, percent in participation_dict.items():
        df.loc[df["rozdzial"] == code, ["dochod-z-PIT"]] = (df["wplaty"] * 100 / percent)

    agg_func_mean = {'dochod-z-PIT': np.mean}
    data_calc = df.groupby(['kod']).agg(agg_func_mean)
    df = df[["kod", "nazwa-JST", "WK", "PK", "GK", "rodzaj-JST"]].drop_duplicates()
    df.set_index('kod', verify_integrity=True, inplace=True)
    df = df.join(data_calc, how='inner')
    return df


# First the data from 2019, then 2020.
def income_comparison(file1, file2):
    df1 = income_jst(file1)
    df2 = income_jst(file2)
    df1 = df1.rename(columns={'dochod-z-PIT': 'dochod-2019'})
    df2 = df2.rename(columns={'dochod-z-PIT': 'dochod-2020'})
    df1 = df1["dochod-2019"]
    df = df2.join(df1, how='inner')
    df['roznica-wzgl-poprz-roku'] = (df['dochod-2020'] - df['dochod-2019'])
    return df
