from flask import Blueprint, request, jsonify
# from app.services import service1, service2

api = Blueprint('api', __name__)

# @api_bp.route('/service1/endpoint', methods=['GET', 'POST'])
# def service1_endpoint():
#     if request.method == 'GET':
#         response = service1.get_data()
#     else:
#         response = service1.post_data(request.json)
#     return jsonify(response)

# @api_bp.route('/service2/endpoint', methods=['GET', 'POST'])
# def service2_endpoint():
#     if request.method == 'GET':
#         response = service2.get_data()
#     else:
#         response = service2.post_data(request.json)
#     return jsonify(response)