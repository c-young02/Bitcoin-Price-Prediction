import os
from keras.models import load_model
from load_data import load_data
from preprocessing import preprocessing, transform
from evaluation import evaluate_model
from plots import plot_predictions


def evaluate():
    try:
        # Define the number of days to predict in the future
        future = 7

        # Define the dataset file path
        dataset = "data/BTC-USD.csv"

        # Define the number of past days' data to consider for the prediction
        time_step = 60

        # Define the number of future days to predict
        future_step = future

        # Load the data from the CSV file
        df = load_data(dataset)

        # Preprocess the data
        df, close_stock, x_train, y_train, x_val, y_val, x_test, y_test = preprocessing(
            df, time_step, future_step
        )

        # Load the pre-trained model
        model_path = os.path.join(
            os.path.dirname(os.getcwd()), f"models/model_{future}.h5"
        )
        model = load_model(model_path)

        # Predict the training, validation and testing data
        train_predict = model.predict(x_train)
        val_predict = model.predict(x_val)
        test_predict = model.predict(x_test)

        # Transform the predicted data back to its original form
        (
            train_predict,
            val_predict,
            test_predict,
            original_ytrain,
            original_yval,
            original_ytest,
        ) = transform(train_predict, val_predict, test_predict, y_train, y_val, y_test)

        # Evaluate the model
        evaluate_model(
            train_predict,
            original_ytrain,
            val_predict,
            original_yval,
            test_predict,
            original_ytest,
        )

        # Plot the predictions
        plot_predictions(
            df, train_predict, val_predict, test_predict, close_stock, time_step
        )

    except Exception as e:
        print(f"An error occurred during evaluation: {e}")


if __name__ == "__main__":
    evaluate()
