from flask_restful import Resource
from flask_restful import reqparse

from app.CRUD import \
    retrieve_all_comment, retrieve_comment, create_comment, delete_comment

from app.auth import auth_required

parse = reqparse.RequestParser()
parse.add_argument("name", type=str)
parse.add_argument("site", type=str)
parse.add_argument("content", type=str, required=True)


class Comment(Resource):
    method_decorators = {"delete": [auth_required]}

    def get(self, comment_id):
        return retrieve_comment(comment_id)

    def delete(self, comment_id):
        return delete_comment(comment_id)


class CommentList(Resource):
    method_decorators = {"post": [auth_required]}

    def get(self):
        return retrieve_all_comment()

    def post(self):
        args = parse.parse_args()
        return create_comment(
            content=args["content"],
            name=args["name"],
            site=args["site"]
        )
