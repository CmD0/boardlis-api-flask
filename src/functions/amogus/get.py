from flask import Blueprint, Flask


bp_amogus_get = Blueprint('amogus-get', __name__)


@bp_amogus_get.route('', methods=['GET'])
def get_deez_nuts():
    return 'deez nuts lol'
