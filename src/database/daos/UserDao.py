import bcrypt
import json
from database.models.UserModel import User
from mongoengine.errors import NotUniqueError

class UserDao():
    
    @classmethod
    def get_user_by_id(cls, id):
        user = User.objects.get(id=id)
        user_json = json.loads(user.to_json())
        return user_json
    
    @classmethod
    def register_user(cls, username, email, password, display_name):
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        try:
            user = User(username=username, email=email, password=hashed_pw, display_name=display_name, follows=[], boards=[], comments=[])
            user.save()
            user_json = json.loads(user.to_json())
        except NotUniqueError:
            return {'error': 'a user with that username or email already exists'}, 409
        return user_json