from flask import Flask

def create_app():
    app = Flask(__name__)

    from myapp.controllers.calc_control import calc_control

    app.register_blueprint(calc_control, url_prefix='/')
    return app