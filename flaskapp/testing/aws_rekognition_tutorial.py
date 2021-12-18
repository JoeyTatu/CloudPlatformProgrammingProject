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
                                MinConfidence=0)
 

results_dict = {}
results_dict['Results'] = []
# results_dict['Results']['Name'] = ""
# results_dict['Results']['Confidence'] = ""
# @ref: Hugo - https://stackoverflow.com/questions/51192145/aws-rekognition-responsefacedetails               
for label in response['Labels']:
    name = label['Name'] #to get the whole bounding box.
    confidence = label['Confidence'] 
    # # width = imgWidth * box['Width'] #the width of the bb.
    
    # results[label] = values[name]
    
    # results['Name'] = label['Name']
    # results['Confidence'] = label['Confidence']
    # results = results_dict['Results']
    # results['Name'] = labels['Name'] 
    # results['Confidence'] = labels['Confidence']
    
    name_str = str(name)
    conf_str = str(confidence)
    
    # results_dict["Results"]{"Name","Confidence"} = label['Name'], 
    # results_dict["Results"]["Confidence"] = label['Confidence']
    
    results_dict['Results'].append({"Name": name_str, "Confidence": conf_str})
    # i_str = str(i)
    # print(i_str + "_" + name_str + ", " +  i_str  + "_" + conf_str) #access age range low & high
    # i = i+1
    
    # new_results = {}                          
    # new_results['Results'] = {}
    # new_results['Results']['Name'] = name
    # new_results['Results']['Confidence'] = confidence
    # results_dict = results_dict + new_results
    # results_dict.update(results)
    # results["Name"].append(label['Name'])
    # results["Confidence"].append(label['Confidence'])
    # results_dict.update(new_results)
    # print(results_dict)
    # print(name_str + ", " + conf_str)
# for key, value in results_dict.items(): 
#     print(key, ': ', value) 

# print("===============")
print(results_dict)






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