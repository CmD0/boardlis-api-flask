from typing import Tuple
import bcrypt
import json
from database.models.UserModel import User
from mongoengine.errors import NotUniqueError

class UserDao():
    
    @classmethod
    def get_users(cls):
        users = [user for user in User.objects]
        users = list(map(lambda user: json.loads(user.to_json()), users))
        return users, 200
    
    @classmethod
    def get_user_by_id(cls, id):
        user = User.objects.get(id=id)
        user_json = json.loads(user.to_json())
        return user_json, 200
    
    @classmethod
    def register_user(cls, username, email, password, display_name):
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        try:
            user = User(username=username, email=email, password=hashed_pw, display_name=display_name, follows=[], boards=[], comments=[])
            user.save()
            user_json = json.loads(user.to_json())
        except NotUniqueError:
            return {'error': 'a user with that username or email already exists'}, 409
        return user_json, 201

    @classmethod
    def login_user(cls, username, password):
        user = User.objects.get(username=username)
        if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            user_json = json.loads(user.to_json())
            return user_json, 200
        else:
            return {'error': 'incorrect password'}, 401

    @classmethod
    def modify_user(cls, id, username, email, display_name):
        user = User.objects.get(id=id)
        try:
            user.username = username
            user.email = email
            user.display_name = display_name
            user.save()
            user_json = json.loads(user.to_json())
            return user_json, 200
        except NotUniqueError:
            return {'error': 'that username or email is taken'}, 409
