from flask import Blueprint, request

from controllers.UserController import UserController

bp_users_post = Blueprint('users-post', __name__)

@bp_users_post.route('/register', methods=['POST'])
def register_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    display_name = request.json['display_name']
    return UserController.register_user(username, email, password, display_name)

@bp_users_post.route('/login', methods=['POST'])
def login_user():
    username = request.json['username']
    password = request.json['password']
    return UserController.login_user(username, password)

@bp_users_post.route('/<id>', methods=['POST'])
def modify_user(id):
    id = id
    username = request.json['username']
    email = request.json['email']
    display_name = request.json['display_name']
    return UserController.modify_user(id, username, email, display_name)
