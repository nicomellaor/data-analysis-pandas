import pandas as pd

class DataAnalysis:
    def __init__(self, file):
        self.__df = pd.read_csv(file)

    def get_df(self):
        return self.__df
    
    def set_df(self, df):
        self.__df = df