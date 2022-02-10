import pandas as pd
import numpy as np


def load_gm(data):
    try:
        df = pd.read_excel(data,
                           skiprows=8,
                           usecols=[0, 1, 2],
                           names=["nazwa-JST", "KOD", "ludnosc"],
                           dtype={'nazwa-JST': str,
                                  'KOD': str,
                                  'ludnosc': np.float64}
                           )
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    else:
        # 0201011 (KOD) -> 020101 (kod)
        # 0201022 (KOD) -> 020102 (kod)
        df['kod'] = df['KOD'].str.slice(stop=6)
        df['value'] = df['KOD'].str.slice(start=6)
        df = df[df["value"].isin(["1", "2", "5"])]
        # Problems with .drop...
        df.drop(['KOD', 'value'], axis=1)
        df.set_index('kod', inplace=True)
        return df


def load_pow(data):
    try:
        df = pd.read_excel(data,
                           skiprows=9,
                           usecols=[0, 1, 2],
                           names=["nazwa-JST", "kod", "ludnosc"],
                           dtype={'nazwa-JST': str,
                                  'kod': str,
                                  'ludnosc': np.float64}
                           )
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    else:
        df = df[df["kod"].notna()]
        df["kod"] = df["kod"] + "00"
        df.set_index('kod', inplace=True)
        return df


def load_woj(data):
    try:
        df = pd.read_excel(data,
                           skiprows=8,
                           usecols=[0, 1],
                           names=["nazwa-JST", "ludnosc"],
                           dtype={'nazwa-JST': str,
                                  'ludnosc': np.int64}
                           )
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    else:
        df["nazwa-JST"] = df["nazwa-JST"].str.upper()
        df.set_index('nazwa-JST', inplace=True)
        return df
