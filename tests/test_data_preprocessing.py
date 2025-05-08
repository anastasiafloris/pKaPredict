import pandas as pd
import pytest
from pkapredict.data_preprocessing import download_raw_dataset, preview_data, clean_and_visualize_pka
from unittest.mock import patch, Mock
import pathlib
from pathlib import Path

def test_download_raw_dataset(tmp_path):
    dummy_csv = "col1,col2\nval1,val2\n"
    dummy_url = "https://fake-url.com/dummy.csv"
    dummy_filename = "test.csv"

    # Mock the response from requests.get
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = dummy_csv
    mock_response.content = dummy_csv.encode("utf-8")

    with patch("pkapredict.data_preprocessing.requests.get", return_value=mock_response):
        downloaded_path = download_raw_dataset(
            url=dummy_url,
            filename=dummy_filename,
            levels_up=0,  # stay in tmp_path
            data_folder=tmp_path.name
        )

    # Ensure the file was saved correctly
    expected_path = tmp_path / dummy_filename
    assert isinstance(downloaded_path, pathlib.Path)
    assert downloaded_path.name == dummy_filename
    assert downloaded_path.exists()
    assert downloaded_path.read_text() == dummy_csv


def test_preview_data(tmp_path):
    # Create a dummy CSV file
    dummy_data = "col1,col2\n1,a\n2,b\n3,c\n"
    dummy_file = tmp_path / "pkadatasetRAWDATA.csv"
    dummy_file.write_text(dummy_data, encoding="utf-8")

    # Use the actual path as a string (relative path simulation)
    relative_path = str(dummy_file)

    # Run the function
    result = preview_data(relative_path=relative_path, preview_chars=50, preview_rows=2)

    # Check if a DataFrame is returned
    assert isinstance(result, pd.DataFrame), "Expected a pandas DataFrame"
    assert result.shape == (3, 2), "Expected DataFrame shape (3, 2)"
    assert list(result.columns) == ["col1", "col2"], "Unexpected DataFrame columns"

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'Smiles': ['CCO', 'CCO', 'C(=O)O', 'CCN', 'CCN'],
        'pka': [16, 16, 4.8, 10.5, 10.5],
        'acid_base_type': ['acid', 'acid', 'acid', 'base', 'base']
    })

def test_clean_and_visualize_pka_valid_data(sample_data, capsys, monkeypatch):
    # Suppress the actual plot display
    monkeypatch.setattr("matplotlib.pyplot.show", lambda: None)

    clean_and_visualize_pka(sample_data)
    captured = capsys.readouterr()

    assert "Initial dataset shape" in captured.out
    assert "Missing values before cleaning" in captured.out
    assert "Total duplicate rows removed" in captured.out
    assert "Dataset shape after NaN and duplicate removal" in captured.out

def test_empty_dataframe(capsys):
    empty_df = pd.DataFrame()
    clean_and_visualize_pka(empty_df)
    captured = capsys.readouterr()
    assert "❌ Error: Dataset is empty or not loaded." in captured.out

def test_missing_required_columns(capsys):
    df_missing = pd.DataFrame({
        'Smiles': ['CCO'],
        'pka': [16]
        # Missing 'acid_base_type'
    })
    clean_and_visualize_pka(df_missing)
    captured = capsys.readouterr()
    assert "❌ Error: Missing required columns" in captured.out