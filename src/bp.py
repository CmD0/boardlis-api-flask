from functions.users.get import bp_users_get
from functions.amogus.get import bp_amogus_get

def register_blueprints(app):
    app.register_blueprint(bp_amogus_get, url_prefix='/amogus')

    app.register_blueprint(bp_users_get, url_prefix='/users')