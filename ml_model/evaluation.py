import math
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    explained_variance_score,
    r2_score,
    mean_gamma_deviance,
    mean_poisson_deviance,
)


def calculate_and_print_metrics(y_true, y_pred, data_type):
    """
    Helper function to calculate and print the metrics.

    Args:
        y_true: The actual values.
        y_pred: The predicted values.
        data_type: The type of data (train or test).
    """
    metrics = {
        "RMSE": math.sqrt(mean_squared_error(y_true, y_pred)),
        "MSE": mean_squared_error(y_true, y_pred),
        "MAE": mean_absolute_error(y_true, y_pred),
        "Explained Variance Regression Score": explained_variance_score(y_true, y_pred),
        "R2 Score": r2_score(y_true, y_pred),
        "Mean Gamma Deviance": mean_gamma_deviance(y_true, y_pred),
        "Mean Poisson Deviance": mean_poisson_deviance(y_true, y_pred),
    }

    for metric_name, metric_value in metrics.items():
        print(f"{data_type} data {metric_name}: {metric_value}")


def evaluate_model(train_predict, original_ytrain, test_predict, original_ytest):
    """
    Function to evaluate the performance of the model using various metrics.
    :param train_predict: Predicted values for the training data
    :param original_ytrain: Original values for the training data
    :param test_predict: Predicted values for the test data
    :param original_ytest: Original values for the test data
    """
    calculate_and_print_metrics(original_ytrain, train_predict, "Train")
    calculate_and_print_metrics(original_ytest, test_predict, "Test")
