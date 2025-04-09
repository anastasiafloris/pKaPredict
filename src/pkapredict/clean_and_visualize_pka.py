"""This module cleans and visualizes pKa datasets and computes RDKit molecular descriptors for SMILES strings, with optional CSV output for example molecules."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


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
        The function prints dataset statistics and checks for missing and NaN values as well as selects the relevant columns to the package
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

   
    





