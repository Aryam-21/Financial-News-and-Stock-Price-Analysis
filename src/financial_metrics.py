
# pynance can fail to import on newer Pythons if 'distutils' is missing.
# We try to import it and provide a helpful message if it fails.
try:
    from pynance import stats
    def financial_metrics(closing_data):
        returns = stats.returns(closing_data)
        cumulative_returns = (1 + returns).cumprod()
        volatility = stats.volatility(closing_data)
        return returns,cumulative_returns,volatility
except Exception as e:
    pn = None
    def financial_metrics(closing_data):
        returns = closing_data.pct_change()
        cumulative_return = (1+returns).cumprod()
        volatility = returns.std()*(252**0.5)
        return returns,cumulative_return, volatility