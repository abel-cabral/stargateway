from flask import Blueprint, request
from app.services import websage

api = Blueprint('api', __name__)

@api.route('/websage/api/list-items', methods=['GET'])
def list_items():
    # Chamando a função websage com os parâmetros adequados
    response = websage.api(request)
    return response.json()

@api.route('/websage/api/save-item', methods=['POST'])
def save_item():
    # Chamando a função websage com os parâmetros adequados
    response = websage.api(request)
    return response.json()

@api.route('/websage/api/delete-item/<string:id>', methods=['DELETE'])
def delete_item(id):
    # Chamando a função websage com os parâmetros adequados
    response = websage.api(request)
    return response.json()