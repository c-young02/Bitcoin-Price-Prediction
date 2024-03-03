import matplotlib.pyplot as plt


def print_dataframe_info(df):
    """
    Prints information about the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to print information about.
    """
    print("Shape of the DataFrame:")
    print(df.shape)

    print("First few rows of the DataFrame:")
    print(df.head())

    print("Last few rows of the DataFrame:")
    print(df.tail())

    print("DataFrame Info:")
    print(df.info())

    print("DataFrame Description:")
    print(df.describe())

    print("Number of missing values in each column:")
    print(df.isnull().sum())


def plot_data(df, column, title, xlabel, ylabel):
    """
    Plots data from a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to plot data from.
        column (str): The column to plot.
        title (str): The title of the plot.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.
    """
    df[column].plot()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def exploration(df):
    """
    Performs data exploration and visualization on the given DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to be explored.
    """
    print_dataframe_info(df)

    # Set the 'Date' column as the index
    df.set_index("Date", inplace=True)

    # Plot 'Close' prices over 'Date'
    plot_data(df, "Close", "Close Prices Over Time", "Date", "Close Price")
