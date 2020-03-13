写完后记：mongo的确简单，但查询起来一点不方便，当然主要是不熟悉，flask_restful和pymongo是现学现用，代码整体写的太乱。本来是打算做blog后台的，还是算了，就当一个练习。目前懒得折腾了

---

### 定义数据库模型(MongoDB)
user就自己一个，post也只有一个所属，另外评论、分类、标签等都是post的一个field
1. User
```json
{
    "_id": "",
    "username": "",
    "password": "",
    "nickname": "",
    "avatar": "",
    "is_admin": true
}
```
2. Post
```json
{
    "_id": "",
    "title": "",
    "description": "",
    "body": "",
    "pubdate": "",
    "category": "",
    "tags": []
}
```
3. Comment(不是评论，是留言)
```json
{
    "_id": "",
    "name": "",
    "site": "",
    "content": "",
    "pubdate": "",
}
```
*评论以后添加，mongodb也足够方便更改数据结构*


### 定义API
#### User相关
有几个方法没必要，但是为了简单实践一下restful api
| HTTP方法 | 资源URL | 说明 | 是否需要权限
| :--- | :--- | :--- | :---:
| `GET` | `/info` | 返回我自己的信息
| `GET` | `/users` | 返回所有用户集合
| `GET` | `/users/<user_id>` | 返回一个用户信息
| `PUT` | `/users/<user_id>` | 修改一个用户信息 | :star:
#### Post相关
暂时因为文章不多，查询的可选参数有关内容以后添加
| HTTP方法 | 资源URL | 说明 | 是否需要权限
| :--- | :--- | :--- | :---:
| `GET` | `/posts` | 返回文章集合
| `POST` | `/posts/` | 新增一篇文章 | :star:
| `GET` | `/posts/<post_id>` | 返回文章详情
| `PUT` | `/posts/<post_id)>` | 修改一篇文章  | :star:
| `DELETE` | `/posts/<post_id>` | 删除一篇文章 | :star:
#### Comment相关
| HTTP方法 | 资源URL | 说明 | 是否需要权限
| :--- | :--- | :--- | :---:
| `GET` | `/comments` | 返回留言集合
| `POST` | `/comments` | 新增留言
| `GET` | `/comments/<comment_id>` | 返回留言详情
| `DELETE` | `/comments/<comment_id>` | 删除留言 | :star: