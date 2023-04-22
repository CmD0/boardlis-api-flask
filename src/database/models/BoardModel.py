from mongoengine import Document, fields
import datetime

class Board(Document):
    title = fields.StringField(required=True)
    description = fields.StringField(required=True)
    author = fields.ReferenceField('User')
    comments = fields.ListField(fields.ReferenceField('Comment'))
    created_at = fields.DateTimeField(default=datetime.datetime.now)