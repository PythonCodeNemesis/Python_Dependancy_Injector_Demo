class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository
    def get_user(self, user_id):
        return self.user_repository.get_user(user_id)