from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# instantiate the app
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1122@localhost/alembic'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://DmitryRbl:N1Hu6FVhmSfM@ep-icy-dust-032217.eu-central-1.aws.neon.tech/neondb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(__name__)

# enable CORS
CORS(app)

db = SQLAlchemy(app)             
migrate = Migrate(app, db)

app.app_context().push()