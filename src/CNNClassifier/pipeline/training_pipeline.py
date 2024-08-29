from src.CNNClassifier.constant import * 
from src.CNNClassifier.logger import logging 
from src.CNNClassifier.utils import * 
from src.CNNClassifier.config.configuration import ConfigurationManager 

from src.CNNClassifier.components.data_ingestion import DataIngestion


import os ,sys
import pandas as pd
import uuid
from threading import Thread
from collections import namedtuple
from datetime import datetime


class TrainPipeline():
    def __init__(self ,config: ConfigurationManager):
        try:
            self.config = config  
        except Exception as e:
            raise e 
        
    def start_data_ingestion(self ):
        try:
            data_ingestion_config = self.config.get_data_ingestion_config()
            data_ingestion = DataIngestion(
                config= data_ingestion_config
            ) 
            data_ingestion.initialize_data_ingestion()
        except Exception as e:
            raise e 
    
    
    
    
    def run_pipeline(self):
        try:
            data_ingestion_artifacts = self.start_data_ingestion() 
            # data_validation_artifacts = self.start_data_Validation()
            # data_transformation_artifacts = self.start_data_transformation()
            # model_training_artifacts = self.start_model_training()
            # model_evaluation_artifacts = self.start_model_evaluation()
        except Exception as e:
            raise e 
        
    def run(self):
        try:
            self.run_pipeline() 
        except Exception as e:
            raise e 