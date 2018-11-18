from .. import db, flask_bcrypt
import datetime
import jwt
from ..config import key


class Item(db.Model):
    
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    list_id = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.String(255), nullable=False)    
    status = db.Column(db.String(255), nullable=False)
        

    def __repr__(self):
        return "<Item '{}'>".format(self.desc)