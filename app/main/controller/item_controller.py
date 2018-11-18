from flask import request
from flask_restplus import Resource

from ..util.dto import ItemDto
from ..service.item_service import save_new_item, get_all_items, get_a_item,delete_a_item,put_a_item

api = ItemDto.api
_item = ItemDto.item


@api.route('/')
class ItemList(Resource):
    @api.doc('list_of_items')
    @api.marshal_list_with(_item, envelope='data')
    def get(self):
        """List all items """
        return get_all_items()

    @api.response(201, 'Item successfully created.')
    @api.doc('create a new item')
    @api.expect(_item, validate=True)
    def post(self):
        """Creates a new Item """
        data = request.json
        return save_new_item(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Item identifier')
@api.response(404, 'Item not found.')
class Item(Resource):
    @api.doc('get a item')
    @api.marshal_with(_item)
    def get(self, public_id):
        """get a user given its identifier"""
        item = get_a_item(public_id)
        if not item:
            api.abort(404)
        else:
            return item
            
    @api.doc('update a item') 
    @api.expect(_item, validate=True)   
    def put(self,public_id):
        data = request.json
        return put_a_item(data=data)
            
    @api.doc('delete a item')    
    def delete(self, public_id):
        """delete item given its identifier"""
        ret = delete_a_item(public_id)
        return ret