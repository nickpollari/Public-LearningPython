import pandas as pd
import pandas_datareader.data as web
import datetime as dt


#######################
##### 7.1 - Apply #####
#######################

def get_data(ticker, start_dt, end_dt):
    df = web.DataReader(ticker, 'iex', start_dt, end_dt)
    df['ticker'] = ticker
    return df


def get_all_ticker_price_data(ticker_list, start_dt, end_dt):
    ticker_data = dict()

    for ticker in ticker_list:
        ticker_df = get_data(ticker, start_dt, end_dt)
        ticker_data[ticker] = ticker_df

    return ticker_data


def compute_sma(price_series, window_len):
    sma = price_series.rolling(window_len).mean()
    return sma


def establish_position(sma_row, price_row):
    positions = price_row > sma_row
    return positions


#######################
#### 7.2 - Groupby ####
#######################


def create_positions(ticker_data_df):
    ticker_data_df = ticker_data_df.set_index('date')
    sma = ticker_data_df['close'].rolling(20).mean()
    positions = ticker_data_df['close'] > sma
    return positions