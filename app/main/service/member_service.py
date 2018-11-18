import uuid
import datetime

from app.main import db
from app.main.model.member import Member
from sqlalchemy import and_

def save_new_member(data):
    member = Member.query.filter(and_(Member.user_id==data['user_id'],Member.family_id==data['family_id'])).first()
    
    if not member:
        new_member = Member(
            public_id=str(uuid.uuid4()),
            user_id=data['user_id'],
            family_id=data['family_id'],
        )
        save_changes(new_member)
        response_object = {
            'status': 'success',
            'message': 'member created',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'member already exists',
        }
        return response_object, 409


def get_all_members():
    return Member.query.all()
    
def get_all_members_for_user(user_id):
    return Member.query.filter_by(user_id=user_id).all()

def get_a_member(public_id):
    return Member.query.filter_by(public_id=public_id).first()

def delete_a_member(public_id):
    ret = Member.query.filter_by(public_id=public_id).delete()
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Member deleted'
    }
    return response_object, 200
    
def save_changes(data):
    db.session.add(data)
    db.session.commit()
