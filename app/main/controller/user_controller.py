from flask import request
from flask_restplus import Resource

from ..util.decorator  import token_required
from ..util.dto import UserDto,FamilyDto,MemberDto
from ..service.user_service import save_new_user, get_all_users, get_a_user,delete_a_user
from ..service.family_service import get_all_families,get_families_in_list
from ..service.member_service import get_all_members_for_user

api = UserDto.api
_user = UserDto.user
_family = FamilyDto.family
_member = MemberDto.member

@api.route('/<public_id>/families')
class FamilyList(Resource):
    @api.marshal_list_with(_member, envelope='data')
    def getMembers(self,user_id):
        members = get_all_members_for_user(user_id)        
        return members
        
    @api.doc('list_of_families_for_user') 
    @api.marshal_list_with(_family, envelope='data')
    #@token_required
    def get(self,public_id):
        """List all families 
        for user"""
        members = self.getMembers(public_id)
        return get_families_in_list(members)
    

@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user
    
    @api.doc('delete a user')    
    def delete(self, public_id):
        """delete user given its identifier"""
        ret = delete_a_user(public_id)
        return ret
        