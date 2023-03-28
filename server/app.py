from flask import Flask
from src.Routes import route
from dotenv import load_dotenv
from werkzeug.exceptions import HTTPException

load_dotenv()

app = Flask(__name__)
app.debug = True
route(app)


# @app.errorhandler(Exception)
# def handle_exception(e):
#
#     try:
#         msg = e.msg
#         code = e.code
#     except:
#         msg = 'error'
#         code = 500
#
#     return msg, code


if __name__ == "__main__":
    app.run(host='0.0.0.0')
