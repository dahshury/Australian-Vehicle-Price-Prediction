import os
import numpy as np
import xgboost as xb
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.pipeline import make_pipeline
import joblib
from mlAusCar import custom_logger
from mlAusCar.config.configuartion import ModelTrainerConfig
from mlAusCar.components.data_transformation import DataTransformation
from mlAusCar.utils.common import create_dirs

class ModelTrainer:
    def __init__(self, train_config: ModelTrainerConfig, transformations: DataTransformation):
        self.train_config = train_config
        self.transformations= transformations
        create_dirs(self.train_config.root_dir)

    def train_model(self):
        X_train, y_train, X_test, y_test, log_pipeline_, preprocessing = self.transformations
        models = {
            'Random Forest': RandomForestRegressor(),
            'Decision Tree': DecisionTreeRegressor(),
            'Ada Boost': AdaBoostRegressor(),
            'Gradient Boost': GradientBoostingRegressor(),
            'XG Boost': xb.XGBRegressor()
        }

        r2_best = 0
        for name, model in models.items():
            model_pipeline = make_pipeline(preprocessing, model)
            model_pipeline.fit(X_train, y_train)
            df_predictions = model_pipeline.predict(X_test)
            
            rmse = mean_squared_error(y_true=np.exp(y_test), y_pred=np.exp(df_predictions), squared=False)
            r2 = r2_score(y_true=np.exp(y_test), y_pred=np.exp(df_predictions))
            
            if r2 > r2_best:
                final_model = model_pipeline
            
            custom_logger.info(f"{name} model results: \nRMSE: {rmse} \nAccuracy: {r2} \n{'=' * 30}")
            
        joblib.dump(final_model, os.path.join(self.train_config.root_dir, self.train_config.model_name))