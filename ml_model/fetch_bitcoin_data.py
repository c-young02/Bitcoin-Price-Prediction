import yfinance as yf
from datetime import datetime, timedelta


def fetch_data(ticker_symbol='BTC-USD', days=60):
    """
    Fetches the closing prices for a given ticker symbol for a specified number of days.

    Parameters:
    ticker_symbol (str): The ticker symbol to fetch data for. Defaults to 'BTC-USD'.
    days (int): The number of past days to fetch data for. Defaults to 30.

    Returns:
    pandas.Series: A pandas Series object containing the closing prices for the specified ticker symbol for the past 'days' days.

    Raises:
    Exception: If an error occurs while fetching the data.
    """
    try:
        # Calculate the start and end dates for the data fetch
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days-1)

        # Fetch the data using the yfinance download method
        data = yf.download(ticker_symbol, start=start_date, end=end_date)

        # Extract the 'Close' column from the fetched data
        close = data['Close']

        # Return the closing prices
        return close
    except Exception as e:
        # Print the error message and return None if an error occurs
        print(f"An error occurred while fetching data: {e}")
        return None
