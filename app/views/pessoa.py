from app import app
import json
from flask import Response, request
from app.services.pessoa import (
    getAllPessoas,
    getPessoaById,
    postPessoa,
    putPessoa,
    deletePessoa,
)


@app.get("/pessoas")
def getPessoas():
    return Response(json.dumps(getAllPessoas()), mimetype="application/json")


@app.get("/pessoa/<id>")
def getPessoa(id):
    return Response(json.dumps(getPessoaById(id)), mimetype="application/json")


@app.post("/pessoas")
def createPessoa():
    body = request.get_json()
    return Response(json.dumps(postPessoa(body)), mimetype="application/json")


@app.put("/pessoa/<id>")
def updatePessoa(id):
    body = request.get_json()
    return Response(json.dumps(putPessoa(body, id)), mimetype="application/json")


@app.delete("/pessoa/<id>")
def removePessoa(id):
    return Response(json.dumps(deletePessoa(id)), mimetype="application/json")
