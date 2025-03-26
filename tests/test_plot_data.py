import sys
import os
import pytest
import numpy as np

# Add the 'src' folder to sys.path so pkapredict can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src", "pkapredict")))

from plot_data import plot_data

def test_plot_data_output(capsys, monkeypatch):
    # Suppress the actual plot display
    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)

    actual = np.array([3.0, 7.0, 10.0])
    predicted = np.array([3.1, 6.9, 10.2])

    plot_data(actual, predicted, "Test Plot")

    captured = capsys.readouterr()
    assert "R² =" in captured.out
    assert "RMSE =" in captured.out
    assert "✅ Plot generated" in captured.out

