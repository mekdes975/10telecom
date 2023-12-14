import missingno as msno 
import matplotlib.pyplot as plt 
import pandas as pd
from sqlalchemy import create_engine
import sys 
import os 
import numpy as np 
import seaborn as sns 
import sys, os

import logging
from scipy.stats.mstats import winsorize

import re 


current_directory = os.getcwd()
parent_directory = os.path.abspath(os.path.join(current_directory, '..'))

if parent_directory not in sys.path:
    sys.path.insert(0, parent_directory)


from utils import percent_missing, format_float, find_agg, missing_values_table,convert_bytes_to_megabytes,fix_missing_ffill,fix_missing_bfill


class DataFrameInformation:
    
    def __init__(self,data:pd.DataFrame):
        self.data = data
        logging.basicConfig(filename='../logfile.log', filemode='a',
                            encoding='utf-8', level=logging.DEBUG)
        
    #calculate the skewness of the dataframe first
    def get_skewness(self,data:pd.DataFrame):
        skewness = data.skew(axis=0, skipna=True)
        df_skewness = pd.DataFrame(skewness)
        df_skewness = df_skewness.rename(
            columns={0: 'skewness'})
        
        return df_skewness
       #calculate skewness and missing value table
    def get_skewness_missing_count(self,data:pd.DataFrame):
        df_skewness = self.get_skewness(data)
        minfo = MissingInformation(data)
        
        mis_val_table_ren_columns = minfo.missing_values_table(data)
        df = pd.concat([df_skewness, mis_val_table_ren_columns], axis=1)
        df['Dtype'] = df['Dtype'].fillna('float64')
        df['% of Total Values'] = df['% of Total Values'].fillna(0.0)
        df['Missing Values'] = df['Missing Values'].fillna(0)
        df = df.sort_values(by='Missing Values', ascending=False)
        return df

    def get_column_with_string(self,df: pd.DataFrame, text):
        return [col for col in df.columns if re.findall(text, col) != []]
    
    def get_dataframe_information(self,df: pd.DataFrame):
        columns = []
        counts = []
        i = 0

        for key, item in df.isnull().sum().items():
            if item != 0:
                columns.append(key)
                counts.append(item)
                i += 1
        logging.info(
            'the dataset contain {} columns with missing values'.format(i))
        return pd.DataFrame({'column name': columns, 'counts': counts})
    