import pandas as pd
import numpy as np


def load(data):
    try:
        df = pd.read_excel(data,
                           skiprows=6,
                           usecols=[0, 1, 2, 4, 8, 9, 11],
                           names=["WK", "PK", "GK", "nazwa-JST", "rozdzial", "paragraf", "wplaty"],
                           dtype={'WK': str,
                                  'PK': str,
                                  'GK': str,
                                  'nazwa-JST': str,
                                  'rozdzial': str,
                                  'paragraf': str,
                                  'wplaty': np.float64}
                           )
        load_test(df)
    except AssertionError as error:
        print(error)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    else:
        for col in ["PK", "GK"]:
            df.loc[df[col] == "-", [col]] = "00"

        df["kod"] = (df["WK"] + df["PK"] + df["GK"])
        df["nazwa-JST"] = df["nazwa-JST"].str.upper()

        code_dict = {"['75621']": "gmina",
                     "['75622']": "powiat",
                     "['75634']": "metropolia",
                     "['75623']": "wojewodztwo",
                     "['75621', '75622']": "miasto npp",
                     }

        chapter_jst = str(list(df["rozdzial"].drop_duplicates()))
        df["rodzaj-JST"] = code_dict[chapter_jst]
        return df


def load_test(data):
    assert np.all(data["paragraf"] == "0010"), "TO NIE SĄ DANE DLA PIT."
