from mlAusCar import custom_logger
from mlAusCar.pipeline.stage_01_data_ingestion import  DataIngestionTrainingPipeline
from mlAusCar.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlAusCar.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlAusCar.pipeline.stage_04_model_training import ModelTrainingPipeline

stage_name = 'Data Ingestion'
try:
    custom_logger.info(f">> stage {stage_name} has started.")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    custom_logger.info(f">> stage {stage_name} has finished.\n\nx===============x")
    
except Exception as e:
    raise e

stage_name= 'Data Validation'
try:
    custom_logger.info(f">> stage {stage_name} has started.")
    obj = DataValidationTrainingPipeline()
    obj.main()
    custom_logger.info(f">> stage {stage_name} has finished.\n\nx===============x")
    
except Exception as e:
    raise e

stage_name= 'Data Transformation'
try:
    custom_logger.info(f">> stage {stage_name} has started.")
    obj = DataTransformationTrainingPipeline()
    transformation_obj = obj.main()
    custom_logger.info(f">> stage {stage_name} has finished.\n\nx===============x")
    
except Exception as e:
    raise e

stage_name= 'model_training'
try:
    custom_logger.info(f">> stage {stage_name} has started.")
    obj = ModelTrainingPipeline(transformation_obj=transformation_obj, eval=False)
    obj.main()
    custom_logger.info(f">> stage {stage_name} has finished.\n\nx===============x")
    
except Exception as e:
    raise e