from mlAusCar.config.configuartion import ConfigurationManager
from mlAusCar.components.data_ingestion import DataIngestion
from mlAusCar import custom_logger

stage_name = 'Data ingestion stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):

        config= ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        
if __name__ == '__main__':
    try:
        custom_logger.info(f">> stage {stage_name} has started.")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        custom_logger.info(f">> stage {stage_name} has finished.\n\nx===============x")
        
    except Exception as e:
        raise e