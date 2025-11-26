import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def moving_averages(closing_data, sma_20, ema_20):
    plt.figure(figsize=(14,7))
    plt.plot(closing_data, label='Close price', color='r', alpha=0.8, linewidth=3)
    plt.plot(sma_20, label='SMA 20', color="b", alpha=0.6,linewidth=3)
    plt.plot(ema_20, label='EMA 20', color="#70390688",linewidth=3)
    plt.title('Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def rsi_plot(rsi):
    plt.figure(figsize=(14,7))
    plt.plot(rsi, label='RSL', color='purple')
    plt.axhline(70, color='red', linestyle='--')
    plt.axhline(30, color='green', linestyle='--')
    plt.title('Relative Strength Index (RSI)')
    plt.show()
def cumulative(cumulative_returns):
    plt.figure(figsize=(14,6))
    plt.plot(cumulative_returns, label='Cumulative Return', color='blue')
    plt.title('Cumulative Returns Over Time')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.legend()
    plt.show()
def daily_returns(returns):
    plt.figure(figsize=(14,7))
    plt.plot(returns, label=' Return', color='gold')
    plt.title('Percentage change of stock price')
    plt.xlabel('Date')
    plt.ylabel('daily Return')
    plt.legend()
    plt.show()
def macd_result(macd, macd_signal, macd_hist):
    plt.figure(figsize=(14,7))
    plt.plot(macd, label='MACD', color='r')
    plt.plot(macd_signal, label='MACD_Signal', color="b" )
    plt.plot(macd_hist, label='MACD_Hist', color="GREEN")
    plt.title('Moving Average Convergence Divergence')
    plt.xlabel('Trading Date')
    plt.ylabel('MACD / Signal / Histogram')
    plt.legend()
    plt.show()
def correlation_map(corr_data):
    
    mask = np.zeros_like(corr_data)
    upper_triangle = np.triu_indices_from(mask)
    mask[upper_triangle] = True
    plt.figure(figsize=(14,7))
    sns.heatmap(data=corr_data, mask=mask, annot=True)
    plt.show()
