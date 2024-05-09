import pandas as pd
from datetime import datetime


def add_year(df, column):
    return df[column].dt.year


def add_quarter(df, column):
    return df[column].dt.quarter


def add_month(df, column):
    return df[column].dt.month


def add_day(df, column):
    return df[column].dt.day


def add_hour(df, column):
    return df[column].dt.hour


def add_weekday(df, column):
#     df['weekday'] = ((pd.DatetimeIndex(df.index).dayofweek) // 5 == 1).astype(float)
#     df['weekday'] = 
    return ((pd.DatetimeIndex(df[column]).weekday) // 5 == 1).astype(float)


def add_date_columns(df, column):
    df['year'] = add_year(df, column)
    df['quarter'] = add_quarter(df, column)
    df['month'] = add_month(df, column)
    df['day'] = add_day(df, column)
    df['hour'] = add_hour(df, column)
    df['weekday'] = add_weekday(df, column)
    return df


def is_tv_show(df):
    df['is_tv_show'] = df.original_title.str.match(r"^S\d+\sE\d+\s\-\s")
    return df


def tv_series_expand(df):
    df[['season', 'episode', 'series']] = df.original_title.str.extract(r"^S(?P<season>\d+)\sE(?P<episode>\d+)\s\-\s(?P<series_title>.*)")
    return df


def timediff(x):
  return x.max() - x.min()


def calc_timediff(df):
  df = df.assign(watchTimeByContentAsset=df.groupby(['ContentAsset']).DateTimeStamp.transform(timediff), 
  watchTimeByClientDevice=df.groupby(['ClientDevice']).DateTimeStamp.transform(timediff),
  watchTimeByClientIp=df.groupby(['ClientIp']).DateTimeStamp.transform(timediff), 
  watchTimeBySeries=df.groupby(['series']).DateTimeStamp.transform(timediff))
  return df


def calc_avgwatch(df):
    df_tv_avg = df[df['is_tv_show'] ==True].groupby(['series'])['watchTimeBySeries'].mean().rename('AverageWatchTime').reset_index()
    df = df.merge(df_tv_avg, how='left', left_on='series', right_on='series')
    return df


def feateng(df):
    df['DateTimeStamp'] = df.Date +" "+ df.Timestamp
    df['DateTimeStamp'] = pd.to_datetime(df.DateTimeStamp)
    df_new = is_tv_show(df)
    df_new = tv_series_expand(df_new)
    df_new = calc_timediff(df_new)
    df_new = add_date_columns(df_new, 'DateTimeStamp')
    df_new = calc_avgwatch(df_new)
    return df_new


# if __name__ == "__main__":
#   feateng(df)
#   print("Starting feature engineering of data.")
