from .. import db, flask_bcrypt
import datetime
import jwt
from ..config import key

class Member(db.Model):
    
    __tablename__ = "member"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(100),nullable=False)
    family_id = db.Column(db.String(100),nullable=False)
    public_id = db.Column(db.String(100), unique=True)
    
    def __repr__(self):
        return "<Member '{}'>".format(self.public_id)