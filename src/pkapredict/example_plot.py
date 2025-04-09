from pkapredict.plot_data import plot_data
import numpy as np

def example_plot():
    """
    Generate an example plot with dummy predicted and actual pKa values.
    """
    actual = np.array([3.2, 7.4, 10.5, 5.6, 9.8])
    predicted = np.array([3.1, 7.3, 10.7, 5.4, 9.9])
    plot_data(actual, predicted, "Example Validation Data")

if __name__ == "__main__":
    example_plot()
    