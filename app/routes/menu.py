from flask import Blueprint, request, jsonify
from app.utils.db import conexMysql
from app.models.menu import Menu

bp = Blueprint('menu', __name__, url_prefix='/api')

@bp.route('/', methods=['GET'])

def obtener_menu():

    return Menu.obtener_menu()

#@bp.route('/insertar', methods=['POST'])

