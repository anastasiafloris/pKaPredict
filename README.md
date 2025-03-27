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

Create a new environment, you may also give the environment a different name. 

```
conda create -n pkapredict python=3.10 
```

```
conda activate pkapredict
(conda_env) $ pip install .
```

If you need jupyter lab, install it 

```
(pkapredict) $ pip install jupyterlab
```


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



