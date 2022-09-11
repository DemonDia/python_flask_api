from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app = Flask(__name__)
# configuring marshmellow
ma = Marshmallow(app)

# wrap app in the API
# =================configuring SQLAlchemy=================
# the destination of the data source
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

# Import each model so that they are created in order
# NOTE: Create those that do not have foreign keys first
from Models.User import User
from Models.Video import Video
db.create_all()
