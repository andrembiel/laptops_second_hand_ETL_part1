from Users import Costumer 
from Users import Supplier
from Products import Product
from FileWriter import DataWriter
from faker import Faker

fake = Faker('en_GB')

class TransactionsGenerator:
    def __init__ (self):
        self.costumer = Costumer().jsonGnerator()
        self.product =  Product().jsonGnerator()
        self.suplier =  Supplier().jsonGnerator()

    def transaction_generator(self  ):

        transaction_data = { 'costumer' : self.costumer,
                 'supplier'  :self.suplier,
                 'product': self.product,
                  'purchase_date':str(fake.past_datetime(start_date = '-7d')) }
        return transaction_data
    
    def saving_transaction(self):
        DataWriter().write(self.transaction_generator())