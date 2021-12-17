# @Ref - PyLenin - Part 1: https://www.youtube.com/watch?v=Jtr0gyM9rCI
# @Ref - PyLenin - Part 2: https://www.youtube.com/watch?v=_cQEuLGv45o
# @Ref - PyLenin - Part 3: https://www.youtube.com/watch?v=P8MKBU3dx-k
# @Ref - PyLenin - Part 4: https://www.youtube.com/watch?v=mQYjSsH2-KY

import boto3
import json

BUCKET = "cpp-project-jtatu"

FOLDER = 'testing/'
JOEY =  FOLDER + "Joey_30_Sept.png"
BEYONCE = FOLDER + "beyonce_rekognition_moderation_testing.jpg"
MANBEARD = FOLDER + "man_beard.jpg"
MEN = FOLDER + "men_group.jpg"

#photo = "joey.png"

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
                                    'Bucket': BUCKET,
                                    'Name': JOEY
                                }},
                                MaxLabels = 10,
                                MinConfidence=95)
                                
                                
# @ref: Hugo - https://stackoverflow.com/questions/51192145/aws-rekognition-responsefacedetails               
for labels in response['Labels']:
    name = labels['Name'] #to get the whole bounding box.
    confidence = labels['Confidence'] 
    # width = imgWidth * box['Width'] #the width of the bb.
    print(str(name) + ", " + str(confidence)) #access age range low & high






#     if key == 'Labels':
#         #name = response.get('Labels', {}).get('Name')
#         #confidence = response.get('Labels', {}).get('Confidence')
#

# <class '__main__.Hasher'>
        
        #print(f"Name {name}. \n Confidence: {confidence}")

#Moderation testing
# response = client.detect_moderation_labels(Image=
#                                     {'S3Object': {
#                                         'Bucket': BUCKET,
#                                         'Name': BEYONCE
#                                         }
#                                     },
#                                 MinConfidence=95)

#Face detection
# response = client.detect_faces(Image=
#                                     {'S3Object': {
#                                         'Bucket': BUCKET,
#                                         'Name': MEN
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