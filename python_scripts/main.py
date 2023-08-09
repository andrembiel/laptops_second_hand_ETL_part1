from dotenv import load_dotenv
import boto3
import os
from S3Ingestion import S3FileIngestor
from EventsGenerator import TransactionsGenerator

def generating_new_transactions(number_of_new_transactions):
    if  isinstance(number_of_new_transactions , int):
        for transaction in range (0, number_of_new_transactions):
        
            TransactionsGenerator().saving_transaction()
    else:
        pass

def ingest_file_s3(true_or_false):
    
    if true_or_false is True: 
        path = os.getcwd()+'\\.env'
        load_dotenv(path)
    
        s3_client = boto3.client(
                            's3',
                            aws_access_key_id = os.getenv('AWS_ID'),
                            aws_secret_access_key = os.getenv('AWS_KEY'),
                            region_name =  'eu-west-2')
        S3FileIngestor(s3_client = s3_client).uploading_files()

    else:
        pass

if __name__ == '__main__':
  
  number_of_new_transactions =  5 #  <--edit variable
  generating_new_transactions(number_of_new_transactions)

  ingest_file_to_s3 = False  #  <--edit variable
  ingest_file_s3(ingest_file_to_s3)