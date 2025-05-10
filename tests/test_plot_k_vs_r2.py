import pytest
from unittest import mock
from pkapredict.plotting import plot_k_vs_r2_ET

def test_plot_k_vs_r2_ET_runs_without_saving_or_blocking():
    k_values = [1, 2, 3]
    r2_scores = [0.1, 0.3, 0.5]

    try:
        # Patch plt.show() so it doesn't block
        with mock.patch("matplotlib.pyplot.show"):
            plot_k_vs_r2_ET(k_values, r2_scores, save_filename=None)
    except Exception as e:
        pytest.fail(f"plot_k_vs_r2_ET raised an exception: {e}")



