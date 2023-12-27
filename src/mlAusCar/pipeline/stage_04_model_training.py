from mlAusCar.config.configuartion import ConfigurationManager
from mlAusCar.components.model_training import ModelTrainer
from mlAusCar.components.data_transformation import DataTransformation
from mlAusCar import custom_logger

stage_name = 'Model training stage'

class ModelTrainingPipeline:
    def __init__(self, transformation_obj: DataTransformation, eval: bool = False):
        self.transformation_obj= transformation_obj
        self.eval= eval
    def main(self):
        
        try:
            config= ConfigurationManager()
            data_training_config= config.get_model_trainer_config()
            trainer=ModelTrainer(data_training_config, self.transformation_obj, eval= self.eval)
            trainer.train_model()
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    try:
        custom_logger.info(f">> stage {stage_name} has started.")
        obj = ModelTrainingPipeline()
        obj.main()
        custom_logger.info(f">> stage {stage_name} has finished.\n\nx===============x")
        
    except Exception as e:
        raise e