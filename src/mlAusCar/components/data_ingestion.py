from mlAusCar.config.configuartion import DataIngestionConfig
from urllib import request
from mlAusCar import custom_logger
import os

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url= self.config.source_URL,
                filename= self.config.local_data_file
            )
            custom_logger.info(f"{filename} downloaded, with info: {headers}")
        else:
            custom_logger.info(f"{self.config.local_data_file} already exists.")