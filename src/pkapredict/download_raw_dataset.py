from pathlib import Path
import requests

def download_raw_dataset(
    url: str = "https://raw.githubusercontent.com/anastasiafloris/pKaPredict/main/data/pkadatasetRAWDATA.csv",
    filename: str = "pkadatasetRAWDATA.csv",
    levels_up: int = 1,
    data_folder: str = "data"
) -> Path:
    """
    Downloads a CSV file from a given URL and saves it in the specified data directory.
    
    Parameters:
        url (str): URL of the raw CSV file.
        filename (str): Name to save the file as.
        levels_up (int): Number of directory levels to go up from the current working directory.
        data_folder (str): Subfolder name under the repo root to save the file.

    Returns:
        Path: Path to the downloaded file.
    """
    # Get repository root by going up `levels_up` directories
    repo_root = Path.cwd()
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
