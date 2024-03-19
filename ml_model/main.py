from load_data import load_data
from preprocessing import preprocessing, transform
from model import create_model, train_model
from evaluation import evaluate_model
from plots import plot_loss, plot_close, plot_predictions


def main():
    # Define the dataset file path
    dataset = "data/BTC-USD.csv"

    # Define the number of epochs for training the model
    epochs = 200

    # Define the number of past days' data to consider for the prediction
    time_step = 60

    # Define the number of future days to predict
    future_step = 7

    # Load the data from the CSV file
    df = load_data(dataset)

    # Plot the 'Close' column against the 'Date' column
    plot_close(df)

    # Preprocess the data
    df, close_stock, x_train, y_train, x_val, y_val, x_test, y_test = preprocessing(
        df, time_step, future_step
    )

    # Create the model
    model = create_model()

    # Train the model
    history = train_model(
        model, x_train, y_train, x_val, y_val, future_step, epochs=epochs, batch_size=32
    )

    # Plot the training and validation loss
    plot_loss(history)

    # Predict the training, validation and testing data
    train_predict = model.predict(x_train)
    val_predict = model.predict(x_val)
    test_predict = model.predict(x_test)

    # Transform the predicted data back to its original form
    train_predict, val_predict, test_predict, original_ytrain, original_yval, original_ytest = transform(
        train_predict, val_predict, test_predict, y_train, y_val, y_test
    )

    # Evaluate the model
    evaluate_model(train_predict, original_ytrain, val_predict, original_yval, test_predict, original_ytest)

    # Plot the predictions
    plot_predictions(df, train_predict, val_predict, test_predict, close_stock, time_step)


if __name__ == "__main__":
    main()
