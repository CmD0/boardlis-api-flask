class UserDao():

    @classmethod
    def get_user_by_id(cls, id):
        return {'id': id}