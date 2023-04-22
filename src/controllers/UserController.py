from database.daos.UserDao import UserDao

class UserController():

    @classmethod
    def get_users(cls):
        return UserDao.get_users()

    @classmethod
    def get_user_by_id(cls, id):
        return UserDao.get_user_by_id(id)

    @classmethod
    def register_user(cls, username, email, password, display_name):
        return UserDao.register_user(username, email, password, display_name)

    @classmethod
    def login_user(cls, username, password):
        return UserDao.login_user(username, password)

    @classmethod
    def modify_user(cls, id, username, email, display_name):
        return UserDao.modify_user(id, username, email, display_name)
