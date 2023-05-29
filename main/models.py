from django.db.models import *


# Create your models here.


class QnA(Model):
    question = CharField(max_length=200, null=True)
    answer = TextField(null=True)
