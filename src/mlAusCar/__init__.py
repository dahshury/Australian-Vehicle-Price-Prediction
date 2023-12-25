import os
import sys
import logging

log_path = os.path.join('logs', 'running_logs.log')

os.makedirs('logs', exist_ok=True)

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s]: %(levelname)s: %(module)s: %(message)s',
                    handlers=[
                        logging.FileHandler(log_path),
                        logging.StreamHandler(sys.stdout)
                    ])

custom_logger = logging.getLogger('mlAusCar logger')