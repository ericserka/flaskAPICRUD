from flask import Flask
from flask_cors import CORS
from string import Template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_DATABASE_URI']= Template('postgresql://$user:$password@$host/$name').substitute(user = os.getenv('DATABASE_USER'), password = os.getenv('DATABASE_PASSWORD'), host = os.getenv('DATABASE_HOST'), name = os.getenv('DATABASE_NAME'))
from app import alert_views
from app import candidate_views