from flask import Blueprint
__author__ = "inchan"


item_blueprint = Blueprint('item', __name__)

@item_blueprint.route('/item/<string:name>')
def item_page(name):
    pass

@item_blueprint.route('/load')
def load_item():


    pass