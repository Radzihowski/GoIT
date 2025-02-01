from datetime import datetime

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField

class Tag(EmbeddedDocument):
    name = StringField()

class Record(EmbeddedDocument):
    description =