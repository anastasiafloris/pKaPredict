import os
import pickle

def load_model(): 
    """
    Load a pickled LGBMRegressor trained model from the package's models directory.

    """
    base_dir = os.path.dirname(os.path.abspath(__file__))  
    model_path = os.path.join(base_dir, "models", "best_pKa_model.pkl")

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"❌ Model file not found at: {model_path}")

    with open(model_path, "rb") as file:
        model = pickle.load(file)
    print("✅ LGBMRegressor model successfully loaded!")
    return model






