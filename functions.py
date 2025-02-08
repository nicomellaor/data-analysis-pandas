import numpy as np
import pandas as pd

def calculate_outliers(df_column):
    Q1 = np.percentile(df_column, 25)
    Q3 = np.percentile(df_column, 75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = (df_column < lower) | (df_column > upper) #array of boolean values
    return outliers

def count_outliers(df_column):
    return calculate_outliers(df_column).sum() #counts True values

def calculate_iqr(df):
    df_nums = df.select_dtypes(include=np.number)
    Q1 = df_nums.quantile(0.25)
    Q3 = df_nums.quantile(0.75)
    return Q3 - Q1 #return a Series/DF

def replace_nulls(df, column, value):
    for x in df.index:
        if np.isnan(df.loc[x, column]):
            df.loc[x, column] = value
    return df

def remove_nulls(df, column):
    for x in df.index:
        if np.isnan(df.loc[x, column]):
            df.drop(x, inplace=True)
    return df

def change_to_datetime(df, column):
    #fix format DD-MM-YYYY to YYYY-MM-DD
    for i in range(len(df[column])):
        if(len(df.at[i,column].split("-")[0])!=4):
            df.at[i,column]="-".join((df.at[i,column].split("-"))[::-1])
        else:
            continue
    df[column] = pd.to_datetime(df[column], errors="coerce")
    return df

def count_inconsistent_ages(df, column):
    condition = (df[column] > 100) | (df[column] < 0)
    return condition.sum()

def replace_ages(df, column, value):
    for x in df.index:
        if (df.loc[x, column] > 100) | (df.loc[x, column] < 0):
            df.loc[x, column] = value
    return df

def remove_ages(df, column):
    for x in df.index:
        if (df.loc[x, column] > 100) | (df.loc[x, column] < 0):
            df.drop(x, inplace=True)
    return df