from sqlalchemy.sql.expression import func

def getAllCandidatesObject(db, Candidate):
    return db.session.query(Candidate).filter(func.length(Candidate.cpf)==11)