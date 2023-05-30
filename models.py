from datetime import datetime
import connect
from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import  DateTimeField,  ListField, StringField,ReferenceField


class Author(Document):
    fullname = StringField()
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()


class Qoutes(Document):
    tags = ListField()
    authors = ReferenceField(Author)
    quote = StringField()
   