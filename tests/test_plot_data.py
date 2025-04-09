import pytest
import numpy as np
from pkapredict.plot_data import plot_data

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

