from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
database_user = os.getenv("DATABASE_USER")
database_password = os.getenv("DATABASE_PASSWORD")
database_host = os.getenv("DATABASE_HOST")
database_name = os.getenv("DATABASE_NAME")
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{database_user}:{database_password}@{database_host}/{database_name}"
db = SQLAlchemy(app)
from app.views import alert_views, candidate_views
