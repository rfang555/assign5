import streamlit as st
import yfinance as yf

# Define the ticker and monthly risk-free rate
ticker = "MSFT"
rf_monthly = 0.0025  # 0.25% per month

# Title of the application
st.title("Microsoft (MSFT) 5-Year Sharpe Ratio")

# Download 5 years of monthly MSFT stock prices
data = yf.Ticker(ticker).history(period="5y", interval="1mo")

if not data.empty:
    # Extract monthly closing prices
    close_prices = data["Close"]

    # Calculate monthly stock returns
    monthly_returns = close_prices.pct_change().dropna()

    if len(monthly_returns) >= 2 and monthly_returns.std() > 0:
        # Calculate monthly excess returns
        excess_returns = monthly_returns - rf_monthly

        # Calculate average excess return
        mean_excess_return = excess_returns.mean()

        # Calculate standard deviation of returns
        std_dev_return = monthly_returns.std()

        # Calculate monthly Sharpe Ratio
        monthly_sharpe_ratio = mean_excess_return / std_dev_return

        # Display the result in Streamlit
        st.metric(
            label="Monthly Sharpe Ratio",
            value=f"{monthly_sharpe_ratio:.3f}"
        )
    else:
        st.error("Not enough monthly returns to calculate the Sharpe Ratio.")
else:
    st.error("No data found for MSFT.")
