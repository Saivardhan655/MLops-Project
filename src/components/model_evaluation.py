import pandas as pd
import numpy as np
from src.logger.custom_logger import logging
from src.exception.exception import customexception
import os
import sys
import mlflow
import mlflow.sklearn
import pickle
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from urllib.parse import urlparse
from dataclasses import dataclass
@dataclass
class ModelEvaluationConfig:
    pass
class ModelEvaluation:
    def __init__(self):
        pass
    def initiate_model_evaluation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)
        