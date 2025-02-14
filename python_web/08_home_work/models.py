from mongoengine import EmbeddedDocument
from mongoengine.fields import (ListField, StringField,
                                DateField, ReferenceField, Document)
from db_connect import connect



class Authors(Document):
    fullname = StringField()
    born_date = DateField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    tags = ListField()
    author = ReferenceField(Authors)
    quote = StringField()
