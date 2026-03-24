# Install required Librarys
import yfinance as yf 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Download financial data on ADA-USD, BNB-USD, BTC-US, ETH-USD from Yahoo Finance.
# Compute returns for these coins since 2016.
data = yf.download(['ADA-USD','BNB-USD','BTC-USD','ETH-USD'],'2016-1-1')
ret = data['Close'] / data['Close'].shift() - 1

# The signal on each day for each coin will be: sqrt(10)*(avg past 10 day ret - avg past 365 day ret) / (stdev past 365 day ret). 
# You can think of this as the z-score of the past 10 day returns, and it tells us if a coin is doing better than it usually does. 
signal = np.sqrt(10) * (ret.rolling(10).mean() - ret.rolling(365).mean()) / ret.rolling(365).std()

# The signal will have extreme values. 
# Pass them through a tanh function to curtail these. These are final daily portfolio weights.
weights = np.tanh(signal)

# 4. Compute the returns to the weights from previous step.
weighted_returns = ret * weights.shift(1)
print(weighted_returns)


# Calculate weighted_sharpe, plot weighted returns.
weighted_sharpe = (weighted_returns.mean() / weighted_returns.std()) * np.sqrt(365)
cum_weighted_returns = (1 + weighted_returns).cumprod()
cum_weighted_returns.plot()
plt.show()

# Check correlation between base returns and strategy returns.
corr = pd.concat([ret.add_suffix('_raw'), weighted_returns.add_suffix('_strategy')], axis=1)
corr = corr.corr()
print(corr)
print(weighted_sharpe)
