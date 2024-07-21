import pandas as pd
import numpy as np
from src.logger.logger import logging
from src.exception.exception import customexception
import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")
        try:
            data = pd.read_csv(r'expirement\gemstone.csv')  # Fixed path
            logging.info("Reading CSV file")

            # Ensure the directory exists
            artifacts_dir = os.path.dirname(self.ingestion_config.raw_data_path)
            if not os.path.exists(artifacts_dir):
                os.makedirs(artifacts_dir)
            
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Saved file to artifacts folder")

            logging.info("Data is splitting into train and test files")
            train_data, test_data = train_test_split(data, test_size=0.25)
            logging.info("Train-test split completed")

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info('Data ingestion completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.error("Exception occurred while reading the data", exc_info=True)
            raise customexception(e, sys)

if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()
