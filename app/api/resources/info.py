from flask_restful import Resource

from app.CRUD import User, retrieve_user


class Info(Resource):

    def get(self):
        me = User.find_one({"username": "wongxy"})
        return retrieve_user(me["_id"])