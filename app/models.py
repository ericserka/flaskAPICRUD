from datetime import datetime
from app import db
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import event

Base = automap_base()
# se as tabelas estiverem num schema diferente de public, ele deve ser especificado (no exemplo abaixo foi o schema sihab)
# Base.prepare(db.engine, reflect=True, schema="sihab")
Base.prepare(db.engine, reflect=True)
Noticia = Base.classes.noticia
Pessoa = Base.classes.pessoa


def before_update(mapper, conenction, target):
    target.updated_at = datetime.now()


for cls in [Noticia, Pessoa]:
    event.listen(cls, "before_update", before_update)
