
import connect

import pika
import json
from contact_model import Contact

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost', port=5672, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

def send_email(contact_id):
    contact = Contact.objects.get(id=contact_id)
    print(f"Відправка повідомлення на електронну пошту: {contact.email}")
    contact.update(message_sent = True)
    contact.save()
   

def callback(ch, method, properties, body):
    contact_id = body.decode()
    send_email(contact_id)
   

channel.basic_consume(queue='email_queue', on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
