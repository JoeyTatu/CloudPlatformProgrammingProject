# This Python code file is used, similar to a class file in Java. It's like an extension to the app.py file. 

# source: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html
# some of the code included here is taken or adapted from the Amazon S3 examples available on Boto3 documentation

import logging, boto3, io, json, tweepy
import matplotlib.pyplot as plt, matplotlib.image as mpimg, numpy as np
from botocore.exceptions import ClientError

# These were used for the Twitter API, before being abandoned. 
consumer_key = "1400096255259336710-EP8EufQnDgJlEablex6z1u7qG6GgVX"
consumer_secret = "PsnxymAxut7uoWi7K7luaVqXYw400QGNkVQMuL0oReebt"
access_token = "fslJZf36Kkx5FTHfhscn1EKhQ"
access_token_secret = "xYSgMixTrYCJQIcOShNikD0SsXsRCZCloCYIYa2tIX7EuO7DRJ"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAK6sXAEAAAAArYia8aKwJtYrFBamanLfwLd95nw%3DHDu9F38FqDzkAXkgbuNKmiQxdmYJVJRAs7KdSbYWRjoZ9MSfvv"

######## S3 ######## 
def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created by default in the region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True
    
    
# Used in /list-items for demo of retrieving data from DynamoDB. 
def list_buckets():
    # Retrieve the list of existing buckets
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print('\t', bucket["Name"])
    
    
def upload_file(file_name, bucket):
    """
    Function to upload a file to an S3 bucket
    """
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)

    return response
    
    
    
def delete_object(region, bucket_name, object_key):
    """Delete a given object from an S3 bucket
    """
    s3_client = boto3.client('s3')
    response = s3_client.delete_object(Bucket=bucket_name, Key=object_key)
    


def delete_bucket(region, bucket_name):
    """Delete a given S3 bucket
    """
    s3_client = boto3.client('s3')
  
    # first delete all the objects from a bucket, if any objects exist
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    if response['KeyCount'] != 0:
          for content in response['Contents']:
            object_key = content['Key']
            print('\t Deleting object...', object_key)
            s3_client.delete_object(Bucket=bucket_name, Key=object_key)


    # delete the bucket
    print('\t Deleting bucket...', bucket_name)
    response = s3_client.delete_bucket(Bucket=bucket_name)
  
    list_buckets()
  
#  def upload_file(file_name, bucket):
#     """
#     Function to upload a file to an S3 bucket
#     """
#     object_name = file_name
#     s3_client = boto3.client('s3')
#     response = s3_client.upload_file(file_name, bucket, object_name)

#     return response

    

def list_files(bucket):
    """
    Function to list files in a given S3 bucket
    """
    s3 = boto3.client('s3')
    contents = []
    try:
        for item in s3.list_objects(Bucket=bucket)['Contents']:
            print(item)
            contents.append(item)
    except Exception as e:
        pass

    return contents
    
# def get_image(bucket, filename):
  
#     s3 =  boto3.resource('s3')
  
#     obj  = s3.Object(bucket, filename)
 

#     try:
  
#         file_stream = obj.get()['Body'].read()
        
#         if "pdf" in file_path:
#             response = HttpResponse(file_stream, content_type='application/pdf')
            
#         if "jpg" in file_path:
#             response = HttpResponse(file_stream,content_type="image/jpeg")
            
#         if "jpeg" in file_path:
#             response = HttpResponse(file_stream,content_type="image/jpeg")
            
#         if "png" in file_path:
#             response = HttpResponse(file_stream,content_type="image/png")
  
#         response['Content-Disposition'] = 'filename=%s' %  file_path
  
#         return response
#     except:
#         return False

def show_image(bucket):
    s3_client = boto3.client('s3')
    public_urls = []
    try:
        for item in s3_client.list_objects(Bucket=bucket)['Contents']:
            presigned_url = s3_client.generate_presigned_url('get_object', Params = {'Bucket': bucket, 'Key': item['Key']}, ExpiresIn = 100)
            public_urls.append(presigned_url)
    except Exception as e:
        pass
    # print("[INFO] : The contents inside show_image = ", public_urls)
    return public_urls


