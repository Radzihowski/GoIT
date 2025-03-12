from django.db import models

# Create your models here.
class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Tag(Base):
    name = models.CharField(max_length=25, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"

class Author(Base):
    fullname = models.CharField(max_length=150, null=False)
    born_date = models.DateField()
    born_location = models.CharField(max_length=512, null=False)
    description = models.TextField(max_length=2048, null=False)

    def __str__(self):
        return f"{self.fullname}"

class Quote(Base):
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quote = models.TextField(max_length=4096, null=False)

    def __str__(self):
        return f"{self.pk}"

#
# from mongoengine import EmbeddedDocument
# from mongoengine.fields import (ListField, StringField,
#                                 DateField, ReferenceField, Document, BooleanField,
#                                 EmailField)
# from db_connect import connect
#
#
#
# class Authors(Document):
#     fullname = StringField()
#     born_date = DateField()
#     born_location = StringField()
#     description = StringField()
#
#     def __str__(self):
#         return self.fullname + " " + str(self.born_date)
#
#
# class Quotes(Document):
#     tags = ListField()
#     author = ReferenceField(Authors)
#     quote = StringField()
#
#     def __str__(self):
#         return self.quote
#
# class Users(Document):
#     name = StringField()
#     is_send = BooleanField(default=False)
#     email = EmailField()
#     phone_number = StringField()
#     preferred_method = StringField()
#
#     def __str__(self):
#         return self.name
#
