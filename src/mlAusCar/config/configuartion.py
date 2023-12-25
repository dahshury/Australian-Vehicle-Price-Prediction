from mlAusCar.utils.common import read_yaml, create_dirs
from mlAusCar.constants import *
from mlAusCar.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig

class ConfigurationManager:
    def __init__(self,
                config_file = CONFIG_FILE_PATH,
                params_file = PARAMS_FILE_PATH,
                schema_file = SCHEMA_FILE_PATH):
    
        self.config = read_yaml(config_file)
        self.params = read_yaml(params_file)
        self.schema = read_yaml(schema_file)
        
        create_dirs([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_dirs([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file
        )
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
    
        create_dirs([self.config.data_validation.root_dir])
        config = DataValidationConfig(
            root_dir= self.config.data_validation.root_dir,
            STATUS_FILE= self.config.data_validation.status_file,
            local_data_file= self.config.data_ingestion.local_data_file,
            all_schema= self.schema.COLUMNS
        )
        return config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        create_dirs(self.config.data_transformation.root_dir)
        
        data_config= DataTransformationConfig(
            root_dir= self.config.data_transformation.root_dir,
            csv_path= self.config.data_transformation.csv_path
        )
        
        return data_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        model_trainer_config = ModelTrainerConfig(
            root_dir= self.config.model_trainer.root_dir,
            model_name= self.config.model_trainer.model_name,
            target_column=self.schema.TARGET_COLUMN.name
        )
        
        return model_trainer_config