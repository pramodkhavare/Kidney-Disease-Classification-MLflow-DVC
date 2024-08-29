from src.CNNClassifier.constant import * 
from src.CNNClassifier.logger import logging 
from src.CNNClassifier.utils import * 
from src.CNNClassifier.config.configuration import ConfigurationManager 
from src.CNNClassifier.exception import ClassificationException

from six.moves.urllib import request
from zipfile import ZipFile
from pathlib import Path
import os
import urllib.request as request
import zipfile
import gdown
# DataIngestionConfig(root_dir='artifacts/data_ingestion', sourse_url='https://drive.google.com/file/d/1vlhZ5c7abUKF8xXERIw6m9Te8fW7ohw3/view?usp=sharing', 
#                     local_data_file='artifacts/data_ingestion/data.zip', unzip_dir='artifacts/data_ingestion')
class DataIngestion:
    def __init__(self , config:ConfigurationManager):
        try:
            logging.info(f"{'*'*20}Data Ingestion Step Started{'*'*20}")
            self.config = config  
        except Exception as e:
            raise ClassificationException(e, sys) from e
        
    def download_file(self):
        """
        Downloads the file from the source URL if it doesn't already exist locally.
        """
        try:
    
            dataset_url = self.config.sourse_url 

            local_data_file = self.config.local_data_file
            
            
            root_dir = self.config.root_dir
            create_directories([root_dir])
            logging.info(f'Succssfully created directory at {root_dir}') 
            
            file_id = dataset_url.split('/')[-2]
            prefix =  'https://drive.google.com/uc?/export=download&id='
            print(prefix + file_id ,local_data_file)
            gdown.download(prefix + file_id ,local_data_file)
            
            
            logging.info(f'Successfully downloaded data at {local_data_file}')
            
            return local_data_file
            
        except Exception as e:
            raise ClassificationException(e, sys) from e
    # def download_file(self)-> str:
    #     '''
    #     Fetch data from the url
    #     '''

    #     try: 
    #         dataset_url = self.config.sourse_url
    #         zip_download_dir = self.config.local_data_file
    #         os.makedirs("artifacts/data_ingestion", exist_ok=True)
    #         logging.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

    #         file_id = dataset_url.split("/")[-2]
    #         prefix = 'https://drive.google.com/uc?/export=download&id='
    #         gdown.download(prefix+file_id,zip_download_dir)

    #         logging.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

    #     except Exception as e:
    #         raise e  
    
    def unzip_file(self):
        try:

            unzip_path = self.config.unzip_dir

            create_directories([unzip_path])
            print(self.config.local_data_file)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logging.info(f"Extracted all files to {unzip_path}") 
        
        except Exception as e:
            raise ClassificationException(e, sys) from e
        
    def initialize_data_ingestion(self):
        try:
            tgz_file_path = self.download_file() 
            self.unzip_file()
            logging.info(f"{'*'*20}Data Ingestion Step Completed{'*'*20}")
            # print("Data Ingestion Completed")
        except Exception as e:
            raise ClassificationException(e, sys) from e
        