import pytest
from pkapredict.load_model import load_model

def test_load_model_file_not_found(monkeypatch):
    # Simulate the model path check returning False
    monkeypatch.setattr("os.path.exists", lambda _: False)

    with pytest.raises(FileNotFoundError, match="❌ Model file not found"):
        load_model()