from general_falcon_webserver import WebApp, SqliteDatabase
from api.database_manager import DatabaseManager
from api.authenticator import Auth
from api.users import Users
from pathlib import Path

app = WebApp('frontend', 'page_not_found.html')

with open(Path('api') / 'database_config.sql') as file:
    db_config = file.read()
db = SqliteDatabase('wedding_package_database', db_config)

# Add all api locations
users = Users(db)
app.add_route('users', users)

auth = Auth(db)
app.add_route('auth', auth)

app.launch_webserver()
