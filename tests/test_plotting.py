import numpy as np
import pytest
import matplotlib
import os
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Use non-interactive backend for testing
matplotlib.use("Agg")

from pkapredict.plotting import plot_data, plot_best_models, plot_k_vs_r2_ET

def test_plot_data(capsys):
    actual = np.array([3.2, 7.4, 10.5])
    predicted = np.array([3.1, 7.3, 10.7])

    try:
        plot_data(actual, predicted, "Test pKa Plot")
    except Exception as e:
        pytest.fail(f"plot_data raised an exception: {e}")

    captured = capsys.readouterr()
    assert "R² = " in captured.out
    assert "RMSE = " in captured.out
    assert "✅ Plot generated with R²" in captured.out

matplotlib.use("Agg")

def test_plot_best_models():
    # Generate synthetic regression dataset
    X, y = make_regression(n_samples=100, n_features=5, noise=0.1, random_state=42)
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_valid_scaled = scaler.transform(X_valid)

    # Convert to DataFrame/Series
    X_train_df = pd.DataFrame(X_train_scaled)
    X_valid_df = pd.DataFrame(X_valid_scaled)
    y_train_series = pd.Series(y_train)
    y_valid_series = pd.Series(y_valid)

    # Run the function and test
    models_sorted = plot_best_models(X_train_df, X_valid_df, y_train_series, y_valid_series)

    assert isinstance(models_sorted, pd.DataFrame), "Expected output to be a DataFrame"
    assert not models_sorted.empty, "Expected non-empty DataFrame"
    assert "R-Squared" in models_sorted.columns, "Expected 'R-Squared' column in output"


matplotlib.use("Agg")

def test_plot_k_vs_r2_ET_runs_without_error(): # plot_k_vs_r2_ET is the same function as LGBMplot_k_vs_r2 so will be only tested once.
    k_values = [1, 2, 3, 4, 5]
    r2_scores = [0.1, 0.3, 0.5, 0.45, 0.48]

    try:
        path = plot_k_vs_r2_ET(k_values, r2_scores, save_filename="test_k_vs_r2_ET.png")
    except Exception as e:
        pytest.fail(f"plot_k_vs_r2_ET raised an exception: {e}")

    assert isinstance(path, str) or isinstance(path, os.PathLike), "Expected a file path as return value"

