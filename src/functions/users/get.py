from flask import Blueprint, request

from controllers.UserController import UserController

bp_users_get = Blueprint('users-get', __name__)


@bp_users_get.route('', methods=['GET'])
def search():
    query = request.args.get('query')
    field = request.args.get('field')
    if query and field:
        return UserController.search(query, field)
    else:
        return UserController.get_users()

@bp_users_get.route('/<id>', methods=['GET'])
def get_user_by_id(id):
    return UserController.get_user_by_id(id)
