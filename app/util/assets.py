from flask_assets import Bundle, Environment
from .. import app

bundles = {
  'base_css': Bundle(
      'css/lib/spectre.min.css',
      'css/base.css',
      output='gen/base.css')
}

assets = Environment(app)
assets.register(bundles)