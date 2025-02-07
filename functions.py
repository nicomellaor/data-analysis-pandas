import numpy as np

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

def replace_nulls(df_column, value):
    pass

def remove_nulls(df_column):
    pass

def change_to_datetime(df_column):
    # fix date format
    pass

def count_inconsistent_ages(df_column):
    pass

def replace_ages(df_column, value):
    pass

def remove_ages(df_column):
    pass