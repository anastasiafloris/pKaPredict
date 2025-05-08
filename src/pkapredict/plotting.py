"""Module defining the function for plotting predicted vs actual pKa values with regression line and evaluation metrics."""

import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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
    sns.regplot(x=predicted, y=actual, scatter_kws={'color': 'pink'}, line_kws={"lw": 2, "ls": "--", "color": "deeppink", "alpha": 0.7})
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

    # model_selector.py




from lazypredict.Supervised import LazyRegressor

def plot_best_models(X_train, X_valid, y_train, y_valid, random_state=42):
    """
    Runs LazyRegressor on provided datasets and saves a bar plot of the top 10 models by R² score.

    Parameters:
        X_train (pd.DataFrame): Scaled training features
        X_valid (pd.DataFrame): Scaled validation features
        y_train (pd.Series): Training targets
        y_valid (pd.Series): Validation targets
        random_state (int): Random state for LazyRegressor

    Returns:
        models_sorted (pd.DataFrame): Sorted dataframe of model performances
    """
    # Initialize LazyRegressor
    lregs = LazyRegressor(verbose=0, ignore_warnings=True, custom_metric=None, random_state=random_state)

    # Fit models
    models, _ = lregs.fit(X_train, X_valid, y_train, y_valid)

    # Sort models by R-squared
    models_sorted = models.sort_values(by="R-Squared", ascending=False)

    # Plot top 10 models
    plt.figure(figsize=(12, 6))
    plt.barh(models_sorted.index[:10], models_sorted["R-Squared"][:10], align='center', color='pink')
    plt.xlabel("R-Squared Score")
    plt.ylabel("Machine Learning Models")
    plt.title("Top 10 Machine Learning Models for pKa Prediction")
    plt.gca().invert_yaxis()

 
    # ✅ Ensure Plots directory exists
    plot_dir = os.path.join(os.getcwd(), "Plots")
    os.makedirs(plot_dir, exist_ok=True)
    save_path = os.path.join(plot_dir, "Top10MLModels.png")

    plt.savefig(save_path, dpi=300, bbox_inches='tight')

    return models_sorted
    
    

def plot_k_vs_r2_ET(k_values, r2_scores, save_filename="optimalkvalue.png"):
    """
    Plots R² scores versus number of selected features (k) and saves the plot
    in 'pkapredict/notebooks/Plots/'.

    Parameters:
        k_values (list or array-like): List of k values used in SelectKBest
        r2_scores (list or array-like): Corresponding R² scores for each k
        save_filename (str): Filename for the saved plot

    Returns:
        save_path (str): Path to the saved plot image
    """

 

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(k_values, r2_scores, marker='o', linestyle='-', color='lightpink')
    plt.xlabel("Number of Features (k)", color="black")
    plt.ylabel("R² Score", color="black")
    plt.title("Optimal k for SelectKBest Feature Selection", color="black")
    plt.gca().set_facecolor('white')
    plt.tick_params(axis='both', colors='black')

    
# ✅ Ensure Plots directory exists
    plot_dir = os.path.join(os.getcwd(), "Plots")
    os.makedirs(plot_dir, exist_ok=True)
    save_path = os.path.join(plot_dir, "OptimalKValueExtraTrees")

    plt.savefig(save_path, dpi=300, bbox_inches='tight')

    

    return save_path




def LGBMplot_k_vs_r2(k_values, r2_scores, save_filename="OptimalKValueLGBM.png"):
    """
    Plots R² scores versus number of selected features (k) and saves the plot
    in 'notebooks/Plots/'.

    Parameters:
        k_values (list or array-like): List of k values used in SelectKBest
        r2_scores (list or array-like): Corresponding R² scores for each k
        save_filename (str): Filename for the saved plot (should end in .png)

    Returns:
        save_path (str): Path to the saved plot image
    """
    plt.figure(figsize=(10, 6))
    plt.plot(k_values, r2_scores, marker='o', linestyle='-', color='lightpink')
    plt.xlabel("Number of Features (k)", color="black")
    plt.ylabel("R² Score", color="black")
    plt.title("Optimal k for SelectKBest Feature Selection", color="black")
    plt.gca().set_facecolor('white')
    plt.tick_params(axis='both', colors='black')

    # Create save directory
    plot_dir = os.path.join(os.getcwd(), "Plots")
    os.makedirs(plot_dir, exist_ok=True)
    save_path = os.path.join(plot_dir, save_filename)

    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()

    return save_path


