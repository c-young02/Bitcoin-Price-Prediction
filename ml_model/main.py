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
    time_step = 30

    # Define the number of future days to predict
    future_step = 14

    # Load the data from the CSV file
    df = load_data(dataset)

    # Plot the 'Close' column against the 'Date' column
    plot_close(df)

    # Preprocess the data
    df, close_stock, x_train, y_train, x_test, y_test = preprocessing(
        df, time_step, future_step
    )

    # Create the model
    model = create_model()

    # Train the model
    history = train_model(
        model, x_train, y_train, x_test, y_test, epochs=epochs, batch_size=32
    )

    # Plot the training and validation loss
    plot_loss(history)

    # Predict the training and testing data
    train_predict = model.predict(x_train)
    test_predict = model.predict(x_test)

    # Transform the predicted data back to its original form
    train_predict, test_predict, original_ytrain, original_ytest = transform(
        train_predict, test_predict, y_train, y_test
    )

    # Evaluate the model
    evaluate_model(train_predict, original_ytrain, test_predict, original_ytest)

    # Plot the predictions
    plot_predictions(df, train_predict, test_predict, close_stock, time_step)


if __name__ == "__main__":
    main()
