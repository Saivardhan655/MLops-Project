import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import customexception
import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path
from src.utils.utils import save_object,evaluate_model
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

@dataclass
class ModelTrainerConfig:
    pass
class ModelTrainer:
    def __init__(self):
        pass
    def initate_model_training(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)