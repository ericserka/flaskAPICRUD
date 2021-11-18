from sqlalchemy.orm import class_mapper


def serialize(model, fields=[]):
    # return dict with all fields
    if fields == []:
        columns = [c.key for c in class_mapper(model.__class__).columns]
        return dict((c, getattr(model, c)) for c in columns)
    # return dict with specified fields
    else:
        return dict((f, getattr(model, f)) for f in fields)
