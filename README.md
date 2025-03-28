![Project Logo](assets/banner.png)

![Coverage Status](assets/coverage-badge.svg)

<h1 align="center">
pKaPredict
</h1>

<br>


pKaPredict project

## 📦 Overview
This package provides a streamlined pipeline for predicting the pKa values of molecules from their SMILES strings using machine learning. It includes tools for data cleaning, descriptor generation via RDKit, and model training using LightGBM and other regressors. The package is designed to be easily pip-installable and modular, making it ideal for cheminformatics applications and molecular property prediction tasks. 

## 🎀 Summary
🤯 Acquiring Dataset <br>
🧹 Cleaning Dataset <br>
🛟 Saving the cleaned data to a csv file <br>
🤓 Computation of RDKit Molecular Descriptors <br>
💡 Formatting the dataset for machine learning <br>
🕹️ Machine learning model selection <br>
🌲 Machine learning model 🥇: ExtraTreesRegressor <br>
🤖 Machine learning model 🥈 : LGBMRegressor <br>
🧐 Comparison of the two machine learning models <br>
🧅 Saving the LGBMRegressor trained model <br>
🩷 Usage of this trained machine learning model

## 👩‍💻 Installation

### 🌱 Environment setup

1. **Clone the repository**:

```bash
git clone https://github.com/TonNomUtilisateur/pKaPredict.git
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
pip install .
```

4. **Install jupyter lab**:
```bash
pip install jupyterlab
```

🍏 For macOS users (⚠ required for LightGBM to work):

4. **Install the system library libomp**:
```bash
brew install libomp
```
If brew is not installed, follow the instructions here: https://brew.sh




## 🛠️ Development installation

Initialize Git (only for the first time). 

Note: You should have create an empty repository on `https://github.com:anastasiafloris/pKaPredict`.

```
git init
git add * 
git add .*
git commit -m "Initial commit" 
git branch -M main
git remote add origin git@github.com:anastasiafloris/pKaPredict.git 
git push -u origin main
```

Then add and commit changes as usual. 

To install the package, run

```
(pkapredict) $ pip install -e ".[test,doc]"
```

### Run tests and coverage

```
(conda_env) $ pip install tox
(conda_env) $ tox
```



