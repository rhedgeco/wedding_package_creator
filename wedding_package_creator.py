from general_falcon_webserver import WebApp, SqliteDatabase
from api.database_manager import DatabaseManager
from api.authenticator import Auth
from api.users import Users

app = WebApp('frontend', 'page_not_found.html')
db = SqliteDatabase('wedding_package_database')

manager = DatabaseManager(db)

# Add all api locations
users = Users(manager)
app.add_route('users', users)

app.launch_webserver()
