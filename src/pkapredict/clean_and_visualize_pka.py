from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def clean_and_visualize_pka(
    data_pka: pd.DataFrame,
    save_path: str = "../data/pkadataset_cleaned.csv"
) -> pd.DataFrame | None:
    """
    Cleans the dataset by removing NaN values, duplicates, and visualizes pKa distribution.
    Saves the cleaned DataFrame to a CSV file.

    Parameters
    ----------
    data_pka : pd.DataFrame
        A DataFrame containing 'Smiles', 'pka', and 'acid_base_type' columns.
    save_path : str
        Path where the cleaned DataFrame should be saved.

    Returns
    -------
    pd.DataFrame or None
        The cleaned DataFrame if successful; otherwise, None.
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

    # Warn if the dataset is now empty
    if data_pka.empty:
        print("⚠️ Warning: All rows were removed during cleaning. Skipping CSV save.")
        return None

    # Save to CSV
    save_path_obj = Path(save_path)
    save_path_obj.parent.mkdir(parents=True, exist_ok=True)

    try:
        data_pka.to_csv(save_path_obj, index=False)
        print(f"💾 Cleaned dataset saved to: {save_path_obj.resolve()} (shape: {data_pka.shape})")
    except Exception as e:
        print(f"❌ Failed to save cleaned dataset: {e}")
        return None

    return data_pka




   
    





