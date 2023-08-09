from faker import Faker
from unidecode import unidecode
from abc import ABC, abstractmethod
import numpy as np
import datetime
import os
import json
fake = Faker('en_GB')

class DataWriter():

    def __init__(self) -> None:
        self.directory_name = 'transaction_files'
  
    def creatting_directory(self):
    
        try:
            os.mkdir(self.directory_name)
        except FileExistsError:
            print ('saving in the' + self.directory_name)
           
    def _write_row (self , row  ) -> None:
        self.creatting_directory()
        dt = str(datetime.datetime.now().date())
        file_name = self.directory_name+'\\' + dt+'.json'
        with open (file_name , 'a')  as f:
            f.write(row)
   
            
    def write(self , data ):
        self._write_row(json.dumps(data) + "\n"  )       