"""Module to compute RDKit molecular descriptors from SMILES strings and output results as a CSV file."""


import pandas as pd
import os
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.ML.Descriptors import MoleculeDescriptors
from tqdm import tqdm

def RDkit_descriptors(smiles: list) -> tuple:
    """
    Compute RDKit molecular descriptors for a list of SMILES strings.

    Parameters
    ----------
    smiles : list
        List of SMILES strings.

    Returns
    -------
    tuple
        (List of computed descriptor values, List of descriptor names)
    
    Examples
    --------
    >>> RDkit_descriptors(["CCO", "C(=O)O"])
    """
    mols = [Chem.MolFromSmiles(i) for i in smiles]
    calc = MoleculeDescriptors.MolecularDescriptorCalculator([x[0] for x in Descriptors._descList])
    desc_names = calc.GetDescriptorNames()

    Mol_descriptors = []
    for mol in tqdm(mols, desc="Computing Molecular Descriptors"):
        if mol is not None:
            mol = Chem.AddHs(mol)  # Add hydrogens for better accuracy
            descriptors = calc.CalcDescriptors(mol)
            Mol_descriptors.append(descriptors)
        else:
            Mol_descriptors.append([None] * len(desc_names))  # Handle invalid SMILES

    return Mol_descriptors, desc_names

def example_descriptors_output() -> None:
    """
    Compute molecular descriptors for a few example SMILES and output as a CSV file.
    """
    example_smiles = ["CCO", "C(=O)O"]
    print("🔹 Computing molecular descriptors for example molecules...")
    Mol_descriptors, desc_names = RDkit_descriptors(example_smiles)
    
    # Create DataFrame with descriptors and add SMILES column
    df_descriptors = pd.DataFrame(Mol_descriptors, columns=desc_names)
    df_descriptors.insert(0, "Smiles", example_smiles)  # Insert Smiles as the first column
    
    # Output CSV data
    print("✅ Descriptor computation completed. Outputting CSV data:")
    print(df_descriptors.to_csv(index=False))

if __name__ == "__main__":
    example_descriptors_output()