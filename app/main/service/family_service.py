import uuid
import datetime

from app.main import db
from app.main.model.family import Family
from app.main.model.member import Member
from app.main.model.list import List


def get_all_members_for_family(public_id):
    return Member.query.filter_by(family_id=public_id).all()

def save_new_family(data):
    family = Family.query.filter_by(name=data['name']).first()
    if not family:
        public_family_id = str(uuid.uuid4())
        
        new_list = List(
            public_id=str(uuid.uuid4()),
            title=data['name'],
            family_id=public_family_id
        )
        
        new_family = Family(
            public_id=public_family_id,
            name=data['name'],
            default_list_id=new_list.public_id            
        )       
        
    
        save_changes(new_list)
        save_changes(new_family) 
        response_object = {
            'status': 'success',
            'message': 'family created',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Family already exists',
        }
        return response_object, 409


def get_all_families():
    return Family.query.all()
    
def get_families_in_list(list):  
    
    
    family_ids = [element['family_id'] for element in list['data']]
    print(family_ids)
    families = Family.query.filter(Family.public_id.in_(family_ids)).all()
    return families

def get_a_family(public_id):
    return Family.query.filter_by(public_id=public_id).first()

def delete_a_family(public_id):
    ret = Family.query.filter_by(public_id=public_id).delete()
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Family deleted'
    }
    return response_object, 200

def save_changes(data):
    db.session.add(data)
    db.session.commit()
