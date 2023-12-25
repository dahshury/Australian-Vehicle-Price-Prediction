from mlAusCar.config.configuartion import ConfigurationManager
from mlAusCar.components.data_validation import DataValidation
from mlAusCar import custom_logger

stage_name = 'Data validation stage'

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):

        config = ConfigurationManager()
        val_config = config.get_data_validation_config()
        obj = DataValidation(val_config)
        obj.validate_all_columns()

if __name__ == '__main__':
    try:
        custom_logger.info(f">> stage {stage_name} has started.")
        obj = DataValidationTrainingPipeline()
        obj.main()
        custom_logger.info(f">> stage {stage_name} has finished.\n\nx===============x")
        
    except Exception as e:
        raise e