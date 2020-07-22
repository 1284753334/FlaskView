from flask import Flask
from App.views import blue, second, init_view


def create_app():
    app = Flask(__name__)
    # app.register_blueprint(blue)
    # app.register_blueprint(second)
    init_view(app)


    return app



