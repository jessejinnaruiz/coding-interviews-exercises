# from pandas_profiling import ProfileReport
import pandas as pd


def perform_eda(df):
  print(df.columns)
  print(df.info())
  print(df.shape)
  print(df.isnull().sum())
  print(df.nunique())

# prof = ProfileReport(df)
# prof.to_file(output_file='output.html')
# prof.to_notebook_iframe()

