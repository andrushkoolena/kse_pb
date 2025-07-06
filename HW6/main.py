import yfinance as yf
import pandas as pd
data = yf.download("AAPL", start="2015-01-01", end="2025-01-01")
data.dropna(inplace=True) 
data['SMA10'] = data['Close'].rolling(window=10).mean()
data['SMA50'] = data['Close'].rolling(window=50).mean()
data['Signal'] = 0
data.loc[data['SMA10'] > data['SMA50'], 'Signal'] = 1
#в такому випадку покупка, бо short moving average> long moving average
data.loc[data['SMA10'] <= data['SMA50'], 'Signal'] = -1
#в цьому випадку це сигнал на продаж
display(data)
#інше я не зрозуміла ;(