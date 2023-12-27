from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    local_data_file: str
    all_schema: dict
    
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    csv_path: Path
    
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    model_name: str
    target_column: str
    metrics_file_name: Path
    eval_root_dir: Path