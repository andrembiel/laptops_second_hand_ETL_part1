from faker import Faker
from unidecode import unidecode
from abc import ABC, abstractmethod
import numpy as np
import datetime

fake = Faker('en_GB')

class User(ABC):
    def __init__ (self):
       
        self.id = fake.lexify(text='??????', letters='01ABCDE')
        self.name = unidecode(fake.first_name())
        self.surname = fake.last_name()
        self.dob = str(fake.date_of_birth(minimum_age = 21 , maximum_age = 59))
        self.adress = fake.address()
        self.user_created_at = datetime.datetime.now()

    @abstractmethod
    def email(self):
        pass

class Supplier(User):
    def __init__ (self):
       
        self.bank_account = fake.iban() 
        self.obj_type = 'Supplier'
        super().__init__()
          
    @property
    def email(self):
        return  fake.ascii_company_email()
    
    def jsonGnerator(self): 
        data = {
                'id' : self.id ,
                'name' : self.name ,
                'surname' :self.surname ,
                'dob' : self.dob ,
                'addres' : self.adress , 
                'email' : self.email,
                'bank_acc' : self.bank_account ,
                'created_at' : str(self.user_created_at.strftime('%Y/%m/%d')),
                 'user_type' : self.obj_type 
                    }
        return data

class Costumer(User):
    def __init__ (self):
       
        self.obj_type = 'Costumer'
        super().__init__()
           
    @property
    def email(self) -> str:
        return  fake.ascii_free_email()
    
    def jsonGnerator(self): 
        data = {
                'id' : self.id ,
                'name' : self.name ,
                'surname' :self.surname ,
                'dob' : self.dob ,
                'addres' : self.adress , 
                'email' : self.email,
                'created_at' : str(self.user_created_at.strftime('%Y/%m/%d')),
                'user_type' : self.obj_type 
                    }
     
        return data
        
   
