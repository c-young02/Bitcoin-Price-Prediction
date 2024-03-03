import os
import pandas as pd


def load_data(dataset):
    """
    Loads the data from the given dataset file into a pandas DataFrame.

    Args:
        dataset (str): The name of the dataset file located in the same directory as this script.

    Returns:
        pd.DataFrame: The loaded data if the file exists.

    Raises:
        FileNotFoundError: If the dataset file does not exist.
        ValueError: If the dataset parameter is not a string.
    """

    # Define the directory that this script is in
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Construct the path to the dataset file
    file_path = os.path.join(script_dir, dataset)

    # Check that the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The dataset file {file_path} does not exist.")

    # Load the data from the dataset file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Return the loaded data
    return df
