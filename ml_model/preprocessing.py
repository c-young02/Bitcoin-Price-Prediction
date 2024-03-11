import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib

# Initialize MinMaxScaler with feature range of 0 to 1
scaler = MinMaxScaler(feature_range=(0, 1))


def preprocessing(df, time_step=30, future_step=14):
    """
    Preprocesses the given DataFrame for model training.

    Args:
        df: DataFrame containing the 'Date' and 'Close' columns.
        time_step: The number of past days' data to consider for the prediction.
        future_step: The number of future days to predict.

    Returns:
        df: Preprocessed DataFrame.
        close_stock: DataFrame containing the original 'Date' and 'Close' columns.
        x_train: Training data features.
        y_train: Training data labels.
        x_test: Test data features.
        y_test: Test data labels.
    """
    # Set the 'Date' column as the index and reset the index
    df.set_index("Date", inplace=True)
    df.reset_index(inplace=True)

    # Keep only the 'Date' and 'Close' columns
    df = df[["Date", "Close"]]
    df = df[df["Date"] > "2020-02-29"]
    close_stock = df.copy()
    print("Total data for prediction: ", df.shape[0])
    # Delete the 'Date' column and normalize the remaining data using MinMax Scaler
    del df["Date"]
    df = scaler.fit_transform(np.array(df).reshape(-1, 1))
    joblib.dump(scaler, "./data/scaler.gz")

    # Split the data into training, validation, and test sets
    training_size = int(len(df) * 0.60)
    validation_size = int(len(df) * 0.20)
    test_size = len(df) - training_size - validation_size
    train_data, val_data, test_data = df[0:training_size, :], df[training_size:training_size+validation_size, :], df[training_size+validation_size:len(df), :1]

    # Convert an array of values into a dataset matrix
    def create_dataset(dataset, time_step, future_step):
        datax, datay = [], []
        for i in range(len(dataset) - time_step - future_step):
            a = dataset[i : (i + time_step), 0]
            datax.append(a)
            datay.append(dataset[i + time_step + future_step - 1, 0])
        return np.array(datax), np.array(datay)

    # Create datasets for training, validation, and test data
    x_train, y_train = create_dataset(train_data, time_step, future_step)
    x_val, y_val = create_dataset(val_data, time_step, future_step)
    x_test, y_test = create_dataset(test_data, time_step, future_step)

    # Reshape input to be [samples, time steps, features] which is required for LSTM
    x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], 1)
    x_val = x_val.reshape(x_val.shape[0], x_val.shape[1], 1)
    x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], 1)

    return df, close_stock, x_train, y_train, x_val, y_val, x_test, y_test


def transform(train_predict, val_predict, test_predict, y_train, y_val, y_test):
    """
    Transforms the predicted and original values back to their original scale.

    Args:
        train_predict: Predicted values for the training data.
        val_predict: Predicted values for the validation data.
        test_predict: Predicted values for the test data.
        y_train: Original values for the training data.
        y_val: Original values for the validation data.
        y_test: Original values for the test data.

    Returns:
        train_predict: Transformed predicted values for the training data.
        val_predict: Transformed predicted values for the validation data.
        test_predict: Transformed predicted values for the test data.
        original_ytrain: Transformed original values for the training data.
        original_yval: Transformed original values for the validation data.
        original_ytest: Transformed original values for the test data.
    """
    train_predict = scaler.inverse_transform(train_predict)
    val_predict = scaler.inverse_transform(val_predict)
    test_predict = scaler.inverse_transform(test_predict)
    original_ytrain = scaler.inverse_transform(y_train.reshape(-1, 1))
    original_yval = scaler.inverse_transform(y_val.reshape(-1, 1))
    original_ytest = scaler.inverse_transform(y_test.reshape(-1, 1))
    return train_predict, val_predict, test_predict, original_ytrain, original_yval, original_ytest
