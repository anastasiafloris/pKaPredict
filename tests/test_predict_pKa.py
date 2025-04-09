import pytest
import numpy as np
from unittest.mock import MagicMock
from pkapredict.predict_pKa import predict_pKa

# Fixture for a minimal descriptor list
@pytest.fixture
def descriptor_names():
    return ["desc1", "desc2", "desc3"]

# The actual test function
def test_predict_pKa(monkeypatch, descriptor_names):
    # Mock the model
    mock_model = MagicMock()
    mock_model.predict.return_value = [5.55]

    # Mock the descriptor generator
    def mock_smiles_to_rdkit_descriptors(smiles, desc_names):
        return np.array([1.0, 2.0, 3.0])
    
    monkeypatch.setattr(
        "pkapredict.predict_pKa.smiles_to_rdkit_descriptors",
        mock_smiles_to_rdkit_descriptors
    )

    predicted = predict_pKa("CCO", mock_model, descriptor_names)

    assert isinstance(predicted, float)
    assert predicted == 5.55
