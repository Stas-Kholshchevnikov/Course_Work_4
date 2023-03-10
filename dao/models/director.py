from marshmallow import Schema, fields

from setup_db import db


class Director(db.Model):
    """
    Модель данных для таблицы directors
    """
    __tablename__ = "directors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


class DirectorSchema(Schema):
    """
    Схема данных для таблицы directors
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()
