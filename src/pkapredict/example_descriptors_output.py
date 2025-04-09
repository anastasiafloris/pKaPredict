"""Example module to compute RDKit molecular descriptors from example SMILES strings and output results as a CSV data."""
from pkapredict.RDkit_descriptors import RDkit_descriptors
import pandas as pd

def example_descriptors_output() -> None:
    """
    Compute molecular descriptors for a few example SMILES and output as a CSV data.
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