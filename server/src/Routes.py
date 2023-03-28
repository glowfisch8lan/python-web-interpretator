from flask import jsonify

from src.modules.compiler.CompilerController import CompilerController


def index():
    return jsonify({
        "success": "true",
        "data": 'v1'
    })

def route(app):
    app.add_url_rule('/', view_func=index, methods=['GET'])
    app.add_url_rule('/api/v1/run-code' , view_func=CompilerController().run_code, methods=['POST'])
    app.add_url_rule('/api/v1/get_img/<img>', view_func=CompilerController().get_image, methods=['GET'])
    return None
