# Main used for local testing only.

import pandas as pd
from datetime import datetime
from datapull import data_pull_csv
from preprocess import preprocess
from eda import perform_eda
from feateng import *
from offload import *


file = '../data/data-log.csv'

def main():
  # data pull
  df = data_pull_csv(file)

  # eda
  perform_eda(df)

  # data preprocessing
  df = preprocess(df)

  # feature engineering
  df_new = feateng(df)

  # data offload
  data_offload_csv(df_new)

  return df_new
  
  

if __name__ == "__main__":
    print("Starting processing of data.")
    main()
    print("Completed")
