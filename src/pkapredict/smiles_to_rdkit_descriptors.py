"""This module predicts the pKa value of a molecule from its SMILES string by computing RDKit molecular descriptors and feeding them into a pre-trained LightGBM regression model."""

import numpy as np
from rdkit import Chem
from rdkit.ML.Descriptors.MoleculeDescriptors import MolecularDescriptorCalculator

def smiles_to_rdkit_descriptors(smiles, descriptor_names):
    """
    Convert a SMILES string to a vector of RDKit molecular descriptors.
    """
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        calculator = MolecularDescriptorCalculator(descriptor_names)
        descriptors = np.array(calculator.CalcDescriptors(mol))
        return descriptors
    else:
        raise ValueError(f"❌ Invalid SMILES string: {smiles}")