{"filter":false,"title":"s3.py","tooltip":"/s3/s3.py","undoManager":{"mark":10,"position":10,"stack":[[{"start":{"row":0,"column":0},"end":{"row":129,"column":7},"action":"insert","lines":["# source: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html","# some of the code included here is taken or adapted from the Amazon S3 examples available on Boto3 documentation","","import logging","import boto3","from botocore.exceptions import ClientError","","","def create_bucket(bucket_name, region=None):","    \"\"\"Create an S3 bucket in a specified region","","    If a region is not specified, the bucket is created by default in the region (us-east-1).","","    :param bucket_name: Bucket to create","    :param region: String region to create bucket in, e.g., 'us-west-2'","    :return: True if bucket created, else False","    \"\"\"","","    # Create bucket","    try:","        if region is None:","            s3_client = boto3.client('s3')","            s3_client.create_bucket(Bucket=bucket_name)","        else:","            s3_client = boto3.client('s3', region_name=region)","            location = {'LocationConstraint': region}","            s3_client.create_bucket(Bucket=bucket_name,","                                    CreateBucketConfiguration=location)","    except ClientError as e:","        logging.error(e)","        return False","    return True","    ","    ","","def list_buckets():","    # Retrieve the list of existing buckets","    s3_client = boto3.client('s3')","    response = s3_client.list_buckets()","","    # Output the bucket names","    print('Existing buckets:')","    for bucket in response['Buckets']:","        print('\\t', bucket[\"Name\"])","    ","    ","def upload_file(file_name, bucket, object_key=None):","    \"\"\"Upload a file to an S3 bucket","","    :param file_name: File to upload","    :param bucket: Bucket to upload to","    :param key: S3 object key. If not specified then file_name is used","    :return: True if file was uploaded, else False","    \"\"\"","","    # If S3 key was not specified, use file_name","    if object_key is None:","        object_key = file_name","","    # Upload the file","    s3_client = boto3.client('s3')","    try:","        response = s3_client.upload_file(file_name, bucket, object_key)","        '''","        # an example of using the ExtraArgs optional parameter to set the ACL (access control list) value 'public-read' to the S3 object","        response = s3_client.upload_file(file_name, bucket, key, ","            ExtraArgs={'ACL': 'public-read'})","        '''","        ","    except ClientError as e:","        logging.error(e)","        return False","    return True","    ","    ","    ","def delete_object(region, bucket_name, object_key):","    \"\"\"Delete a given object from an S3 bucket","    \"\"\"","    s3_client = boto3.client('s3')","    response = s3_client.delete_object(Bucket=bucket_name, Key=object_key)","    ","","","def delete_bucket(region, bucket_name):","    \"\"\"Delete a given S3 bucket","    \"\"\"","    s3_client = boto3.client('s3')","  ","    # first delete all the objects from a bucket, if any objects exist","    response = s3_client.list_objects_v2(Bucket=bucket_name)","    if response['KeyCount'] != 0:","          for content in response['Contents']:","            object_key = content['Key']","            print('\\t Deleting object...', object_key)","            s3_client.delete_object(Bucket=bucket_name, Key=object_key)","","","    # delete the bucket","    print('\\t Deleting bucket...', bucket_name)","    response = s3_client.delete_bucket(Bucket=bucket_name)","  ","    list_buckets()","  "," "," "," ","    ","def main():","    import argparse","    parser = argparse.ArgumentParser()","    parser.add_argument('bucket_name', help='The name of the bucket.')","    parser.add_argument('--file_name', help='The name of the file to upload.')","    parser.add_argument('--object_key', help='The object key')","","    region = 'us-east-1'","  ","    args = parser.parse_args()","    create_bucket(args.bucket_name)","    #list_buckets()","    ","    ","    #upload_file(args.file_name,args.bucket_name, args.object_key)","    #delete_object(region, args.bucket_name, args.object_key)","    #delete_bucket(region, args.bucket_name)"," "," ","","if __name__ == '__main__':"," main()"],"id":1}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":7,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["r"]},{"start":{"row":7,"column":1},"end":{"row":7,"column":2},"action":"insert","lines":["e"]},{"start":{"row":7,"column":2},"end":{"row":7,"column":3},"action":"insert","lines":["g"]},{"start":{"row":7,"column":3},"end":{"row":7,"column":4},"action":"insert","lines":["e"]},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["i"]}],[{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["o"],"id":3},{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["n"]}],[{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"remove","lines":["n"],"id":4},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"remove","lines":["o"]},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"remove","lines":["i"]},{"start":{"row":7,"column":3},"end":{"row":7,"column":4},"action":"remove","lines":["e"]}],[{"start":{"row":7,"column":3},"end":{"row":7,"column":4},"action":"insert","lines":["i"],"id":5},{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["o"]},{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["n"]}],[{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":[" "],"id":6},{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["="]}],[{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":[" "],"id":7}],[{"start":{"row":7,"column":9},"end":{"row":7,"column":20},"action":"insert","lines":["'us-east-1'"],"id":8}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":20},"action":"remove","lines":["region = 'us-east-1'"],"id":9},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"remove","lines":["",""]},{"start":{"row":5,"column":43},"end":{"row":6,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":105,"column":0},"end":{"row":105,"column":1},"action":"remove","lines":[" "],"id":10},{"start":{"row":104,"column":1},"end":{"row":105,"column":0},"action":"remove","lines":["",""]},{"start":{"row":104,"column":0},"end":{"row":104,"column":1},"action":"remove","lines":[" "]},{"start":{"row":103,"column":1},"end":{"row":104,"column":0},"action":"remove","lines":["",""]},{"start":{"row":103,"column":0},"end":{"row":103,"column":1},"action":"remove","lines":[" "]},{"start":{"row":102,"column":2},"end":{"row":103,"column":0},"action":"remove","lines":["",""]},{"start":{"row":102,"column":1},"end":{"row":102,"column":2},"action":"remove","lines":[" "]},{"start":{"row":102,"column":0},"end":{"row":102,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":101,"column":18},"end":{"row":102,"column":0},"action":"remove","lines":["",""],"id":11}]]},"ace":{"folds":[],"scrolltop":1560,"scrollleft":0,"selection":{"start":{"row":101,"column":18},"end":{"row":101,"column":18},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":110,"state":"start","mode":"ace/mode/python"}},"timestamp":1639568991948,"hash":"84a5433723b50b313f0bc3e2781325494090bc48"}