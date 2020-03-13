from flask import jsonify
from werkzeug.security import check_password_hash
from flask_restful import Resource
from flask_restful import reqparse
from flask_restful import abort

from app.CRUD import User
from app.auth import generate_token


class Login(Resource):
    def __init__(self):
        self.parse = reqparse.RequestParser()
        self.parse.add_argument("username", type=str, required=True)
        self.parse.add_argument("password", type=str, required=True)
        super().__init__()

    def post(self):
        args = self.parse.parse_args()
        username = args["username"]
        password = args["password"]

        if not username or not password:
            abort(400)
        if not User.find_one({"username": username}):
            abort(400)

        user = User.find_one({"username": username})
        password_hash = user.get("password")
        if check_password_hash(password_hash, password):
            token = generate_token()
            return jsonify({"token": token})
        else:
            return abort(400)
