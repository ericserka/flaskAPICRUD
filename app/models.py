from app import db
from sqlalchemy.ext.automap import automap_base

Base = automap_base()
Base.prepare(db.engine, reflect=True, schema="sihab")
Alert = Base.classes.candidate_cadastre_alerts
Candidate = Base.classes.candidate_cadastres
