import falcon

from api.database_manager import DatabaseManager
from api.authenticator import hash_password, validate_token_expire, TokenValidationType
from api.api_utils import validate_params


class Users:

    def __init__(self, manager: DatabaseManager):
        self.db = manager

    def on_get(self, req, resp):
        if not validate_params(req.params, 'authToken'):
            resp.status = falcon.HTTP_BAD_REQUEST
            resp.body = 'Bad parameters.'
            return

        token = req.params['authToken']
        user = validate_token_expire(self.db, token)

        if user == TokenValidationType.BAD_TOKEN:
            resp.status = falcon.HTTP_UNAUTHORIZED
            resp.body = 'Bad Token.'
            return

        if user == TokenValidationType.EXPIRED:
            resp.status = falcon.HTTP_UNAUTHORIZED
            resp.body = 'Login expired.'
            return

        resp.status = falcon.HTTP_OK
        resp.body = user

    def on_post(self, req, resp):
        if not validate_params(req.params, 'username', 'password'):
            resp.status = falcon.HTTP_BAD_REQUEST
            resp.body = "Bad parameters."
            return

        username = req.params['username']
        if self.db.get_user(username):
            resp.status = falcon.HTTP_CONFLICT
            resp.body = "Username already exists."
            return

        password = hash_password(req.params['password'])
        self.db.create_user(username, password)
