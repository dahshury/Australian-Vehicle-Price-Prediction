from mlAusCar.config.configuartion import ConfigurationManager
from mlAusCar.components.data_transformation import DataTransformation
from mlAusCar import custom_logger
from pathlib import Path

stage_name = 'Data transformation stage'

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            val_config= config.get_data_validation_config()
            
            with open(Path(f"{val_config.STATUS_FILE}"), 'r') as f:
                status = f.read().split(" ")[-1]
            if status == "True":
                transformation_config = config.get_data_transformation_config()
                obj = DataTransformation(transformation_config)
                obj = obj.transform_data()
            
            else:
                raise Exception("The data validation status is False.")
            
            return obj
        
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    try:
        custom_logger.info(f">> stage {stage_name} has started.")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        custom_logger.info(f">> stage {stage_name} has finished.\n\nx===============x")
        
    except Exception as e:
        raise e