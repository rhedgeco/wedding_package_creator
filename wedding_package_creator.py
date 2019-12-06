from pathlib import Path
from general_falcon_webserver import WebApp, SqliteDatabase

app = WebApp('frontend', 'page_not_found.html')
db = SqliteDatabase('wedding_package_database')
app.launch_webserver()
