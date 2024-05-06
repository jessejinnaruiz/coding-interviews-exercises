import pandas as pd
from datetime import datetime

t = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
offload_file = f'../data/output-{t}.csv'


def data_offload_csv(df):
    print('Offloading csv file')
    df.to_csv(offload_file)