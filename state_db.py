import mongoengine

mongoengine.connect('training_state')


class State(mongoengine.Document):
    name = mongoengine.StringField()
    path = mongoengine.StringField()
    state = mongoengine.StringField()
    clfPath = mongoengine.StringField()
