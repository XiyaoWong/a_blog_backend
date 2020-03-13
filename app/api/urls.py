from app.api import api
from app.api.resources.ping import Ping
from app.api.resources.login import Login
from app.api.resources.user import User, UserList
from app.api.resources.post import Post, PostList
from app.api.resources.comment import Comment, CommentList
from app.api.resources.info import Info


api.add_resource(Ping, "/ping/")
api.add_resource(Login, "/login/")
# api.add_resource(UserList, "/users")
api.add_resource(User, "/users/<user_id>/")
api.add_resource(PostList, "/posts/")
api.add_resource(Post, "/posts/<post_id>/")
api.add_resource(CommentList, "/comments/")
api.add_resource(Comment, "/comments/<comment_id>/")
api.add_resource(Info, "/info/")
