from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config  as cfg


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://%s:%s@%s/%s" % (cfg.MYSQL_LOGINNAME, cfg.MYSQL_PASSWORD, cfg.MYSQL_HOST, cfg.DATABASE)

db = SQLAlchemy(app)

from api import view
from api import decorator