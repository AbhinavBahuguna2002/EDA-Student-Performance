'''
The given code defines a class `DataIngestionConfig` using the `@dataclass` decorator. It has three attributes `train_data_path`, `test_data_path`, and `raw_data_path`, which are initialized with default values using the `os.path.join()` function. 
These default values are relative file paths pointing to CSV files located in the "artifacts" directory.

Next, the code defines a class `DataIngestion`, which has an `__init__` method that creates an instance of `DataIngestionConfig` and assigns it to the `ingestion_config` attribute.

The class `DataIngestion` also has a method called `initiate_data_ingestion`, which performs the following steps:

1. Reads a CSV file named "stud.csv" located in the "notebook\data" directory and stores it as a Pandas DataFrame.
2. Creates the directory structure for the `train_data_path` using `os.makedirs()` if it doesn't already exist.
3. Saves the DataFrame as a CSV file at `raw_data_path` location.
4. Splits the DataFrame into a training set and a test set using the `train_test_split` function from scikit-learn, with a test size of 0.2 and a random state of 42.
5. Saves the training set as a CSV file at `train_data_path` location and the test set as a CSV file at `test_data_path` location.
6. Logs the progress and completion of the data ingestion process.
7. Finally, it returns a tuple containing the paths of the generated training and test data files.

If any exception occurs during the data ingestion process, it raises a custom exception `CustomException`, passing the original exception `e` and the `sys` module.

The `if __name__ == "__main__"` block creates an instance of the `DataIngestion` class and calls the `initiate_data_ingestion` method, triggering the execution of the data ingestion process when the script is run directly.

'''

import os 
import sys 
import pandas as pd
from src.exception import CustomException
from src.logger import logging

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass #decorator
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts', 'train.csv')
    test_data_path: str=os.path.join('artifacts', 'test.csv')
    raw_data_path: str=os.path.join('artifacts', 'raw.csv')

class DataIngestion: 
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    # To read data from a file/database
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Reading Dataset
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the dataset as a dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)            

            logging.info("Train Test split initiated")
            train_set, test_set= train_test_split (df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            #saving test file
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (

                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )            
        except Exception as e:
            raise CustomException(e,sys)

