from flask import Flask

from App.views import blue, second, init_view
from App.ext import init_ext


def create_app():
    app = Flask(__name__)
    # app.register_blueprint(blue)
    # app.register_blueprint(second)
    # # uri  数据库+驱动：//用户名：密码@主机：端口/具体哪个库  添加到settings中
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqlite.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost:3306/helloflask"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    init_ext(app)
    init_view(app=app)

    return app



