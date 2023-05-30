from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import  DateTimeField,  ListField, StringField,ReferenceField, BooleanField

class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    message_sent = BooleanField(default=False)