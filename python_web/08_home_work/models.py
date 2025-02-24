from mongoengine import EmbeddedDocument
from mongoengine.fields import (ListField, StringField,
                                DateField, ReferenceField, Document, BooleanField,
                                EmailField)
from db_connect import connect



class Authors(Document):
    fullname = StringField()
    born_date = DateField()
    born_location = StringField()
    description = StringField()

    def __str__(self):
        return self.fullname + " " + str(self.born_date)


class Quotes(Document):
    tags = ListField()
    author = ReferenceField(Authors)
    quote = StringField()

    def __str__(self):
        return self.quote

class Users(Document):
    name = StringField()
    is_send = BooleanField(default=False)
    email = EmailField()

    def __str__(self):
        return self.name
