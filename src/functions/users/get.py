from flask import Blueprint

from controllers.UserController import UserController

bp_users_get = Blueprint('users-get', __name__)

@bp_users_get.route('/<id>', methods=['GET'])
def get_user_by_id(id):
    return UserController.get_user_by_id(id)
