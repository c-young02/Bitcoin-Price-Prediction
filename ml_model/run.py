from tensorflow.keras.models import load_model
from predict import predict_price, predict_price_plot
import os
from fetch_bitcoin_data import fetch_data


def predict_bitcoin_price(model_paths):
    try:
        # Get the directory where the current script is located
        model_dir = os.path.dirname(os.path.realpath(__file__))

        # Initialize an empty list to store the predicted prices
        predicted_prices = []

        # Fetch the Bitcoin data
        bitcoin_data = fetch_data()

        # Loop over the array of model paths
        for path in model_paths:
            # Construct the absolute path to the saved model
            file_path = os.path.join(model_dir, path)

            # Load the pre-trained model from the file
            model = load_model(file_path)

            # Use the loaded model to predict the price 14 days into the future using the fetched Bitcoin data
            predicted_price = predict_price(model, bitcoin_data)

            # Append the predicted price to the list
            predicted_prices.append(predicted_price)

        # Return the list of predicted prices
        return predicted_prices
    except Exception as e:
        print(f"Error in predict_bitcoin_price: {e}")
        return None