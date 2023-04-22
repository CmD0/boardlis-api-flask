from functions.users.get import bp_users_get
from functions.users.post import bp_users_post
from functions.amogus.get import bp_amogus_get

def register_blueprints(app):
    app.register_blueprint(bp_amogus_get, url_prefix='/amogus')

    app.register_blueprint(bp_users_get, url_prefix='/users')
    app.register_blueprint(bp_users_post, url_prefix='/users')