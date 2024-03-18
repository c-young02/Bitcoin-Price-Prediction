import numpy as np
import plotly.graph_objects as go
import os
import joblib

# Get the directory where the current script is located
current_dir = os.path.dirname(os.path.realpath(__file__))

# Define the absolute path to the scaler.gz file
scaler_path = os.path.join(current_dir, "data", "scaler.gz")

# Load the scaler from the saved file
scaler = joblib.load(scaler_path)


def predict_price(model, bitcoin_data):
    """
    Predicts the price 14 days into the future based on the last 60 days' closing prices.

    Args:
        model: The trained model.
        bitcoin_data: An array of the last 60 days' closing prices.

    Returns:
        The predicted price 14 days into the future.
    """
    # Scale the last 60 days' data using the preloaded scaler
    bitcoin_data_scaled = scaler.transform(bitcoin_data.values.reshape(-1, 1))

    # Reshape the data into the required shape for the model
    bitcoin_data_scaled = np.reshape(bitcoin_data_scaled, (1, 60, 1))

    # Use the model to predict the price 14 days into the future
    predicted_price = model.predict(bitcoin_data_scaled)

    # Inverse transform the predicted price to get it back to the original scale
    predicted_price = scaler.inverse_transform(predicted_price)

    return predicted_price


def create_trace(x, y, mode, name, marker=None):
    """
    Helper function to create a Scatter trace.
    """
    return go.Scatter(x=x, y=y, mode=mode, name=name, marker=marker)


def predict_price_plot(predicted_price, bitcoin_data):
    """
    Plots the past 60 days' closing prices, an exponential fit line,
    and a predicted price line.

    Args:
        predicted_price: The predicted price 14 days into the future.
        bitcoin_data: An array of the last 60 days' closing prices.
    """
    # Define the days for the plot
    days = np.arange(1, 75)  # Extend the days to 74

    # Define the future_days for the plot
    future_days = np.arange(60, 75)  # Start from day 60 and end at day 74

    # Extract the single predicted price value from the array
    predicted_price_value = predicted_price[0][0]

    # Create a line from the last day to the predicted day
    predicted_price_line = np.linspace(
        bitcoin_data.iloc[-1], predicted_price_value, len(future_days)
    )

    # Fit an exponential function to the last 60 days and extend it to 74 days
    coeffs = np.polyfit(np.arange(1, 61), np.log(bitcoin_data), 1)
    exponential_fit_line = np.exp(coeffs[1]) * np.exp(coeffs[0] * days)

    # Create traces for the plot
    trace1 = create_trace(
        np.arange(1, 61), bitcoin_data, "lines+markers", "Past 60 days"
    )
    trace2 = create_trace(days, exponential_fit_line, "lines", "Exponential fit")
    trace3 = create_trace(
        future_days,
        predicted_price_line,
        "lines+markers",
        "Predicted price",
        marker=dict(size=[0] * 14 + [10]),
    )

    # Create a layout for the plot
    layout = go.Layout(
        title="Price vs Day", xaxis=dict(title="Day"), yaxis=dict(title="Price")
    )

    # Create a figure and add the traces
    fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)

    # Show the figure
    fig.show()
