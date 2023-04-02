import os
import sqlite3
from UserRepository import UserRepository
from UserService import UserService

class DatabaseUserRepository(UserRepository):
    def __init__(self, db_path):
        self.db_path = db_path

    def get_user(self, user_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name FROM users WHERE id=?", (user_id,))
            row = cursor.fetchone()
            if row is None:
                return None
            return {"id": row[0], "name": row[1]}

if __name__ == "__main__":
    # Swap out the InMemoryUserRepository with a DatabaseUserRepository
    db_dir = "test"
    os.makedirs(db_dir, exist_ok=True)
    db_path = os.path.join(db_dir, "test.db")
    
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
        cursor.execute('INSERT INTO users (id, name) VALUES (1, "Alice")')
        cursor.execute('INSERT INTO users (id, name) VALUES (2, "Bob")')
        cursor.execute('INSERT INTO users (id, name) VALUES (3, "Charlie")')
    
    user_repository = DatabaseUserRepository(db_path)
    user_service = UserService(user_repository)
    user = user_service.get_user(1)
    print(user["name"])
