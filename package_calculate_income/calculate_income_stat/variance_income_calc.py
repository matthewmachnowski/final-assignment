import numpy as np


def income_variance_gm(file1, file2):
    file1["powiat"] = file1['WK'] + file1["PK"] + ["00"]
    df1 = file1.groupby(['powiat']).agg({'sredni-doch-opod': [np.mean, np.std]})
    df2 = calculations(df1, file2)
    return df2


def income_variance_pow(file1, file2):
    file1["wojewodztwo"] = file1['WK'] + ["0000"]
    df1 = file1.groupby(['wojewodztwo']).agg({'sredni-doch-opod': [np.mean, np.std]})
    df2 = calculations(df1, file2)
    return df2


def calculations(df1, file2):

