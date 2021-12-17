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
# response = client.detect_labels(Image=
#                                 {'S3Object': {
#                                     'Bucket': BUCKET,
#                                     'Name': JOEY
#                                 }},
#                                 MaxLabels = 10,
#                                 MinConfidence=95)

#Moderation testing
# response = client.detect_moderation_labels(Image=
#                                     {'S3Object': {
#                                         'Bucket': BUCKET,
#                                         'Name': BEYONCE
#                                         }
#                                     },
#                                 MinConfidence=95)

#Face detection
response = client.detect_faces(Image=
                                    {'S3Object': {
                                        'Bucket': BUCKET,
                                        'Name': MEN
                                        }
                                    },
                                    Attributes=[
                                        'ALL',
                                    ]
                                )

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

json_object = json.dumps(response)
print(json_object)