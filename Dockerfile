FROM python:3.7

COPY consumer.py

# Specify the command to run your Python program
CMD [ "python", "consumer.py", "us-east-1", "https://sqs.us-east-1.amazonaws.com/835778894128/cs5260-requests", "widgets"]