from tensorflow.keras.models import load_model
from ml_model.model import root_mean_squared_error
from predict import predict_price, predict_price_plot
import os
from fetch_bitcoin_data import fetch_data

# Get the directory where the current script is located
model_dir = os.path.dirname(os.path.realpath(__file__))
# Define the relative path to the saved model
path = "../models/model.h5"

# Construct the absolute path to the saved model
file_path = os.path.join(model_dir, path)

# Load the pre-trained model from the file
model = load_model(file_path, custom_objects={'root_mean_squared_error': root_mean_squared_error})

# Fetch the Bitcoin data
bitcoin_data = fetch_data()

# Use the loaded model to predict the price 14 days into the future using the fetched Bitcoin data
predicted_price = predict_price(model, bitcoin_data)

# Print the predicted price
print("The predicted price 14 days into the future is: ", predicted_price)

predict_price_plot(predicted_price, bitcoin_data)