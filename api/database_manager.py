import json

from general_falcon_webserver.backend.general_manager.databases import SqliteDatabase
from datetime import datetime

TIME_FORMAT = '%d/%m/%Y %H:%M:%S'


class DatabaseManager:

    def __init__(self, database: SqliteDatabase):
        self.db = database

    def get_user(self, username: str):
        return json.dumps(self.db.fetchone_query(f"SELECT 1 FROM users WHERE username='{username}'"), ensure_ascii=True)

    def create_user(self, username: str, password_hash: str):
        self.db.send_query(f"INSERT INTO users(username, password_hash, last_access) "
                           f"VALUES '{username}', '{password_hash}', '{datetime.now().strftime(TIME_FORMAT)}'")

    def update_user_access(self, username: str):
        self.db.send_query(f"UPDATE users SET last_access = {datetime.now().strftime(TIME_FORMAT)} "
                           f"WHERE username = {username}")

    def validate_user_expire(self, username: str, expire_time):
        user = self.get_user(username)
        last_access = datetime.strptime(user['last_access'], TIME_FORMAT)
        return last_access + expire_time > datetime.now()
