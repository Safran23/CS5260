import boto3
s3 = boto3.resource('s3')

my_bucket = s3.Bucket('usu-cs5250-water2-requests')

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)
    
    
s3 = boto3.client('s3')

s3.download_file('usu-cs5250-water2-requests', '1695786989229', '1695786989229.json')

d={}
import json
f=open('1695786989229.json')
#return JSON as a dictionary

data = json.load(f)
data


d['widgetId'] = data['widgetId']
d['owner'] = data['owner']
d['label'] = data ['label']
d['description'] = data['description']

d
print(d)


json1 = json.dumps(data)

print(json1)

#Saving it to Bucket 3

bucket_name = 'usu-cs5250-water3-web'
client = boto3.client('s3')

s3.upload_file('1695786989229.json', 'usu-cs5250-water3-web', 'json1')

