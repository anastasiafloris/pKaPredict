from pathlib import Path
import os
import pandas as pd

def preview_data(
    relative_path: str = os.path.join("..", "data", "pkadatasetRAWDATA.csv"),
    preview_chars: int = 100,
    preview_rows: int = 10
) -> pd.DataFrame | None:
    """
    Loads and previews the raw pKa dataset from a relative file path.

    Parameters:
        relative_path (str): Path to the dataset file relative to the notebook.
        preview_chars (int): Number of characters to preview from the raw file.
        preview_rows (int): Number of rows to preview from the DataFrame.

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
