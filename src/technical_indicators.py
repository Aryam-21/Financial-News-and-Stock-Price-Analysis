
import talib as ta

def technical_analysis(closing_data):
    sma_20 = ta.SMA(closing_data, timeperiod=20)
    ema_20 = ta.EMA(closing_data, timeperiod=20)
    rsl = ta.RSI(closing_data, timeperiod=14)
    macd,macd_signal, macd_hist = ta.MACD(closing_data, fastperiod=12, slowperiod=26, signalperiod=9)
    return sma_20,ema_20,rsl,macd,macd_signal,macd_hist