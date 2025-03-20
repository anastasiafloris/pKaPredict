"""Module for plotting predicted vs actual pKa values with regression line and evaluation metrics."""

import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import matplotlib.patches as mpatches
from sklearn.metrics import mean_squared_error, r2_score

def plot_data(actual, predicted, title):
    """
    Plots predicted vs actual pKa values with regression line and evaluation metrics.

    Parameters
    ----------
    actual : list or np.array
        The actual (experimental) pKa values.
    predicted : list or np.array
        The predicted pKa values.
    title : str
        The title for the plot.
    
    Returns
    -------
    None
        Displays the plot and prints RMSE and R² values.

    Examples
    --------
    >>> import numpy as np
    >>> actual = np.array([3.2, 7.4, 10.5])
    >>> predicted = np.array([3.1, 7.3, 10.7])
    >>> plot_data(actual, predicted, "Example Plot")
    """
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    R2 = r2_score(actual, predicted)

    plt.figure(figsize=(8, 6))
    sn.regplot(x=predicted, y=actual, scatter_kws={'color': 'pink'}, line_kws={"lw": 2, "ls": "--", "color": "deeppink", "alpha": 0.7})
    plt.title(title, color="black")
    plt.xlabel("Predicted pKa", color="black")
    plt.ylabel("Experimental pKa", color="black")
    plt.gca().set_facecolor('white')  # Set background to white

    # Add R² and RMSE patches to legend
    R2_patch = mpatches.Patch(color='pink', label=f"R² = {R2:.2f}")
    rmse_patch = mpatches.Patch(color='pink', label=f"RMSE = {rmse:.2f}")
    plt.legend(handles=[R2_patch, rmse_patch])
    plt.show()
    
    print(f"✅ Plot generated with R² = {R2:.2f} and RMSE = {rmse:.2f}")

def example_plot():
    """
    Generate an example plot with dummy predicted and actual pKa values.
    """
    actual = np.array([3.2, 7.4, 10.5, 5.6, 9.8])
    predicted = np.array([3.1, 7.3, 10.7, 5.4, 9.9])
    plot_data(actual, predicted, "Example Validation Data")

if __name__ == "__main__":
    example_plot()
