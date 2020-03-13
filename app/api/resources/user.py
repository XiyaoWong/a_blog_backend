from flask_restful import Resource, reqparse

from app.CRUD import \
    retrieve_user, update_user, retrieve_all_user
from app.auth import auth_required

parse = reqparse.RequestParser()
parse.add_argument("password", type=str)
parse.add_argument("nickname", type=str)
parse.add_argument("avatar", type=str)


class User(Resource):
    method_decorators = {
        "put": [auth_required],
    }

    def get(self, user_id):
        return retrieve_user(user_id)

    def put(self, user_id):
        args = parse.parse_args()
        return update_user(
            user_id,
            username=args["username"],
            password=args["password"],
            avatar=args["avatar"]
        )


class UserList(Resource):

    def get(self):
        return retrieve_all_user()