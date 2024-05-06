import pandas as pd


def preprocess(df):
  df = df.rename(columns={'date': 'Date', 'time': 'Timestamp', 'sac_status':'SacStatus', 'device': 'HardwareDevice', 'node_ID':'ContentAsset', 'anon_ip': 'ClientIp', 'anon_cs_user_agent': 'ClientDevice'})
  return df

# if __name__ == "__main__":
#   preprocess(df)
#   print("Starting preprocessing of cdn data.")