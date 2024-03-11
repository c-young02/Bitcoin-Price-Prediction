import pandas as pd
import numpy as np
import plotly.express as px
from itertools import cycle
import plotly.io as pio

# Set the default template for plots
pio.templates.default = "plotly_white"
pio.templates["plotly_white"]["layout"]["plot_bgcolor"] = "white"
pio.templates["plotly_white"]["layout"]["xaxis"]["showgrid"] = False
pio.templates["plotly_white"]["layout"]["yaxis"]["showgrid"] = False

# Set the default layout updates
pio.templates["plotly_white"]["layout"]["font"] = {"size": 15, "color": "black"}


def plot_data(df, title):
    """
    Helper function to plot the 'Close' column against the 'Date' column.
    """
    fig = px.line(df, y="Close", x="Date", title=title)
    fig.show()


def plot_close(stock_data):
    """
    Function to plot the 'Close' column against the 'Date' column for the whole period and for the period after '2020-02-29'.
    :param stock_data: DataFrame containing the 'Close' and 'Date' columns
    """
    plot_data(stock_data, "Whole period of timeframe of Bitcoin close price 2014-2024")

    # Filter the DataFrame for dates after '2020-02-29'
    filtered_data = stock_data[stock_data["Date"] > "2020-02-29"]
    plot_data(filtered_data, "Bitcoin close price after 2020-02-29")


def plot_loss(history):
    """
    Function to plot the training and validation loss over each epoch.
    :param history: History object returned by the `fit` method of the model
    """
    # Extract loss and validation loss values
    loss = history.history["loss"]
    val_loss = history.history["val_loss"]

    # Generate range of epochs
    epochs = range(len(loss))

    # Create a DataFrame for plotting
    df = pd.DataFrame(
        {
            "Epoch": list(epochs) * 2,
            "Loss": loss + val_loss,
            "Type": ["Training loss"] * len(loss) + ["Validation loss"] * len(val_loss),
        }
    )

    # Plot training and validation loss
    fig = px.line(
        df, x="Epoch", y="Loss", color="Type", title="Training and validation loss"
    )
    fig.show()


def plot_predictions(df, train_predict, val_predict, test_predict, close_stock, time_step):
    """
    Function to plot the original close price, train predicted close price, validation predicted close price, and test predicted close price.

    Args:
        df: DataFrame containing the original data.
        train_predict: Array containing the train predicted data.
        val_predict: Array containing the validation predicted data.
        test_predict: Array containing the test predicted data.
        close_stock: DataFrame containing the original 'Date' and 'Close' columns.
        time_step: The number of past days' data to consider for the prediction.
    """

    # Shift train predictions for plotting
    look_back = time_step
    trainPredictPlot = np.empty_like(df)
    trainPredictPlot[:, :] = np.nan
    trainPredictPlot[look_back : len(train_predict) + look_back, :] = train_predict

    # Shift validation predictions for plotting
    valPredictPlot = np.empty_like(df)
    valPredictPlot[:, :] = np.nan
    valPredictPlot[len(train_predict) + (look_back * 2): len(train_predict) + len(val_predict) + (look_back * 2),
    :] = val_predict

    # Shift test predictions for plotting
    testPredictPlot = np.empty_like(df)
    testPredictPlot[:, :] = np.nan
    start_index = len(train_predict) + len(val_predict) + (look_back * 3)
    end_index = start_index + len(test_predict)

    # Assign test predictions to the correct slice of testPredictPlot
    testPredictPlot[start_index:end_index, :] = test_predict

    # Prepare data for plotting
    names = cycle(
        [
            "Original close price",
            "Train predicted close price",
            "Validation predicted close price",
            "Test predicted close price",
        ]
    )

    plotdf = pd.DataFrame(
        {
            "date": close_stock["Date"],
            "original_close": close_stock["Close"],
            "train_predicted_close": trainPredictPlot.reshape(1, -1)[0].tolist(),
            "validation_predicted_close": valPredictPlot.reshape(1, -1)[0].tolist(),
            "test_predicted_close": testPredictPlot.reshape(1, -1)[0].tolist(),
        }
    )

    # Create a line plot comparing original close price vs predicted close price
    fig = px.line(
        plotdf,
        x=plotdf["date"],
        y=[
            plotdf["original_close"],
            plotdf["train_predicted_close"],
            plotdf["validation_predicted_close"],
            plotdf["test_predicted_close"],
        ],
        labels={"value": "Stock price", "date": "Date"},
    )
    fig.update_layout(
        title_text="Comparision between original close price vs predicted close price",
        plot_bgcolor="white",
        font_size=15,
        font_color="black",
        legend_title_text="Close Price",
    )
    fig.for_each_trace(lambda t: t.update(name=next(names)))

    # Update plot aesthetics
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    # Display the plot
    fig.show()
