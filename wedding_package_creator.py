from general_falcon_webserver import WebApp, SqliteDatabase

app = WebApp('frontend')
db = SqliteDatabase('wedding_package_database')
app.launch_webserver()
