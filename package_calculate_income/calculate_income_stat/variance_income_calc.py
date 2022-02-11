import numpy as np
import pandas as pd


def income_variance_gm(file1, file2):
    file1["powiat"] = file1['WK'] + file1["PK"] + "00"
    agg_func = {'sredni-opod-doch': [np.mean, np.std]}
    df1 = file1.groupby(['powiat']).agg(agg_func)
    df2 = calculations(df1, file2)
    return df2


def income_variance_pow(file1, file2):
    file1["wojewodztwo"] = file1['WK'] + "0000"
    agg_func = {'sredni-opod-doch': [np.mean, np.std]}
    df1 = file1.groupby(['wojewodztwo']).agg(agg_func)
    df2 = calculations(df1, file2)
    return df2


def calculations(df1, file2):
    data = file2.join(df1, how='inner')
    data['por_mean'] = abs((data['sredni-opod-doch'] -
                            data['sredni-opod-doch', 'mean'])) / data['sredni-opod-doch', 'mean']
    return data
