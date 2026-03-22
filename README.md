# Cryptocurrency Time-Series Momentum Backtest

A Python-based backtest exploring whether major cryptocurrencies exhibit 
time-series momentum — i.e., whether recent strong performance predicts 
continued strong performance.

## What This Project Does
- Computes daily returns for BTC, ETH, ADA, and BNB since 2016
- Constructs a momentum signal by z-scoring recent 10-day returns 
  against a trailing 365-day baseline
- Clips extreme signal values through a tanh function to generate 
  portfolio weights
- Evaluates strategy performance via annualized Sharpe ratio and 
  cumulative returns
- Analyzes correlation between timing strategies and underlying assets

## Key Findings
- The momentum strategies generate positive Sharpe ratios across all 4 coins
- Strategy returns are largely uncorrelated with raw asset returns, 
  suggesting the strategy captures directional timing rather than 
  passive exposure

## Tools & Libraries
Python, pandas, NumPy, yfinance, matplotlib, seaborn
