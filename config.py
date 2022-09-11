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
