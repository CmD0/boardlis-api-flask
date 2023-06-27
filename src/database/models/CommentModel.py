from mongoengine import Document, fields
import datetime

class Comment(Document):
    content = fields.StringField(required=True)
    author = fields.ReferenceField('User')
    board = fields.ReferenceField('Board')
    created_at = fields.DateTimeField(default=datetime.datetime.now)