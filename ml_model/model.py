from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras import backend as K


def root_mean_squared_error(y_true, y_pred):
    """
    Custom metric for root mean squared error (RMSE)
    """
    return K.sqrt(K.mean(K.square(y_pred - y_true)))


def create_model(units=10, activation="relu"):
    """
    Function to create a Sequential model with LSTM and Dense layers.

    Args:
        units (int): The number of units in the LSTM layer.
        activation (str): The activation function to use in the LSTM layer.

    Returns:
        model: Compiled Sequential model
    """
    model = Sequential()
    model.add(LSTM(units, input_shape=(None, 1), activation=activation))
    model.add(Dense(1))
    model.compile(loss="mean_squared_error", optimizer="adam", metrics=[root_mean_squared_error])
    return model


def train_model(model, x_train, y_train, x_test, y_test, epochs=200, batch_size=32):
    """
    Function to train the model with the given training and test data.

    Args:
        model: Compiled Sequential model
        x_train: Training data features
        y_train: Training data labels
        x_test: Test data features
        y_test: Test data labels
        epochs (int): Number of epochs to train for
        batch_size (int): Batch size for training

    Returns:
        history: History object containing training history
    """
    early_stopping = EarlyStopping(monitor='val_root_mean_squared_error', patience=10)
    model_checkpoint = ModelCheckpoint('../models/model.h5', monitor='val_root_mean_squared_error', save_best_only=True)

    history = model.fit(
        x_train,
        y_train,
        validation_data=(x_test, y_test),
        epochs=epochs,
        batch_size=batch_size,
        verbose=1,
        callbacks=[early_stopping, model_checkpoint]
    )
    return history
