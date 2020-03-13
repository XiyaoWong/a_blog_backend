import datetime

from pymongo import MongoClient
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import abort


client = MongoClient(host="localhost", port=27017)
db = client.blog
User = db.user
Post = db.post
Comment = db.comment


def create_user(username, password=None, is_admin=False):
    if list(User.find({"username": username})):
        abort(400)
    if not password:
        password = 123456
    user = {
        "username": username.replace(" ", ""),
        "password": generate_password_hash(str(password)),
        "nickname": username,
        "avatar": "http://q1.qlogo.cn/g?b=qq&nk=286183317&s=640",
        "is_admin": is_admin
    }
    return retrieve_user(User.insert_one(user).inserted_id)


def retrieve_user(id):
    result = list(User.find({"_id": ObjectId(id)}))
    if not result:
        abort(404)
    info = result[0]
    info["_id"] = str(info["_id"])
    return info


def retrieve_all_user():
    users = list(db.user.find())
    for index in range(len(users)):
        users[index]["_id"] = str(users[index]["_id"])
    return users


def update_user(id, **kwargs):
    result = list(User.find({"_id": ObjectId(id)}))
    if not result:
        abort(404)
    info = result[0]
    new_info = info.copy()
    for k, v in kwargs.items():
        if v:
            new_info[k] = v
    return retrieve_user(id)


def create_post(title: str, body: str = None, category: str = None, tags: list = None):
    if not body:
        body = ""
    if not category:
        category = ""
    if not tags:
        tags = []
    post = {
        "title": title,
        "description": body[0:min(50, len(body))],
        "body": body,
        "pubdate": datetime.datetime.utcnow(),
        "category": category,
        "tags": tags
    }
    return retrieve_post(Post.insert_one(post).inserted_id)


def retrieve_post(id):
    result = list(Post.find({"_id": ObjectId(id)}))
    if not result:
        abort(404)
    data = result[0]
    data["_id"] = str(data["_id"])
    data["pubdate"] = str(data["pubdate"])
    data.pop("description")
    return data


def retrieve_all_post():
    posts = list(Post.find())
    for index in range(len(posts)):
        posts[index]["_id"] = str(posts[index]["_id"])
        posts[index]["pubdate"] = str(posts[index]["pubdate"])
        posts[index].pop("body")
    return posts


def update_post(id, **kwargs):
    result = list(Post.find({"_id": ObjectId(id)}))
    if not result:
        abort(404)
    data = result[0]
    new_data = data.copy()
    for k, v in kwargs.items():
        if v:
            new_data[k] = v
    return retrieve_post(id)


def delete_post(ids):
    if isinstance(ids, list):
        for id in ids:
            Post.delete_one({"_id": ObjectId(id)})
    else:
        id = ids
        Post.delete_one({"_id": ObjectId(id)})
    return True


def create_comment(content, name=None, site=None):
    if not name:
        name = "无名氏"
    if not site:
        site = ""
    comment = {
        "name": name,
        "site": site,
        "content": content,
        "pubdate": datetime.datetime.utcnow(),
    }
    return retrieve_comment(Comment.insert_one(comment).inserted_id)


def retrieve_comment(id):
    result = list(Comment.find({"_id": ObjectId(id)}))
    if not result:
        abort(404)
    data = result[0]
    data["_id"] = str(data["_id"])
    data["pubdate"] = str(data["pubdate"])
    return data


def retrieve_all_comment():
    comments = list(Comment.find())
    for index in range(len(comments)):
        comments[index]["_id"] = str(comments[index]["_id"])
        comments[index]["pubdate"] = str(comments[index]["pubdate"])

    return comments


def delete_comment(ids):
    if isinstance(ids, list):
        for id in ids:
            Comment.delete_one({"_id": ObjectId(id)})
    else:
        id = ids
        Comment.delete_one({"_id": ObjectId(id)})
    return True
