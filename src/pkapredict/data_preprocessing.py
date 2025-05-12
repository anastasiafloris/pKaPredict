"""
Module: data_preprocessing.py

This module provides utility functions for handling the raw pKa prediction dataset.
It includes functionality to:

1. Download the dataset CSV file from a specified URL and save it to a local directory.
2. Preview the contents of the dataset.
3. Clean the dataset by removing rows with missing pKa values and duplicates, then save
   the cleaned data to a new CSV file.
4. Visualize the distribution of pKa values.

Intended for use in preprocessing workflows for machine learning tasks related to 
pKa prediction.
"""
from __future__ import annotations
import pathlib
from pathlib import Path
import requests
import pandas as pd
import matplotlib.pyplot as plt
import os

def download_raw_dataset(
    url: str = "https://raw.githubusercontent.com/anastasiafloris/pKaPredict/main/data/pkadatasetRAWDATA.csv",
    filename: str = "pkadatasetRAWDATA.csv",
    levels_up: int = 1,
    data_folder: str = "data"
) -> "Path":  # ✅ FIXED: return type is now a forward reference
    """
    Downloads a CSV file from a given URL and saves it in the specified data directory.

    Returns:
        Path: Path to the downloaded file.
    """
    # Get repository root by going up `levels_up` directories
    repo_root = pathlib.Path.cwd()
    for _ in range(levels_up):
        repo_root = repo_root.parent

    save_dir = repo_root / data_folder
    save_dir.mkdir(parents=True, exist_ok=True)
    file_path = save_dir / filename

    try:
        response = requests.get(url)
        response.raise_for_status()

        if "<!DOCTYPE html>" in response.text:
            print("❌ Error: This is an HTML page, not the CSV file. Check your URL.")
        else:
            with open(file_path, "wb") as file:
                file.write(response.content)
            print(f"✅ File downloaded successfully: {file_path}")
            return file_path

    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to download file: {e}")
        return None

def preview_data(
    relative_path: str = os.path.join("..", "data", "pkadatasetRAWDATA.csv"),
    preview_chars: int = 100,
    preview_rows: int = 10
) -> pd.DataFrame | None:
    """
    Loads and previews the raw pKa dataset from a relative file path.

    Returns:
        pd.DataFrame | None: The loaded dataset if successful, otherwise None.
    """
    current_directory = Path.cwd()
    print("📂 Current Directory:", current_directory.resolve())

    file_path_obj = Path(relative_path)

    if file_path_obj.exists():
        print("✅ Dataset file found. Previewing contents...\n")

        try:
            with file_path_obj.open("r", encoding="utf-8") as file:
                content = file.read()
                print(content[:preview_chars])

            data_pka = pd.read_csv(file_path_obj, delimiter=",")
            print("\n✅ Dataset successfully loaded. Preview:")

            from IPython.display import display
            display(data_pka.head(preview_rows))

            return data_pka

        except Exception as e:
            print(f"❌ Error loading dataset: {e}")
            return None
    else:
        print(f"❌ Error: The file '{file_path_obj}' does not exist.")
        return None

def clean_and_visualize_pka(
    data_pka: pd.DataFrame,
    save_path: str = "../data/pkadataset_cleaned.csv"
) -> pd.DataFrame | None:
    """
    Cleans the dataset by removing NaN values, duplicates, and visualizes pKa distribution.
    Saves the cleaned DataFrame to a CSV file.

    Returns:
        pd.DataFrame | None: The cleaned DataFrame if successful, otherwise None.
    """
    if data_pka is None or data_pka.empty:
        print("❌ Error: Dataset is empty or not loaded.")
        return None

    print("\n🔹 Checking dataset information:")
    print(f"Initial dataset shape: {data_pka.shape}")

    required_columns = {"Smiles", "pka", "acid_base_type"}
    missing_columns = required_columns - set(data_pka.columns)
    if missing_columns:
        print(f"❌ Error: Missing required columns: {missing_columns}")
        return None

    # Select only required columns
    data_pka = data_pka[list(required_columns)].copy()

    # Display missing values
    missing_values = data_pka.isnull().sum()
    print(f"\nMissing values before cleaning:\n{missing_values}")

    # Drop rows where pKa is missing
    data_pka.dropna(subset=["pka"], inplace=True)

    # Remove duplicates
    initial_rows = data_pka.shape[0]
    data_pka.drop_duplicates(inplace=True)
    final_rows = data_pka.shape[0]
    duplicates_removed = initial_rows - final_rows
    print(f"\nTotal duplicate rows removed: {duplicates_removed}")
    print(f"Dataset shape after NaN and duplicate removal: {data_pka.shape}")

    if data_pka.empty:
        print("⚠️ Warning: All rows were removed during cleaning. Skipping CSV save.")
        return None

    save_path_obj = Path(save_path)
    save_path_obj.parent.mkdir(parents=True, exist_ok=True)

    try:
        data_pka.to_csv(save_path_obj, index=False)
        print(f"💾 Cleaned dataset saved to: {save_path_obj.resolve()} (shape: {data_pka.shape})")
    except Exception as e:
        print(f"❌ Failed to save cleaned dataset: {e}")
        return None

    return data_pka
