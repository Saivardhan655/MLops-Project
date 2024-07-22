import os
import sys
import pandas as pd
import numpy as np
from src.exception.exception import customexception
from src.logger.custom_logger import logging
from src.utils.utils import load_object

class PredictPipeline:
    def __init(self):
        logging.info("intialised predictPipeline object")
    def predict(self):
        try:
            pass
        except Exception as e:
            raise customexception(e,sys)