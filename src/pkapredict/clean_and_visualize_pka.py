"""This module cleans and visualizes pKa datasets and computes RDKit molecular descriptors for SMILES strings, with optional CSV output for example molecules."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import os

def clean_and_visualize_pka(data_pka: pd.DataFrame) -> None:
    """
    Cleans the dataset by removing NaN values, duplicates, and visualizes pKa distribution.

    Parameters
    ----------
    data_pka : pd.DataFrame
        A DataFrame containing 'Smiles', 'pka', and 'acid_base_type' columns.

    Returns
    -------
    None
        The function prints dataset statistics and displays a histogram of pKa values.
    """
    if data_pka is None or data_pka.empty:
        print("❌ Error: Dataset is empty or not loaded.")
        return

    # Check initial shape
    print("\n🔹 Checking dataset information:")
    print(f"Initial dataset shape: {data_pka.shape}")

    # Ensure necessary columns exist
    required_columns = {"Smiles", "pka", "acid_base_type"}
    missing_columns = required_columns - set(data_pka.columns)
    if missing_columns:
        print(f"❌ Error: Missing required columns: {missing_columns}")
        return
    
    # Select only relevant columns and create a copy
    data_pka = data_pka[list(required_columns)].copy()
    
    # Check for missing values
    missing_values = data_pka.isnull().sum()
    print(f"\nMissing values before cleaning:\n{missing_values}")
    
    # Drop NaN values
    data_pka.dropna(subset=["pka"], inplace=True)
    
    # Remove duplicates
    initial_rows = data_pka.shape[0]
    data_pka.drop_duplicates(inplace=True)
    final_rows = data_pka.shape[0]
    duplicates_removed = initial_rows - final_rows
    print(f"\nTotal duplicate rows removed: {duplicates_removed}")
    
    # Check final shape after cleaning
    print(f"Dataset shape after NaN and duplicate removal: {data_pka.shape}")
    
    # Plot distribution of pKa values
    plt.figure(figsize=(8, 5))
    plt.hist(data_pka["pka"], bins=30, edgecolor='black', alpha=0.7, color='pink')
    plt.xlabel("pKa")
    plt.ylabel("Frequency")
    plt.title("Distribution of pKa Values")
    plt.grid(False)  # Remove the grid
    plt.show()

if __name__ == "__main__":
    # Example dataset
    example_data = pd.DataFrame({
        'Smiles': ['CCO', 'CCO', 'C(=O)O', 'CCN', 'CCN'],
        'pka': [16, 16, 4.8, 10.5, 10.5],
        'acid_base_type': ['acid', 'acid', 'acid', 'base', 'base']
    })
    clean_and_visualize_pka(example_data)

# -----------------------------------------------------------------------------------


