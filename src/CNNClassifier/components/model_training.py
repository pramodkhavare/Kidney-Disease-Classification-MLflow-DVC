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
import tensorflow as tf 


class ModelTrainer:
    def __init__(self ,config:ConfigurationManager):
        try:
            self.config = config  
        except Exception as e:
            raise ClassificationException(e, sys) from e 
        
    def get_base_model(self):
        try:
 
            self.model = tf.keras.models.load_model(
                filepath= self.config.updated_base_model_path
            )     
            return self.model  
        except Exception as e:
            raise ClassificationException(e, sys) from e 
    def train_valid_generator(self):
        try:
            datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
        ) 
            dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )
            valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )
            self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )
            if self.config.params_is_augmentation:
                train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
            else:
                train_datagenerator = valid_datagenerator
            
            self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
            )

        except Exception as e:
            raise ClassificationException(e, sys) from e 
        
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
        
    # def train(self, callback_list: list):
    def train(self ):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator 
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )  