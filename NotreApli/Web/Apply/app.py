from flask import Flask
from flask_script import Manager
import os.path
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.debug = True
Bootstrap(app)

manager = Manager(app)

app.debug = True

app.config['BOOTSTRAP_SERVE_LOCAL'] = True


app.config['BOOTSTRAP_SERVE_LOCAL'] = True
from flask_bootstrap import Bootstrap
Bootstrap(app)

import os.path
def mkpath(p):
    return os.path.normpath(
        os.path.join(
            os.path.dirname(__file__),
            p))


from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI']=(
    'sqlite:///'+mkpath('../tuto.db'))
db=SQLAlchemy(app)
