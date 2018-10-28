from tinydb import TinyDB, Query
from flask import abort

def find_post(post_name):
  db = TinyDB('blog/posts.json')
  Posts = Query()
  post = db.get(Posts.name == post_name)
  db.close()

  if post is None:
    abort(404)
  else:
    return 'blog/' + post['file']