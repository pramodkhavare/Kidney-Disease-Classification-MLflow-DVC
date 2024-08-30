from src.CNNClassifier.constant import * 
from src.CNNClassifier.logger import logging 
from src.CNNClassifier.utils import * 
from src.CNNClassifier.config.configuration import ConfigurationManager 

from src.CNNClassifier.components.data_ingestion import DataIngestion 
from src.CNNClassifier.components.prepare_base_model import PreparepareBaseModel


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
    
    def start_prepare_base_model(self):
        try:
            prepare_base_model_config = self.config.get_prepare_base_model_config()
            prepare_base_model = PreparepareBaseModel(
                config= prepare_base_model_config
            ) 
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
    
        except Exception as e:
            raise e 
    
    
    def run_pipeline(self):
        try:
            data_ingestion_artifacts = self.start_data_ingestion() 
            prepare_base_model_artifacts = self.start_prepare_base_model()
        except Exception as e:
            raise e 
        
    def run(self):
        try:
            self.run_pipeline() 
        except Exception as e:
            raise e 