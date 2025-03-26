
import sys
import os
import pandas as pd
import pytest

# Add the 'src' folder to sys.path so pkapredict can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..","src","pkapredict")))

from clean_and_visualize_pka import clean_and_visualize_pka
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


