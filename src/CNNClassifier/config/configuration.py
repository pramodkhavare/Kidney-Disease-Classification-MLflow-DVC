from  src.CNNClassifier.constant import  *
from src.CNNClassifier.exception import * 
from src.CNNClassifier.logger import logging 
from src.CNNClassifier.utils import *
from src.CNNClassifier.exception import ClassificationException
from src.CNNClassifier.entity.config_entity import (
    DataIngestionConfig , PrepareBaseModelConfig ,TrainingConfig
)

class ConfigurationManager():
    def __init__(self ,
                 config_file_path =CONFIG_FILE_PATH,
                 params_file_path =PARAMS_FILE_PATH,
                 schema_file_path = SCHEMA_FILE_PATH,
                 current_time_stamp =CURRENT_TIME_STAMP):
        try:
            self.config_file_path = config_file_path 
            self.params_file_path = params_file_path
            self.schema_file_path = schema_file_path
            self.current_time_stamp = current_time_stamp
            
            
            self.config = read_yaml(self.config_file_path)
            self.schema = read_yaml(self.schema_file_path)
            self.params = read_yaml(self.params_file_path)
            
             
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
        
        
    def get_prepare_base_model_config(self)->PrepareBaseModelConfig:
        try:
            config = self.config[PREPARE_BASE_MODEL]
            params = self.params

            prepare_base_model_config = PrepareBaseModelConfig(
                root_dir=config[ROOT_DIR] ,base_model_path=config[BASE_MODEL_PATH] , updated_base_model_path= config[UPDATED_BASE_MODEL_PATh],
                params_image_size= params.IMAGE_SIZE,
                params_learning_rate = params.LEARNING_RATE 
                ,params_include_top=params.INCLUDE_TOP ,
                params_weights = params.WEIGHTS,
                params_classes= params.CLASSES
            ) 
            return prepare_base_model_config
        except Exception as e:
            raise ClassificationException(e, sys) from e 
        
        
    def get_model_training_config(self)-> TrainingConfig:
        try:
            config = self.config[TRAINING]
            params = self.params
            training_config = TrainingConfig(
                 root_dir= config.ROOT_DIR ,
                 trained_model_path=  config.TRAINED_MODEL_PATH ,
                 updated_base_model_path= config.UPDATED_BASE_MODEL_PATh ,
                 training_data= config.TRAINING_DATA ,
                 params_epochs= params.EPOCHS,
                 params_batch_size= params.BATCH_SIZE,
                 params_is_augmentation= params.AUGMENTATION,
                 params_image_size= params.IMAGE_SIZE
             )
            print(training_config)
            return training_config
        except Exception as e:
            raise ClassificationException(e, sys) from e 
