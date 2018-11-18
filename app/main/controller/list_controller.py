from flask import request
from flask_restplus import Resource

from ..util.dto import ListDto
from ..service.list_service import save_new_list, get_all_lists, get_a_list,delete_a_list

api = ListDto.api
_list = ListDto.list


@api.route('/')
class ListList(Resource):
    @api.doc('list_of_lists')
    @api.marshal_list_with(_list, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_lists()

    @api.response(201, 'List successfully created.')
    @api.doc('create a new list')
    @api.expect(_list, validate=True)
    def post(self):
        """Creates a new Family """
        data = request.json
        return save_new_list(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The List identifier')
@api.response(404, 'list not found.')
class List(Resource):
    @api.doc('get a list')
    @api.marshal_with(_list)
    def get(self, public_id):
        """get a user given its identifier"""
        list = get_a_list(public_id)
        if not list:
            api.abort(404)
        else:
            return list
            
    @api.doc('delete a list')    
    def delete(self, public_id):
        """delete list given its identifier"""
        ret = delete_a_list(public_id)
        return ret