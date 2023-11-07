import boto3

sqs = boto3.client('sqs', region_name='us-east-1')

queue_url = 'https://sqs.us-east-1.amazonaws.com/835778894128/cs5260-requests'

#Sending message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    )
print(response['MessageId'])

import boto3
s3 = boto3.resource('s3')


my_bucket = s3.Bucket('usu-cs5250-water2-requests')

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)
    
    
s3 = boto3.client('s3')

s3.download_file('usu-cs5250-water2-requests', '1695786989229', '1695786989229.json')


s3.download_file('usu-cs5250-water2-requests', '1695786990271', '1695786990271.json')
d={}
import json
f=open('1695786989229.json')

f1=open('1695786990271.json')
#return JSON as a dictionary

data = json.load(f)
data


d['widgetId'] = data['widgetId']
d['owner'] = data['owner']
d['label'] = data ['label']
d['description'] = data['description']

d


json1 = json.dumps(data)

print(json1)

#Saving it to Bucket 3

bucket_name = 'usu-cs5250-water3-web'
s3.upload_file('1695786989229.json', sqs, 'json1')

#Deleting widget request
s3 = boto3.client('s3')
s3.delete_object(Bucket="usu-cs5250-water3-web", key='json1')

#Updating widget request in S3
updated_data= '1695786990271.json'

    # Read the existing Widget Request from S3
        response = s3.get_object(usu-cs5250-water3-web, 'json1')
        existing_data = json1
        existing_widget_request = json.loads(existing_data)
    

    # Update the Widget Request with new data
    existing_widget_request.update(updated_data)

    # Write the updated Widget Request back to S3
        updated_data = json.dumps(existing_widget_request)
        s3.put_object(usu-cs5250-water3-web, Key=json1, Body=updated_data)