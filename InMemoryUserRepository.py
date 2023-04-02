from UserRepository import UserRepository
from UserService import UserService

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {
            1: {"id": 1, "name": "Alice"},
            2: {"id": 2, "name": "Bob"},
            3: {"id": 3, "name": "Charlie"},
        }

    def get_user(self, user_id):
        return self.users.get(user_id, None)

if __name__ == "__main__":
    user_repository = InMemoryUserRepository()
    user_service = UserService(user_repository)
    user = user_service.get_user(1)
    print(user.get("name"))
