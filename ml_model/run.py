from tensorflow.keras.models import load_model
from predict import predict_price, predict_price_plot
import os
from data import last_30_days

# Get the directory where the current script is located
model_dir = os.path.dirname(os.path.realpath(__file__))
# Define the relative path to the saved model
path = "../models/model.h5"

# Construct the absolute path to the saved model
file_path = os.path.join(model_dir, path)

# Load the pre-trained model from the file
model = load_model(file_path)

# Use the loaded model to predict the price 14 days into the future
predicted_price = predict_price(model, last_30_days)

# Print the predicted price
print("The predicted price 14 days into the future is: ", predicted_price)

predict_price_plot(predicted_price, last_30_days)
