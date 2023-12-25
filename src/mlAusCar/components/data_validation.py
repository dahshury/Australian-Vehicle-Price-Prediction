from pathlib import Path
import pandas as pd
from mlAusCar import custom_logger
from mlAusCar.config.configuartion import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    def validate_all_columns(self) -> bool:
        validation_status = True
        
        try:
            data= pd.read_csv(Path(self.config.local_data_file))
            all_cols = data.columns
            
            for col in all_cols:
                if col not in self.config.all_schema.keys():
                    validation_status = False
                    custom_logger.info(f"The data is modified. The column {col} is new.")
                
                if str(data[col].dtype) != self.config.all_schema[col]:
                    validation_status = False
                    custom_logger.info(f"The column {col} data type is mismatched.")
                    
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")
                        
            return validation_status
        
        except Exception as e:
            raise e