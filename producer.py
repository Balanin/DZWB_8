from faker import Faker
import connect
from mongoengine import Document, StringField, BooleanField
import pika
import json
from contact_model import Contact

fake = Faker()

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost', port=5672, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

num_contacts = 3


for i in range(num_contacts):
    contact = Contact(
        full_name=fake.name(),
        email=fake.email(),
        message_sent = False
    )
    contact.save()



for contact in Contact.objects:
    message = str(contact.id)

    channel.basic_publish(exchange='', routing_key='email_queue', body=message)
connection.close()