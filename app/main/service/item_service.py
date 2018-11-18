import uuid
import datetime

from app.main import db
from app.main.model.item import Item
from sqlalchemy import and_

def put_a_item(data):   
    
    item =  Item.query.filter_by(public_id=data['public_id']).first()

    item.status = data['status'] 
    save_changes(item) 
    response_object = {
        'status': 'success',
        'message': 'item updated',
    }      
    return response_object, 200
    
def save_new_item(data):    
    item = Item.query.filter(and_(Item.desc==data['desc'],Item.list_id==data['list_id'])).first()

    if not item:
        new_item= Item(
            public_id=str(uuid.uuid4()),
            list_id=data['list_id'],
            desc=data['desc'],
            status=data['status']
        
        )
        save_changes(new_item)
        response_object = {
            'status': 'success',
            'message': 'item created',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Item already exists',
        }
        return response_object, 409


def get_all_items():
    return Item.query.all()
    
def get_all_items_for_list(list):
    list_id = list['data']['public_id']    
    return Item.query.filter_by(list_id=list_id).all()

def get_a_item(public_id):
    return Item.query.filter_by(public_id=public_id).first()

def delete_a_item(public_id):
    ret = Item.query.filter_by(public_id=public_id).delete()
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Item deleted'
    }
    return response_object, 200

def save_changes(data):
    db.session.add(data)
    db.session.commit()
