import joblib
import numpy as np
import plotly.graph_objects as go

# Load the scaler from the saved file
scaler = joblib.load("./data/scaler.gz")


def predict_price(model, last_30_days):
    """
    Predicts the price 14 days into the future based on the last 30 days' closing prices.

    Args:
        model: The trained model.
        last_30_days: An array of the last 30 days' closing prices.

    Returns:
        The predicted price 14 days into the future.
    """
    # Scale the last 30 days' data using the pre-loaded scaler
    last_30_days_scaled = scaler.transform(last_30_days.reshape(-1, 1))

    # Reshape the data into the required shape for the model
    last_30_days_scaled = np.reshape(last_30_days_scaled, (1, 30, 1))

    # Use the model to predict the price 14 days into the future
    predicted_price = model.predict(last_30_days_scaled)

    # Inverse transform the predicted price to get it back to the original scale
    predicted_price = scaler.inverse_transform(predicted_price)

    return predicted_price


def create_trace(x, y, mode, name, marker=None):
    """
    Helper function to create a Scatter trace.
    """
    return go.Scatter(x=x, y=y, mode=mode, name=name, marker=marker)


def predict_price_plot(predicted_price, last_30_days):
    """
    Plots the past 30 days' closing prices, an exponential fit line,
    and a predicted price line.

    Args:
        predicted_price: The predicted price 14 days into the future.
        last_30_days: An array of the last 30 days' closing prices.
    """
    # Define the days for the plot
    days = np.arange(1, 45)  # Extend the days to 44

    # Define the future_days for the plot
    future_days = np.arange(30, 45)  # Start from day 30 and end at day 44

    # Extract the single predicted price value from the array
    predicted_price_value = predicted_price[0][0]

    # Create a line from the last day to the predicted day
    predicted_price_line = np.linspace(
        last_30_days[-1], predicted_price_value, len(future_days)
    )

    # Fit an exponential function to the last 30 days and extend it to 44 days
    coeffs = np.polyfit(np.arange(1, 31), np.log(last_30_days), 1)
    exponential_fit_line = np.exp(coeffs[1]) * np.exp(coeffs[0] * days)

    # Create traces for the plot
    trace1 = create_trace(
        np.arange(1, 31), last_30_days, "lines+markers", "Past 30 days"
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
