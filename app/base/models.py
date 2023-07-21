import mongoengine as me


class User(me.document):
    id = me.ReferenceField()
    username = me.StringField(required=True)
    email = me.EmailField(required=True)
    password = me.StringField(min_length=8)
