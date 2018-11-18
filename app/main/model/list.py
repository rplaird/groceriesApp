from .. import db, flask_bcrypt
import datetime
import jwt
from ..config import key


class List(db.Model):
    
    __tablename__ = "list"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    public_id = db.Column(db.String(100), unique=True)
    family_id = db.Column(db.String(100))


    
    def __repr__(self):
        return "<Family '{}'>".format(self.title)