import numpy as np
import pytest
import matplotlib
import os
import pandas as pd
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Use non-interactive backend for testing


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










