from sqlalchemy import desc
from app import db
from app.models import Pessoa
from app.utils.serializer import serialize


def getAllPessoas():
    try:
        return [
            serialize(n, ["id", "nome"])
            for n in db.session.query(Pessoa.id, Pessoa.nome)
            .order_by(desc(Pessoa.created_at))
            .all()
        ]
    except Exception as e:
        return {"message": "Erro ao listar pessoas", "exception": str(e)}


def getPessoaById(id):
    try:
        return serialize(
            db.session.query(Pessoa.id, Pessoa.nome).filter_by(id=id).first(),
            ["id", "nome"],
        )
    except Exception as e:
        return {"message": "Pessoa não encontrada!", "exception": str(e)}


def postPessoa(body):
    try:
        db.session.add(Pessoa(nome=body["nome"]))
        db.session.commit()
        return {"message": "Pessoa criada com sucesso!"}
    except Exception as e:
        return {"message": "Erro ao criar pessoa!", "exception": str(e)}


def putPessoa(body, id):
    try:
        pessoa = db.session.query(Pessoa).filter_by(id=id).first()
        if "nome" in body:
            pessoa.nome = body["nome"]
        db.session.add(pessoa)
        db.session.commit()
        return {"message": "Pessoa atualizada com sucesso!"}
    except Exception as e:
        return {"message": "Erro ao atualizar pessoa!", "exception": str(e)}


def deletePessoa(id):
    try:
        pessoa = db.session.query(Pessoa).filter_by(id=id).first()
        db.session.delete(pessoa)
        db.session.commit()
        return {"message": "Pessoa deletada com sucesso!"}
    except Exception as e:
        return {"message": "Erro ao deletar pessoa!", "exception": str(e)}
