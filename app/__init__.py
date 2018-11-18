# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.family_controller import api as family_ns
from .main.controller.member_controller import api as member_ns
from .main.controller.item_controller import api as item_ns
from .main.controller.list_controller import api as list_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title=' Task Management APIs',
          version='1.0',
          description='Services for Grocery list demo app'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(family_ns, path='/family')
api.add_namespace(member_ns, path='/member')
api.add_namespace(item_ns, path='/item')
api.add_namespace(list_ns, path='/list')
api.add_namespace(auth_ns)