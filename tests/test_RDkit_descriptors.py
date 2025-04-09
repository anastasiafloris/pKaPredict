import pytest

from pkapredict.RDkit_descriptors import RDkit_descriptors

def test_RDkit_descriptors_valid_smiles():
    smiles = ["CCO", "C(=O)O"]  # ethanol and formic acid
    descriptors, names = RDkit_descriptors(smiles)

    assert len(descriptors) == 2, "Expected 2 descriptor sets"
    assert len(descriptors[0]) == len(names), "Descriptor length should match descriptor name count"
    assert all(isinstance(x, float) or isinstance(x, int) for x in descriptors[0]), "All descriptors should be numeric"

def test_RDkit_descriptors_with_invalid_smiles():
    smiles = ["CCO", "INVALID_SMILES"]
    descriptors, names = RDkit_descriptors(smiles)

    assert len(descriptors) == 2, "Should return descriptor sets for both entries"
    assert descriptors[1].count(None) == len(names), "Invalid SMILES should return list of None values"
