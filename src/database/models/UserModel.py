from mongoengine import Document, fields
import datetime

class User(Document):
    username = fields.StringField(required=True, unique=True)
    email = fields.EmailField(required=True, unique=True)
    password = fields.StringField(required=True, min_length=6)
    display_name = fields.StringField(required=True)
    follows = fields.ListField(fields.ReferenceField('User'))
    boards = fields.ListField(fields.ReferenceField('Board'))
    comments = fields.ListField(fields.ReferenceField('Comment'))
    created_at = fields.DateTimeField(default=datetime.datetime.now)