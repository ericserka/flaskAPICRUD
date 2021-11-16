from app import app
from sqlalchemy import desc
from sqlalchemy.sql.expression import func
import json
from flask import Response, request
from app.serializer import serialize
from app.models import db, Candidate
from datetime import datetime

@app.get("/candidatos")
def getAllCandidates():
    results = db.session.query(Candidate).filter(func.length(Candidate.cpf)==11)
    retorno=[serialize(r) for r in results]
    return Response(json.dumps(retorno, indent=4, sort_keys=True, default=str),mimetype='application/json')

@app.get("/candidato/<id>")
def getCandidateById(id):
    try:
        result = db.session.query(Candidate).filter_by(id=id).first()
        retorno = serialize(result)
        return Response(json.dumps(retorno, indent=4, sort_keys=True, default=str),mimetype='application/json')
    except:
        return Response(json.dumps({"message": "Candidato não encontrado!"}),mimetype='application/json')

@app.post("/candidato")
def createCandidate():
    body = request.get_json()
    candidate = Candidate(cpf = body['cpf'])
    db.session.add(candidate)
    db.session.commit()
    return Response(json.dumps({"message": "Criado com sucesso!"}),mimetype='application/json')

@app.put("/candidato/<id>")
def updateCandidate(id):
    body = request.get_json()
    try:
        candidate = db.session.query(Candidate).filter_by(id=id).first()
        if ('cpf' in body):
            candidate.cpf = body['cpf']
        candidate.updated_at = datetime.now()

        db.session.add(candidate)
        db.session.commit()
        return Response(json.dumps({"message": "Atualizado com sucesso!"}),mimetype='application/json')
    except:
        return Response(json.dumps({"message": "Erro ao atualizar!"}),mimetype='application/json')

@app.delete("/candidato/<id>")
def deleteCandidate(id):
    try:
        candidate = db.session.query(Candidate).filter_by(id=id).first()
        db.session.delete(candidate)
        db.session.commit()
        return Response(json.dumps({"message": "Deletado com sucesso!"}),mimetype='application/json')
    except:
        return Response(json.dumps({"message": "Erro ao deletar!"}),mimetype='application/json')