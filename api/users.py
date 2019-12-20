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
        if not validate_params(req.params, 'first_name', 'last_name', 'email', 'username', 'password'):
            resp.status = falcon.HTTP_BAD_REQUEST
            resp.body = 'Bad parameters.'
            return

        username = req.params['username']
        if self.db.get_user(username) != 'null':
            resp.status = falcon.HTTP_CONFLICT
            resp.body = 'Username already exists.'
            return

        first_name = req.params['first_name']
        last_name = req.params['last_name']
        email = req.params['email']
        password = hash_password(req.params['password'])
        self.db.create_user(first_name, last_name, email, username, password)
