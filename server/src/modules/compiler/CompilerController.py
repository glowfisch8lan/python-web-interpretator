from ...base.Controller import Controller
from flask import jsonify, request, send_file
from ..services.CodeRunnerService import run

class CompilerController(Controller):
    """docstring"""

    def __init__(self):
        """Constructor"""
        super().__init__()

    def run_code(self):
        data = request.get_data()
        output = run(data)
        return jsonify({
            "success": "true",
            "data": output
        })

    def get_image(self, img):
        requested_path = 'imgs/' + img + ".png"
        return send_file(requested_path, mimetype='application/vpn', download_name=img + '.png',
                         as_attachment=True)
