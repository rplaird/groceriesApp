from flask import request
from flask_restplus import Resource

from ..util.dto import MemberDto
from ..service.member_service import save_new_member, get_all_members, get_a_member,delete_a_member

api = MemberDto.api
_member = MemberDto.member


@api.route('/')
class MemberList(Resource):
    @api.doc('list_of_members')
    @api.marshal_list_with(_member, envelope='data')
    def get(self):
        """List all members"""
        return get_all_members()

    @api.response(201, 'member successfully created.')
    @api.doc('create a new member')
    @api.expect(_member, validate=True)
    def post(self):
        """Creates a new Member """
        data = request.json
        return save_new_member(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Member identifier')
@api.response(404, 'Member not found.')
class Member(Resource):
    @api.doc('get a member')
    @api.marshal_with(_member)
    def get(self, public_id):
        """get a member given its identifier"""
        member = get_a_member(public_id)
        if not member:
            api.abort(404)
        else:
            return member
            
    @api.doc('delete a member')    
    def delete(self, public_id):
        """delete member given its identifier"""
        ret = delete_a_member(public_id)
        return ret