def download_file(file_name, bucket):
    """
    Function to download a given file from an S3 bucket
    """
    s3 = boto3.resource('s3')
    output = f"{file_name}"  ## output = f"downloads/{file_name}" -> forward slashes "/" mess it up. Use blackslashes "\"
    s3.Bucket(bucket).download_file(file_name, output)

    return output
    
######## Rekognition ######## 
def scan_image(bucket, filename):
    # #photo = "joey.png"
    
    # rek_client = boto3.client('rekognition')
    
    # #Local storage (or Cloud9 folder) - Convert into bytes first then use Rek.
    # # with open(photo, 'rb') as source_image:
    # #     source_bytes = source_image.read()

    # #response = str(rek_client.detect_labels(Image=
    # #                                {'Bytes': source_bytes},
    # #                                MaxLabels = 10,
    # #                                MinConfidence=95)
    # #                                )
       
    # # S3 Bucket                                
    # response = rek_client.detect_labels(Image=
    #                                 {'S3Object': {
    #                                     'Bucket': bucket,
    #                                     'Name': filename
    #                                 }},
    #                                 MaxLabels = 10,
    #                                 MinConfidence=95)
                                    
    # for key in response.items():
    #     if key == 'Labels':
    #         name = response.get('Labels', {}).get('Name')
    #         confidence = response.get('Labels', {}).get('Confidence')
            
    #         print(f"Name {name}. \n Confidence: {confidence}")
            
    # Moderation testing
    # response = rek_client.detect_moderation_labels(Image=
    #                                     {'S3Object': {
    #                                       'Bucket': bucket,
    #                                       'Name': filename
    #                                         }
    #                                     },
    #                                 MinConfidence=95)
    
    # #Face detection
    # response = rek_client.detect_faces(Image=
    #                                     {'S3Object': {
    #                                         'Bucket': bucket,
    #                                         'Name': filename
    #                                         }
    #                                     },
    #                                     Attributes=[
    #                                         'ALL',
    #                                     ]
    #                                 )
    
    # for key, value in response.items():
    #     if key == 'FaceDetails':
    #         for people_att in value:
    #             print(people_att)
    #             print("\n===========================\n")
    
    #json_data = json.loads(response.text)
    
    # To save to file. 
    # f = open("json_data.json", "x")
    # f.write(response)
    #print(type(response))
    # print(response)
    
    # json_object = json.dumps(response) # convert type dict to json
    # print(json_object)
    
    client = boto3.client('rekognition')
    
    ## Can do directly form S3 but must covert to bytes for local storage
    # with open(photo, 'rb') as source_image:
    #     source_bytes = source_image.read()
        
    #Local storage
    #response = str(client.detect_labels(Image=
    #                                {'Bytes': source_bytes},
    #                                MaxLabels = 10,
    #                                MinConfidence=95)
    #                                )
       
    #S3 Bucket                                
    response = client.detect_labels(Image=
                                    {'S3Object': {
                                        'Bucket': bucket,
                                        'Name': filename
                                    }},
                                    MaxLabels = 10,
                                    MinConfidence= 90)
     
    
    results_dict = {}
    results_dict['Results'] = []   
              
    for label in response['Labels']:
        name = label['Name'] 
        confidence = label['Confidence'] 
    
        
        name_str = str(name)
        conf_str = str(confidence)
        
        
        results_dict['Results'].append({"Name": name_str, "Confidence": conf_str})
    
    return results_dict
    
    
def search_tweets(query):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)
    
    return api

    
def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('bucket_name', help='The name of the bucket.')
    parser.add_argument('--file_name', help='The name of the file to upload.')
    parser.add_argument('--object_key', help='The object key')

    region = 'us-east-1'
  
    args = parser.parse_args()
    create_bucket(args.bucket_name)
    #list_buckets()
    
    
    #upload_file(args.file_name,args.bucket_name, args.object_key)
    #delete_object(region, args.bucket_name, args.object_key)
    #delete_bucket(region, args.bucket_name)
 
 

if __name__ == '__main__':
 main()