from flask import Blueprint, request

from controllers.UserController import UserController

bp_users_patch = Blueprint('users-patch', __name__)

@bp_users_patch.route('/<id>', methods=['PATCH'])
def modify_user(id):
    id = id
    username = request.json['username']
    email = request.json['email']
    display_name = request.json['display_name']
    return UserController.modify_user(id, username, email, display_name)

@bp_users_patch.route('/password', methods=['PATCH'])
def modify_password():
    id = request.json['id']
    password = request.json['password']
    new_password = request.json['new_password']
    return UserController.modify_password(id, password, new_password)