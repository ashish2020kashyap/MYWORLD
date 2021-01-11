
import pika, json,time
from faker import Faker
from timer import timer
fake = Faker()

params = pika.URLParameters('amqps://ntlfismj:hgS4KslLKZA2vSG7nD6V4ke1YXHU2eN0@grouse.rmq.cloudamqp.com/ntlfismj')

connection = pika.BlockingConnection(params)

channel = connection.channel()
method="product_created"

body=  {
        "id": 2,
        "upload_file":"https://miworld2021.s3.amazonaws.com/media/Videos/trailvideo11.mp4"
    }



def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='awslamdaconsuming', body=json.dumps(body), properties=properties)




publish(method,body)

'''


while 1==1:
    body=fake.ipv4_private()
    publish(method,body)
    time.sleep(10)
    
'''
