from database.daos.UserDao import UserDao

class UserController():

    @classmethod
    def get_user_by_id(cls, id):
        return UserDao.get_user_by_id(id)
    
    @classmethod
    def register_user(cls, username, email, password, display_name):
        return UserDao.register_user(username, email, password, display_name)