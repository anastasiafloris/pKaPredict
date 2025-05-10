import pytest
from pkapredict.plotting import plot_k_vs_r2_ET

def test_plot_k_vs_r2_ET_runs_and_shows_plot():
    # Simplified test data
    k_values = [1, 2, 3]
    r2_scores = [0.1, 0.3, 0.5]

    try:
        # Just call the function — it will show the plot as coded
        result = plot_k_vs_r2_ET(k_values, r2_scores, save_filename=None)

        # If no file is saved, the result is likely None or ignored
        # You can skip this assert if your function returns nothing
    except Exception as e:
        pytest.fail(f"plot_k_vs_r2_ET raised an exception: {e}")


