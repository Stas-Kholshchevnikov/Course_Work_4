from marshmallow import Schema, fields

from setup_db import db


class Genre(db.Model):
    """
    Модель данных для таблицы genres
    """
    __tablename__ = "genres"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


class GenreSchema(Schema):
    """
    Схема данных для таблицы genres
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()
