import pandas as pd

file = '../data/data-log.csv'

def data_pull_csv(file):
  df = pd.read_csv(file)
  return df

# TODO:
# instantiate table with BigQuery, connect, read, pull.


# if __name__ == "__main__":
#   data_pull_csv(file)
#   print("Starting data pull from csv of cdn data.")