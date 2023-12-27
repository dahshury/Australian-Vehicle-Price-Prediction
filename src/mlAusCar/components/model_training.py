import os
from pathlib import Path
import numpy as np
import xgboost as xb
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.pipeline import make_pipeline
import joblib
import mlflow
import mlflow.sklearn
from urllib.parse import urlparse
from mlAusCar import custom_logger
from mlAusCar.config.configuartion import ModelTrainerConfig
from mlAusCar.components.data_transformation import DataTransformation
from mlAusCar.utils.common import create_dirs, save_json

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig, transformations: DataTransformation, eval:bool = False):
        self.config = config
        self.transformations= transformations
        self.scores = {}  # Initialize an empty dictionary to store scores
        self.models = {
            'Random Forest': RandomForestRegressor(),
            'Decision Tree': DecisionTreeRegressor(),
            'Ada Boost': AdaBoostRegressor(),
            'Gradient Boost': GradientBoostingRegressor(),
            'XG Boost': xb.XGBRegressor()
        }
        self.eval = eval
        create_dirs([self.config.root_dir, self.config.eval_root_dir])
        self.model_pipeline= None

    def train_model(self):
        X_train, y_train, X_test, y_test, log_pipeline_, preprocessing = self.transformations

        r2_best = 0
        for name, model in self.models.items():
            model_pipeline = make_pipeline(preprocessing, model)
            model_pipeline.fit(X_train, y_train)
            df_predictions = model_pipeline.predict(X_test)
            
            rmse = mean_squared_error(y_true=np.exp(y_test), y_pred=np.exp(df_predictions), squared=False)
            r2 = r2_score(y_true=np.exp(y_test), y_pred=np.exp(df_predictions))
            mae= mean_absolute_error(y_true=np.exp(y_test), y_pred=np.exp(df_predictions))
            
            if r2 > r2_best:
                final_model = model_pipeline
            
            self.model_pipeline = model_pipeline
            
            # Store scores in the dictionary and construct the metrics json
            self.scores[name] = {'RMSE': rmse, 'Accuracy': r2, 'MAE': mae}
            save_json(save_path=Path(os.path.join(self.config.eval_root_dir, name + " " + self.config.metrics_file_name)), data=self.scores)
            
            custom_logger.info(f"{name} model results: \nRMSE: {rmse} \nAccuracy: {r2} \nMAE: {mae}\n{'=' * 30}")
            
            joblib.dump(model_pipeline, os.path.join(self.config.root_dir, name +" " + self.config.model_name))
            
            if self.eval:
        
                mlflow.set_registry_uri("https://dagshub.com/dahshury/Australian-Vehicle-Price-Prediction.mlflow")
                tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
                
                with mlflow.start_run():
                    
                    # Unpack scores into individual variables
                    rmse = self.scores[name]['RMSE']
                    accuracy = self.scores[name]['Accuracy']
                    mae = self.scores[name]['MAE']
                    
                    mlflow.log_metric('RMSE', rmse)
                    mlflow.log_metric('Accuracy', accuracy)
                    mlflow.log_metric('MAE', mae)
                    
                    # Model registry does not work with file store
                    if tracking_url_type_store != "file":

                        # Register the model
                        # There are other ways to use the Model Registry, which depends on the use case,
                        # please refer to the doc for more information:
                        # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                        mlflow.sklearn.log_model(self.model_pipeline, "model", registered_model_name=f"{name}")
                    else:
                        mlflow.sklearn.log_model(self.model_pipeline, f"{name}")