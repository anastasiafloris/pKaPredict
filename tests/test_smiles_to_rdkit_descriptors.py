import pytest
import numpy as np
from unittest.mock import MagicMock


from pkapredict.smiles_to_rdkit_descriptors import smiles_to_rdkit_descriptors
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




