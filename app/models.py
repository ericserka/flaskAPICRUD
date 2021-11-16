from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

db=SQLAlchemy(app)
Base = automap_base()
Base.prepare(db.engine,reflect=True,schema='sihab')
Alert = Base.classes.candidate_cadastre_alerts
Candidate = Base.classes.candidate_cadastres