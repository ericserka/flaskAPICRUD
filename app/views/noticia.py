from app import app
import json
from flask import Response, request
from app.services.noticia import (
    getAllNoticias,
    getNoticiaById,
    postNoticia,
    putNoticia,
    deleteNoticia,
)


@app.get("/noticias")
def getNoticias():
    return Response(json.dumps(getAllNoticias()), mimetype="application/json")


@app.get("/noticia/<id>")
def getNoticia(id):
    return Response(json.dumps(getNoticiaById(id)), mimetype="application/json")


@app.post("/noticias")
def createNoticia():
    body = request.get_json()
    return Response(json.dumps(postNoticia(body)), mimetype="application/json")


@app.put("/noticia/<id>")
def updateNoticia(id):
    body = request.get_json()
    return Response(json.dumps(putNoticia(body, id)), mimetype="application/json")


@app.delete("/noticia/<id>")
def removeNoticia(id):
    return Response(json.dumps(deleteNoticia(id)), mimetype="application/json")
