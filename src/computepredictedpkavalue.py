"""Module to compute RDKit molecular descriptors from SMILES and predict pKa using a trained LGBMRegressor model."""

import numpy as np
import pickle
import pandas as pd
import os
from rdkit import Chem
from rdkit.ML.Descriptors.MoleculeDescriptors import MolecularDescriptorCalculator

# Exact descriptor list used during training
descriptor_names = [
    'MaxAbsEStateIndex', 'MaxEStateIndex', 'MinAbsEStateIndex', 'MinEStateIndex', 'SPS',
    'NumValenceElectrons', 'MaxPartialCharge', 'MinPartialCharge', 'MaxAbsPartialCharge', 'MinAbsPartialCharge',
    'FpDensityMorgan1', 'FpDensityMorgan2', 'FpDensityMorgan3', 'BCUT2D_MWHI', 'BCUT2D_MWLOW',
    'BCUT2D_CHGLO', 'BCUT2D_LOGPLOW', 'BCUT2D_MRHI', 'BalabanJ', 'BertzCT', 'Chi0', 'Chi0n', 'Chi1',
    'Chi1n', 'Chi3v', 'Chi4v', 'HallKierAlpha', 'Kappa1', 'Kappa2', 'Kappa3', 'LabuteASA', 'PEOE_VSA1',
    'PEOE_VSA12', 'PEOE_VSA13', 'PEOE_VSA14', 'PEOE_VSA3', 'PEOE_VSA4', 'PEOE_VSA5', 'PEOE_VSA6',
    'PEOE_VSA7', 'PEOE_VSA8', 'PEOE_VSA9', 'SMR_VSA1', 'SMR_VSA10', 'SMR_VSA2', 'SMR_VSA3', 'SMR_VSA4',
    'SMR_VSA5', 'SMR_VSA6', 'SMR_VSA7', 'SMR_VSA9', 'SlogP_VSA1', 'SlogP_VSA10', 'SlogP_VSA11',
    'SlogP_VSA12', 'SlogP_VSA2', 'SlogP_VSA3', 'SlogP_VSA4', 'SlogP_VSA5', 'SlogP_VSA6', 'SlogP_VSA7',
    'SlogP_VSA8', 'TPSA', 'EState_VSA1', 'EState_VSA10', 'EState_VSA2', 'EState_VSA3', 'EState_VSA4',
    'EState_VSA5', 'EState_VSA6', 'EState_VSA7', 'EState_VSA8', 'EState_VSA9', 'VSA_EState1',
    'VSA_EState10', 'VSA_EState2', 'VSA_EState3', 'VSA_EState4', 'VSA_EState6', 'VSA_EState7',
    'VSA_EState8', 'VSA_EState9', 'FractionCSP3', 'NHOHCount', 'NOCount', 'NumAliphaticHeterocycles',
    'NumAliphaticRings', 'NumAromaticHeterocycles', 'NumAromaticRings', 'NumBridgeheadAtoms',
    'NumHAcceptors', 'NumHeteroatoms', 'NumHeterocycles', 'NumRotatableBonds', 'NumSaturatedHeterocycles',
    'NumSaturatedRings', 'Phi', 'MolMR', 'fr_Al_COO', 'fr_ArN', 'fr_Ar_COO', 'fr_Ar_N', 'fr_Ar_OH',
    'fr_COO', 'fr_COO2', 'fr_C_O', 'fr_C_O_noCOO', 'fr_C_S', 'fr_HOCCN', 'fr_Imine', 'fr_NH0',
    'fr_NH1', 'fr_NH2', 'fr_N_O', 'fr_Ndealkylation1', 'fr_Ndealkylation2', 'fr_alkyl_halide',
    'fr_allylic_oxid', 'fr_amidine', 'fr_aniline', 'fr_aryl_methyl', 'fr_azide', 'fr_azo', 'fr_ester',
    'fr_ether', 'fr_guanido', 'fr_halogen', 'fr_imidazole', 'fr_lactam', 'fr_methoxy', 'fr_nitrile',
    'fr_nitroso', 'fr_phenol', 'fr_phenol_noOrthoHbond', 'fr_piperdine', 'fr_pyridine', 'fr_quatN',
    'fr_sulfide', 'fr_sulfonamd', 'fr_sulfone', 'fr_tetrazole', 'fr_thiazole'
]

# Initialize descriptor calculator
calculator = MolecularDescriptorCalculator(descriptor_names)

def smiles_to_rdkit_descriptors(smiles):
    """
    Convert a SMILES string to a vector of RDKit molecular descriptors.
    """
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        descriptors = np.array(calculator.CalcDescriptors(mol))
        return descriptors
    else:
        raise ValueError(f"❌ Invalid SMILES string: {smiles}")

def load_model(model_path):
    """
    Load the pickled LGBMRegressor model from the given path.
    """
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    print("✅ LGBMRegressor model successfully loaded!")
    return model

def predict_pKa(smiles, model):
    """
    Predict the pKa value of a given molecule from its SMILES string.
    """
    features = smiles_to_rdkit_descriptors(smiles).reshape(1, -1)  # Reshape for a single sample
    features_df = pd.DataFrame(features, columns=descriptor_names)
    predicted_pKa = model.predict(features_df)[0]
    return predicted_pKa

if __name__ == "__main__":
    


# Construct the correct path to the model file
    model_path = os.path.join("..", "notebooks", "models", "best_pKa_model.pkl")

# Normalize the path to remove any redundant ".."
    model_path = os.path.normpath(model_path)

    print(model_path)  # Debugging step to verify the correct path
    
    # Example SMILES string for Ammonia
    smiles = "[NH4+]"
    predicted_pKa = predict_pKa(smiles, model)
    print(f"🔬 Predicted pKa for {smiles}: {predicted_pKa:.2f}")






