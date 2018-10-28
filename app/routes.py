import commonmark

from flask import render_template, abort, Markup
from app import app, posts

@app.route('/')
@app.route('/index')
@app.route('/index.html')
@app.route('/index.php')
def index():
  return load_md('index')

@app.route('/blog/<name>')
def blog(name):
  return load_md(posts.find_post(name))

@app.route('/post')
def post():
  # TODO: authenticate
  return render_template('post.html')

@app.route('/<filename>.md')
def load_md(filename):
  try:
    file = open(filename + '.md', mode='r', encoding='utf_8')
  except OSError:
    abort(404)
  else:
    text = file.read()
    content = Markup(commonmark.commonmark(text))

    return render_template('md.html', md={'title': filename + '.md', 'html' : content})
