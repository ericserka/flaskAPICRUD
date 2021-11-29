from sqlalchemy import desc
from app import db
from app.models import Noticia
from app.utils.serializer import serialize


def getAllNoticias():
    try:
        return [
            serialize(n, ["id", "link"])
            for n in db.session.query(Noticia.id, Noticia.link)
            .order_by(desc(Noticia.created_at))
            .all()
        ]
    except Exception as e:
        return {"message": "Erro ao listar notícias", "exception": str(e)}


def getNoticiaById(id):
    try:
        return serialize(
            db.session.query(Noticia.id, Noticia.link).filter_by(id=id).first(),
            ["id", "link"],
        )
    except Exception as e:
        return {"message": "Notícia não encontrada!", "exception": str(e)}


def postNoticia(body):
    try:
        db.session.add(Noticia(link=body["link"]))
        db.session.commit()
        return {"message": "Notícia criada com sucesso!"}
    except Exception as e:
        return {"message": "Erro ao criar notícia!", "exception": str(e)}


def putNoticia(body, id):
    try:
        noticia = db.session.query(Noticia).filter_by(id=id).first()
        if "link" in body:
            noticia.link = body["link"]
        db.session.add(noticia)
        db.session.commit()
        return {"message": "Notícia atualizada com sucesso!"}
    except Exception as e:
        return {"message": "Erro ao atualizar notícia!", "exception": str(e)}


def deleteNoticia(id):
    try:
        noticia = db.session.query(Noticia).filter_by(id=id).first()
        db.session.delete(noticia)
        db.session.commit()
        return {"message": "Notícia deletada com sucesso!"}
    except Exception as e:
        return {"message": "Erro ao deletar notícia!", "exception": str(e)}
