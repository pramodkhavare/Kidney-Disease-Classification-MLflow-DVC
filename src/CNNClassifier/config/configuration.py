from  src.CNNClassifier.constant import  *
from src.CNNClassifier.exception import * 
from src.CNNClassifier.logger import logging 
from src.CNNClassifier.utils import *
from src.CNNClassifier.exception import ClassificationException
from src.CNNClassifier.entity.config_entity import (
    DataIngestionConfig , DataValidationConfig , DataTransformationConfig ,ModelEvaluationConfig ,ModelTrainerConfig
)

class ConfigurationManager():
    def __init__(self ,
                 config_file_path =CONFIG_FILE_PATH,
                #  params_file_path =PARAMS_FILE_PATH,
                 schema_file_path = SCHEMA_FILE_PATH,
                 current_time_stamp =CURRENT_TIME_STAMP):
        try:
            self.config_file_path = config_file_path 
            # self.params_file_path = params_file_path
            self.schema_file_path = schema_file_path
            self.current_time_stamp = current_time_stamp
            
            
            self.config = read_yaml(self.config_file_path)
            self.schema = read_yaml(self.schema_file_path)
            # self.params = read_yaml(self.params_file_path)
            
             
            create_directories([self.config[ARTIFACTS_ROOT]])
        except Exception as e:
            raise ClassificationException(e, sys) from e
        
    def get_data_ingestion_config(self )->DataIngestionConfig:
        try:
            config = self.config[DATA_INGESTION_CO]
            create_directories([config[ROOT_DIR]])
            data_ingestion_config = DataIngestionConfig(
                root_dir= config[ROOT_DIR],
                sourse_url= config[SOURCE_URL],
                local_data_file= config[LOCAL_DATA_FILE],
                unzip_dir= config[UNZIP_DIR]
            ) 
            
            return data_ingestion_config
        except Exception as e:
            raise ClassificationException(e, sys) from e 
        
        
    def get_da
        
