import sys 
import boto3
import botocore 

s3 = boto2.client('s3') 

def download_file(bucket, s3_name): 
    try: 
        s3_bucket.Bucket(bucktet).download_file('Python.png', 'Python_download.png') 
        print('Downloaded image Python_download.png') 
    except botocor.exceptions.clientError as e: 
        if(e.response['Error']['Code'] == "404"):
            print("The object does not exist") 
        except: 
            raise 
def upload_file(bucket_name, filename): 
    s3.upload_file(filename, bucket_name, filename) 

if __name__ = "__main__": 
    upload_file(sys.argv[1], sys.argv[2]) 
    download_file(sys.argv[1], sys.argv[2]) 
