from flask import Blueprint

__author__ = 'inchan'

store_blueprint = Blueprint('store', __name__)

@store_blueprint.route('/store/<string:name>')
def store_page():
    pass

