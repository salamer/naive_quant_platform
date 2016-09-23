from mongoengine import *

connect("quant")

class training_result(Document):
    taskName = StringField(required=True)
    clf_name = StringField(required=True)
    result = ListField()
    error = StringField(default="null")
