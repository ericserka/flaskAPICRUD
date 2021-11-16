from app import app
from sqlalchemy import desc
import json
from flask import Response, request
from app.serializer import serialize
from app.models import db, Alert
from datetime import datetime

@app.get("/alertas")
def getAllAlerts():
    results = db.session.query(Alert).order_by(desc(Alert.id)).all()
    retorno=[serialize(r) for r in results]
    return Response(json.dumps(retorno, indent=4, sort_keys=True, default=str),mimetype='application/json')

@app.get("/alerta/<id>")
def getAlertById(id):
    try:
        result = db.session.query(Alert).filter_by(id=id).first()
        retorno = serialize(result)
        return Response(json.dumps(retorno, indent=4, sort_keys=True, default=str),mimetype='application/json')
    except:
        return Response(json.dumps({"message": "Alerta não encontrado!"}),mimetype='application/json')

@app.post("/alerta")
def createAlert():
    body = request.get_json()
    alert = Alert(cadastre_id = body['cadastre_id'], description = body['description'], alert_type_id = 1)
    db.session.add(alert)
    db.session.commit()
    return Response(json.dumps({"message": "Criado com sucesso!"}),mimetype='application/json')

@app.put("/alerta/<id>")
def updateAlert(id):
    body = request.get_json()
    try:
        alert = db.session.query(Alert).filter_by(id=id).first()
        if ('cadastre_id' in body):
            alert.cadastre_id = body['cadastre_id']
        if ('date' in body):
            alert.date = body['date']
        if ('description' in body):
            alert.description = body['description']
        if ('alert_type_id' in body):
            alert.alert_type_id = body['alert_type_id']
        alert.updated_at = datetime.now()

        db.session.add(alert)
        db.session.commit()
        return Response(json.dumps({"message": "Atualizado com sucesso!"}),mimetype='application/json')
    except:
        return Response(json.dumps({"message": "Erro ao atualizar!"}),mimetype='application/json')

@app.delete("/alerta/<id>")
def deleteAlert(id):
    try:
        alert = db.session.query(Alert).filter_by(id=id).first()
        db.session.delete(alert)
        db.session.commit()
        return Response(json.dumps({"message": "Deletado com sucesso!"}),mimetype='application/json')
    except:
        return Response(json.dumps({"message": "Erro ao deletar!"}),mimetype='application/json')