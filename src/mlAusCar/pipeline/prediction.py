import joblib
import numpy as numpy
import pandas as pd
from pathlib import Path

class PredictionPipeline:
    def __init__(self, model_path):
        self.model_path= model_path
        self.model= joblib.load(Path(model_path))
        
    def predict(self, data):
        prediction= self.model.predict(data)
        
        return prediction