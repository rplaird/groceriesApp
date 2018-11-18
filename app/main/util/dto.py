from flask_restplus import Namespace, fields

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
    
class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })
    
    
class FamilyDto:
    api = Namespace('family', description='family related operations')
    family = api.model('family', {            
        'name': fields.String(required=True, description='family name'),            
        'public_id': fields.String(description='family Identifier'),
        'default_list_id' : fields.String(description='default list')
    })
    
class MemberDto:
    api = Namespace('member', description='member related operations')
    member = api.model('member', {            
        'user_id': fields.String(required=True, description='associated user'),   
        'family_id': fields.String(required=True, description='associated family'),             
        'public_id': fields.String(description='member Identifier')
    })
    
class ItemDto:
    api = Namespace('item', description='item related operations')
    item = api.model('item', {  
        'public_id': fields.String(description='member Identifier'),         
        'list_id': fields.String(required=True, description='associated user'), 
        'desc': fields.String(required=True, description='associated family'),    
        'status': fields.String( description='associated family')             
                 
    })
    
class ListDto:
    api = Namespace('list', description='list related operations')
    list = api.model('list', {            
        'title': fields.String(required=True, description='list name'),            
        'public_id': fields.String(description='list Identifier'),
        'family_id': fields.String(description='family Identifier')
    })
    
    
