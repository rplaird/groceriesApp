import uuid
import datetime

from app.main import db
from app.main.model.list import List

def save_new_list(data):
    list = List.query.filter_by(title=data['title']).first()
    if not list:
        new_list = List(
            public_id=str(uuid.uuid4()),
            title=data['title'],
            family_id=data['family_id']
        )
        save_changes(new_list)
        response_object = {
            'status': 'success',
            'message': 'list created',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'list already exists',
        }
        return response_object, 409


def get_all_lists():
    return List.query.all()

def get_a_list_for_family(family_id):
    return List.query.filter_by(family_id=family_id).first()

def get_a_list(public_id):
    return List.query.filter_by(public_id=public_id).first()

def delete_a_list(public_id):
    ret = List.query.filter_by(public_id=public_id).delete()
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'List deleted'
    }
    return response_object, 200

def save_changes(data):
    db.session.add(data)
    db.session.commit()
