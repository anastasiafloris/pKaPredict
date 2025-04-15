![Project Logo](assets/banner.png)

![Coverage Status](assets/coverage-badge.svg)

<h1 align="center">
pKaPredict
</h1>

<br>




## 📦 Overview

*pKaPredict* is a cheminformatics tool that predicts the acid dissociation constant (pKa) of chemical compounds from their SMILES strings.  The package is designed to be easily pip-installable and modular, making it ideal for cheminformatics applications. The package combines RDKit generated molecular descriptors with a pre-trained LGBMRegressor model for fast, reproducible predictions. The workflow includes training data preprocessing, descriptor generation, model loading, prediction, and result visualization.

💡 Main Functions :

*Functions used to train the machine learning model on a training dataset*

→ **clean_and_visualize_pka**
Cleans the training dataset by removing duplicates and missing values; also provides basic visualizations for data exploration.

→ **RDKit_descriptors**
Transforms a DataFrame of SMILES into molecular descriptors, used for training the model.
    
→ **plot_data**
Creates scatter plots comparing predicted vs. experimental pKa values to evaluate model performance and choose the most adapted model for this usage.

*Core functions for predicting pKa from user-provided SMILES inputs*

→ **load_model**
Loads the pre-trained LightGBM model optimized for pKa prediction.

→ **smiles_to_rdkit_descriptors**
Converts a user-provided SMILES input into a vector of RDKit molecular descriptors.

→ **predict_pKa**
Takes molecular descriptors as input and returns predicted pKa values using the loaded model.


## 👩‍💻 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/anastasiafloris/pKaPredict.git
cd pKaPredict
```
2. **Create and activate the conda environnement**:


If your project includes an environment.yml file:
```bash 
conda env create -n pkapredict_env -f environment.yml
conda activate pkapredict_env
```
If not, you can create one manually:
```bash
conda create -n pkapredict_env python=3.10 -y
conda activate pkapredict_env
```
3. **Install the package**:
```bash 
pip install pKaPredict
```

4. **Install jupyter lab**:
```bash
pip install jupyterlab
```

🍏 For macOS users (⚠ required for LightGBM to work):

5. **Install the system library libomp**:
```bash
brew install libomp
```
If brew is not installed, follow the instructions here: https://brew.sh

6. **The package is yours 🎁**:

Run the test_package.py file in a python or jupyter environment to predict the pKa of a molecule of your choice, using its SMILES string.


## 🪪 License 

This project is licensed under the MIT License.  
You are free to use, modify, and distribute it with proper attribution.


## 📗 References

The dataset used in this project is the [test_acids_bases_descfinal_nozwitterions.csv](https://github.com/cbio3lab/pKa/blob/main/Data/test_acids_bases_descfinal_nozwitterions.csv) file from the cbio3lab repository.  
It was originally extracted from the Harvard [Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/6A67L9).

## 👯‍♀️ Authors

This project was completed as part of the EPFL course *Practical Programming in Chemistry*.
- [Anastasia Floris](https://github.com/anastasiafloris)  
- [Candice Habert](https://github.com/candicehbt)