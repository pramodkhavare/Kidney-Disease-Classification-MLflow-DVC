import os ,sys 
from pathlib import Path 
from datetime import datetime 


CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
ROOT_DIR = os.getcwd()  
CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("config/params.yaml")
SCHEMA_FILE_PATH = Path("config/schema.yaml") 

ARTIFACTS_ROOT = 'artifacts_root'

DATA_INGESTION_CO = 'data_ingestion'
ROOT_DIR = 'root_dir'
SOURCE_URL = 'source_URL'
LOCAL_DATA_FILE = 'local_data_file'
UNZIP_DIR = 'unzip_dir'

PREPARE_BASE_MODEL = 'prepare_base_model'
ROOT_DIR = 'root_dir'
BASE_MODEL_PATH = 'base_model_path' 
UPDATED_BASE_MODEL_PATh = 'updated_base_model_path'

PREPARE_CALLBACKS = 'prepare_callbacks'
ROOT_DIR = 'root_dir'
TENSORBOARD_ROOT_LOG_DIR = 'tensorboard_root_log_dir'
CHECKPOINT_MODEL_FILEPATH = 'checkpoint_model_filepath'

TRAINING = 'training'
ROOT_DIR = 'root_dir'
TRAINED_MODEL_PATH = 'trained_model_path'
TRAINING_DATA = 'training_data'