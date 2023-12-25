import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'mlAuscar'

file_list = [
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuartion.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/entity/config_entity.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'schema.yaml',
    'main.py',
    'app.py',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'templates/index.html'
]

# Creating logic for creating the files
for file in file_list:
    foldername, filename = os.path.dirname(file), os.path.basename(file)
    if os.path.exists(Path(file)):
        logging.info(f'File {file} already exists')
    
    elif foldername != "" :
        os.makedirs(foldername, exist_ok=True)
        with open(file, 'w'):
            pass
        logging.info(f'File {file} has been created')
        
    else:
        with open(file, 'w'):
            pass
        logging.info(f'File {file} has been created')