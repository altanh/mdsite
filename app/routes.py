import commonmark

from flask import render_template, abort, Markup
from app import app, posts

@app.route('/')
@app.route('/index')
@app.route('/index.html')
@app.route('/index.php')
def index():
  return render_md('index')

@app.route('/blog')
@app.route('/blog/')
def blog():
  ps = list(map(lambda p: {'name': p['name'],
                           'file': p['file'],
                           'html': load_md(p['file'])}, posts.get_posts()))
  return render_template('blog.html', posts=ps)

@app.route('/blog/<name>')
def blog_post(name):
  return render_md(posts.find_post(name))

@app.route('/post')
def post():
  # TODO: authenticate
  return render_template('post.html')

def load_md(filename):
  try:
    file = open(filename + '.md', mode='r', encoding='utf_8')
  except OSError:
    abort(404)
  else:
    text = file.read()
    content = Markup(commonmark.commonmark(text))

    return content

@app.route('/<filename>.md')
def render_md(filename):
  content = load_md(filename)

  return render_template('md.html', md={'title': filename + '.md', 'html' : content})
