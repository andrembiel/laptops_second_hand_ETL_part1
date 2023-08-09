from faker import Faker
from unidecode import unidecode
import numpy as np
from WebScraper import ScrapProduct
import ast

fake = Faker('en_GB')

class Product():
    
    def __init__(self):
            self.all_products_info =  self._load_product_file() 
            self.id  = fake.lexify(text='??????', letters='01ABCDE')
            self.uploaded_at = str(fake.date_time_between(start_date = '-1y'))
            self.obj_type = 'Product' 
            self.web_page = 'https://www.laptopsdirect.co.uk/ct/laptops-and-netbooks/laptops'
 
    @property
    def product_info(self):
        return self.randon_product_generator()
    
    @property
    def product_brand(self):
         return self.product_info['product_brand']

    @property
    def product_title(self):
        return self.product_info['product_tile']
    
    @property
    def product_price(self):
         return self.product_info['product_price']
   
    @property
    def file_name(self) -> str:
         return 'scrape_dump_product_list.txt'
    
    def _write_product_file(self):
        with open (self.file_name , "w") as f:
            f.write(f"{self.all_products_info}")
            f.close()
    
    def _load_product_file(self) -> list:
        try:
            with open(self.file_name , "r") as f:

                return f.read().strip('[]').replace('}' , '}|').replace(', {' , '{').split('|')[0:-1]
        except FileNotFoundError:
             return None   
        
    def check_product_info(self):
        if not self.all_products_info:
            self.all_products_info =  ScrapProduct(self.web_page).getting_product_info()                          
        else: 
           None
    def check_product_file(self):
        
            if  not self._load_product_file():
                self._write_product_file()                      
            else: 
                 None


    def randon_product_generator(self)->dict:
        self.check_product_info()
        self.check_product_file()
        randon_product = np.random.choice(self._load_product_file())
       
        return ast.literal_eval(randon_product)
    
    def jsonGnerator(self):
        self.randon_product_generator()
    
        data = {
                'id' :self.id,
               'name' : self.product_title ,
                'brand' :self.product_brand ,
                'price' : self.product_price , 
                'uploaded_at' : self.uploaded_at,
                'obje_type' : self.obj_type
                    }
       
        return data