from sqlalchemy import desc


def getAllAlertsObject(db, Alert):
    return db.session.query(Alert).order_by(desc(Alert.id)).all()
