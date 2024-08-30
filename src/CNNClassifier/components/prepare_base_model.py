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

class PreparepareBaseModel:
    def __init__(self ,config: ConfigurationManager):
        try:
            self.config = config  
            
        except Exception as e:
            raise ClassificationException(e, sys) from e
        
        
    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            for layer in model.layers:
                model.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)

        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        full_model.summary()
        return full_model
    

    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    
    
    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
    
    def get_base_model(self):
        try:
     
            self.model = tf.keras.applications.VGG16(
                include_top=self.config.params_include_top,
                weights=self.config.params_weights,
                input_shape=self.config.params_image_size 
            )  
            
            self.save_model(path = self.config.base_model_path , model = self.model)
        
        except Exception as e:
            raise ClassificationException(e, sys) from e
    