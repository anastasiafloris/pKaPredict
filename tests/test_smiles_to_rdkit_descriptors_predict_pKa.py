import sys
import os
import pytest
import numpy as np
from unittest.mock import MagicMock

# Add the 'src' folder to sys.path so pkapredict can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src", "pkapredict")))

from smiles_to_rdkit_descriptors_predict_pKa import smiles_to_rdkit_descriptors, predict_pKa, load_model

@pytest.fixture
def descriptor_names():
    # Minimal list of descriptors for quick testing
    return ["MolMR", "MolLogP", "NumHAcceptors", "NumHDonors"]

def test_smiles_to_rdkit_descriptors_valid(descriptor_names):
    descriptors = smiles_to_rdkit_descriptors("CCO", descriptor_names)
    assert isinstance(descriptors, np.ndarray)
    assert descriptors.shape == (len(descriptor_names),)
    assert all(isinstance(x, (float, np.floating)) for x in descriptors)

def test_smiles_to_rdkit_descriptors_invalid(descriptor_names):
    with pytest.raises(ValueError, match="❌ Invalid SMILES string"):
        smiles_to_rdkit_descriptors("INVALID", descriptor_names)

def test_predict_pKa(monkeypatch, descriptor_names):
    mock_model = MagicMock()
    mock_model.predict.return_value = [5.55]

    predicted = predict_pKa("CCO", mock_model, descriptor_names)
    assert isinstance(predicted, float)
    assert predicted == 5.55

def test_load_model_file_not_found(monkeypatch):
    # Simulate the model path check returning False
    monkeypatch.setattr("os.path.exists", lambda _: False)

    with pytest.raises(FileNotFoundError, match="❌ Model file not found"):
        load_model()

