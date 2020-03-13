from flask_restful import Resource
from flask_restful import reqparse

from app.CRUD import \
    create_post, retrieve_post, retrieve_all_post, update_post, delete_post
from app.auth import auth_required


parse = reqparse.RequestParser()
parse.add_argument("title", type=str, required=True)
parse.add_argument("body", type=str)
parse.add_argument("category", type=str)
parse.add_argument("tags", type=list)


class Post(Resource):
    method_decorators = {
        "delete": [auth_required],
        "put": [auth_required],
    }

    def get(self, post_id):
        return retrieve_post(post_id)

    def put(self, post_id):
        args = parse.parse_args()
        return update_post(
            post_id,
            title=args["title"],
            body=args["body"],
            category=args["category"],
            tags=args["tags"]
        )

    def delete(self, post_id):
        return delete_post(post_id)


class PostList(Resource):
    method_decorators = {
        "post": [auth_required],
    }

    def get(self):
        return retrieve_all_post()

    def post(self):
        args = parse.parse_args()
        return create_post(
            title=args["title"],
            body=args["body"],
            category=args["category"],
            tags=args["tags"]
        )
