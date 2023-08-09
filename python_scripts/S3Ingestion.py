from botocore.exceptions import ClientError
import logging
import datetime
import os

class S3FileIngestor():

    def __init__(self , s3_client) -> None:         
      
        self.bucket_name = '1828-landing-zone'
        self.region = 'eu-west-2'
        self.list_of_file =  os.listdir('transaction_files')
        self.s3_client = s3_client
    
    def checking_bucket_alredy_exist(self):
        buckets_in_s3 = self.s3_client.list_buckets()
        for bucket in buckets_in_s3['Buckets']:
            if bucket['Name'] ==  self.bucket_name:
                return True
        return False
            
    def creating_bucket(self): 
        if  self.checking_bucket_alredy_exist() is False: 
            location = {'LocationConstraint': self.region}
            try: 
                self.s3_client.create_bucket(Bucket =  self.bucket_name , CreateBucketConfiguration= location)

            except  ClientError as e:
                logging.error(e)

    def uploading_files(self):
        self.creating_bucket()
        for files_ in self.list_of_file:
            object_name =  f"{os.getcwd()}\\transaction_files\\{files_}" 
            dt = str(datetime.datetime.now().date())

            filepath =  f"laptopsdirect-transaction-json/extracted_at ={dt}/{files_}"
           
            if  files_ != dt +".json":
           
                try:
                    self.s3_client.upload_file( object_name ,  self.bucket_name , filepath)
                except ClientError as e:
                    logging.error(e)
                    False
            else:
                pass
        self.deleting_files_alredy_ingested()
      
    def deleting_files_alredy_ingested(self):
        path =  f"{os.getcwd()}\\transaction_files\\"
        for file_name in os.listdir(path):
            if  file_name != str(datetime.datetime.now().date())+".json":
                os.remove(path+file_name)
                print(f"Deleting {file_name}")
        