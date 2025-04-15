from flask import Flask

def create_app():
    app = Flask(__name__)

    from myapp.controllers.calc_control import calc_control
    from myapp.controllers.about import about
    from myapp.controllers.faq import faq

    app.register_blueprint(faq, url_prefix='/')
    app.register_blueprint(about, url_prefix='/')
    app.register_blueprint(calc_control, url_prefix='/')

    return app