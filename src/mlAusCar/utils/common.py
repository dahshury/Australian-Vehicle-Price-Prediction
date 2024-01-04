import os
from pathlib import Path
import pandas as pd
import yaml
import json
import joblib
from typing import Any, Union
from box import ConfigBox
from box.exceptions import BoxValueError
import zipfile
from mlAusCar import custom_logger
from mlAusCar.constants import CONFIG_FILE_PATH
from ensure import ensure_annotations

@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    """reads a yaml file, returning it as a ConfigBox
    
    Input: .yaml
    
    Raises: ValueError if the file is empty
    
    output: ConfigBox"""
    
    try:
        with open(path) as f:
            content = yaml.safe_load(f)
            custom_logger.info(f".yaml from {path} has been loaded.")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError(".yaml file is empty")
    
    except Exception as e:
        return e

def extract_zip(zip_file_path, destination: str, verbose=False):
    create_dirs(destination)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Extract the specific file to the destination directory
        zip_ref.extractall(destination)
    if verbose:
        custom_logger.info(f"File {zip_file_path} has been extracted")
    
@ensure_annotations
def create_dirs(paths: Union[list, str], verbose = False):
    """Creates directories given in the list passed to the function
    Args: 
        Paths: List of directories
        verbose: Whether to log the directories made.
    """
    if not isinstance(paths, list):
        paths = [paths]
        
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            custom_logger.info(f"Created directory {path}")
            
@ensure_annotations
def save_json(save_path: Path, data: dict):
    """Saves json data into a .json file stored in the given path
    Args:
        path: The path of the .json file that the data will be stored in.
        data: a dictionary resembling the json data
    """
    with open(save_path, 'w') as f:
        json.dump(obj=data, fp=f, indent=4)
        
    custom_logger.info(f".json file saved at {save_path}")
        
@ensure_annotations
def load_json(path: str) -> ConfigBox:
    with open(path, 'w') as f:
        content = json.load(f)
    
    custom_logger.info(f".json loaded from {path} as a Configbox")    
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, save_path: Path):
    """saves binary data to path
    Args:
        data (Any): data to be saved as binary
        path (Path): path of data to be saved
    """
    data = joblib.dump(data, save_path)
    custom_logger.info(f"Data saved to {save_path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """loads binary data from path
    Args: 
        path (Path): path of input binary data
    
    returns: 
        Any: object stored in the file     
    """
    data = joblib.load(path)
    custom_logger.info(f"Data loaded from {path}")
    
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Get size of file in KB
    Args:
        path (Path): path of the file to be measured
    
    returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f" File size is ~ {size_in_kb} KB"

def filter_choices(filters):
    # Load CSV data into a DataFrame
    csv_path = read_yaml(CONFIG_FILE_PATH).data_transformation.root_dir + "/cleaned.csv"
    data = pd.read_csv(csv_path)
    defaults = {}
    if filters == {}:
        for key in ["Brand", "UsedOrNew", "State"]:
            defaults[key] = data[key].unique().tolist()
        return defaults
    # Apply filters to the DataFrame
    for key, value in filters.items():
        # Checking entered data types matches the type of column's data
        
        if data[key].dtype.name in ('int32', 'int64') and not isinstance(value, int):
            try:
                value = int(value)
                filters[key] = value
            except:
                raise ValueError(f"Value {value} is not of type int for column {key}.")
            
        elif data[key].dtype.name == 'float64' and not isinstance(value, float):
            try:
                value = float(value)
                filters[key] = value
            except:
                raise ValueError(f"Value {value} is not of type float for column {key}.")
            
        elif data[key].dtype.name == 'object' and not isinstance(value, str):
            try:
                value = str(value)
                filters[key] = value
            except:
                raise ValueError(f"Value {value} is not of type string for column {key}.")
            
        data = data[data[key] == value]

    # Extract unique choices for each column
    choices = {}
    for column in data.columns:
        choices[column] = data[column].unique().tolist()

    # Create the JSON response
    response = {'filters': filters, 'choices': choices}

    return response