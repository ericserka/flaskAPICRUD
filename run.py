# from datetime import datetime
# from flask import Flask, Response, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
# from sqlalchemy.ext.automap import automap_base
# import json
# from sqlalchemy.orm import class_mapper
# from sqlalchemy import desc
# from dotenv import load_dotenv
# import os
# from string import Template

from app import app

if __name__ == '__main__':
    app.run()

# load_dotenv()

# #Transforms a model into a dictionary which can be dumped to JSON.
# def serialize(model):
#     # first we get the names of all the columns on your model
#     columns = [c.key for c in class_mapper(model.__class__).columns]
#     # then we return their values in a dict
#     return dict((c, getattr(model, c)) for c in columns)

# app = Flask(__name__)
# CORS(app)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
# app.config['SQLALCHEMY_DATABASE_URI']= Template('postgresql://$user:$password@$host/$name').substitute(user = os.getenv('DATABASE_USER'), password = os.getenv('DATABASE_PASSWORD'), host = os.getenv('DATABASE_HOST'), name = os.getenv('DATABASE_NAME'))
# db=SQLAlchemy(app)
# Base = automap_base()
# Base.prepare(db.engine,reflect=True,schema='sihab')
# Alert = Base.classes.candidate_cadastre_alerts

# @app.get("/alertas")
# def getAllAlerts():
#     results = db.session.query(Alert).filter_by(alert_type_id=1).order_by(desc(Alert.id))
#     retorno=[serialize(r) for r in results]
#     return Response(json.dumps(retorno, indent=4, sort_keys=True, default=str),mimetype='application/json')

# @app.get("/alerta/<id>")
# def getAlertById(id):
#     try:
#         result = db.session.query(Alert).filter_by(id=id).first()
#         retorno = serialize(result)
#         return Response(json.dumps(retorno, indent=4, sort_keys=True, default=str),mimetype='application/json')
#     except:
#         return Response(json.dumps({"message": "Alerta não encontrado!"}),mimetype='application/json')

# @app.post("/alerta")
# def createAlert():
#     body = request.get_json()
#     alert = Alert(cadastre_id = body['cadastre_id'], description = body['description'], alert_type_id = 1)
#     db.session.add(alert)
#     db.session.commit()
#     return Response(json.dumps({"message": "Criado com sucesso!"}),mimetype='application/json')

# @app.put("/alerta/<id>")
# def updateAlert(id):
#     body = request.get_json()
#     try:
#         alert = db.session.query(Alert).filter_by(id=id).first()
#         if ('cadastre_id' in body):
#             alert.cadastre_id = body['cadastre_id']
#         if ('date' in body):
#             alert.date = body['date']
#         if ('description' in body):
#             alert.description = body['description']
#         if ('alert_type_id' in body):
#             alert.alert_type_id = body['alert_type_id']
#         alert.updated_at = datetime.now()

#         db.session.add(alert)
#         db.session.commit()
#         return Response(json.dumps({"message": "Atualizado com sucesso!"}),mimetype='application/json')
#     except:
#         return Response(json.dumps({"message": "Erro ao atualizar!"}),mimetype='application/json')

# @app.delete("/alerta/<id>")
# def deleteAlert(id):
#     try:
#         alert = db.session.query(Alert).filter_by(id=id).first()
#         db.session.delete(alert)
#         db.session.commit()
#         return Response(json.dumps({"message": "Deletado com sucesso!"}),mimetype='application/json')
#     except:
#         return Response(json.dumps({"message": "Erro ao deletar!"}),mimetype='application/json')
