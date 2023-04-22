from database.daos.UserDao import UserDao

class UserController():

    @classmethod
    def get_user_by_id(cls, id):
        return UserDao.get_user_by_id(id)