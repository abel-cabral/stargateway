import json
import requests

from flask import Response
from app.utils.resquest_methods_list import Methods

api_host = 'https://websage-api.abelcode.dev'

def api(request) -> Response:
    # Extrair apenas o token de autorização e o Content-Type dos headers da requisição
    headers = {
        'Authorization': request.headers.get('Authorization'),
        'Content-Type': request.headers.get('Content-Type')
    }
    
    endpoint = request.path
    method = request.method
    try:
        data = request.json
    except:
        data = None

    url = f"{api_host}{endpoint.split('/websage')[-1]}"
    requestMethod = method.upper()

    if requestMethod == Methods.GET:
        return requests.get(url, headers=headers)
    elif requestMethod == Methods.PUT:
        return requests.put(url, headers=headers, data=json.dumps(data))
    elif requestMethod == Methods.POST:
        return requests.post(url, headers=headers, data=json.dumps(data))
    elif requestMethod == Methods.PATCH:
        return requests.patch(url, headers=headers, data=json.dumps(data))
    elif requestMethod == Methods.DELETE:
        return requests.delete(url, headers=headers)
    
    return None