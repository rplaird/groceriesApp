from flask import request
from flask_restplus import Resource

from ..util.dto import FamilyDto,MemberDto,ItemDto,ListDto
from ..service.family_service import save_new_family, get_all_families, get_a_family,delete_a_family,get_all_members_for_family
from ..service.item_service import get_all_items_for_list
from ..service.list_service import get_a_list_for_family


api = FamilyDto.api
_family = FamilyDto.family
_member = MemberDto.member
_item = ItemDto.item
_list = ListDto.list

@api.route('/<public_id>/listItems')
class ItemList(Resource):
    @api.marshal_list_with(_list, envelope='data')
    def getList(self,public_id):
        list = get_a_list_for_family(public_id)        
        return list
        
    @api.doc('listItems_for_family') 
    @api.marshal_list_with(_item, envelope='data')
    #@token_required
    def get(self,public_id):    
        list = self.getList(public_id)        
        return get_all_items_for_list(list)
    

@api.route('/<public_id>/members')
class MemberList(Resource):
    @api.doc('list_of_members_for_family') 
    @api.marshal_list_with(_member, envelope='data')
    def get(self,public_id):
        return get_all_members_for_family(public_id)


@api.route('/')
class FamilyList(Resource):
    @api.doc('list_of_families')
    @api.marshal_list_with(_family, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_families()

    @api.response(201, 'Family successfully created.')
    @api.doc('create a new family')
    @api.expect(_family, validate=True)
    def post(self):
        """Creates a new Family """
        data = request.json
        return save_new_family(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Family identifier')
@api.response(404, 'Family not found.')
class Family(Resource):
    @api.doc('get a family')
    @api.marshal_with(_family)
    def get(self, public_id):
        """get a user given its identifier"""
        family = get_a_family(public_id)
        if not family:
            api.abort(404)
        else:
            return family
            
    @api.doc('delete a family')    
    def delete(self, public_id):
        """delete family given its identifier"""
        ret = delete_a_family(public_id)
        return ret