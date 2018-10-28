import commonmark

from flask import render_template, abort, Markup
from app import app

@app.route('/')
@app.route('/index')
def index():
  return "hello world"

@app.route('/<filename>.md')
def load_md(filename):
  try:
    file = open(filename + '.md', mode='r', encoding='utf_8')
  except OSError:
    abort(404)
  else:
    text = file.read()
    content = Markup(commonmark.commonmark(text))

    return render_template('base.html', title=filename, md={'html' : content})