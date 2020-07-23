from flask import Flask

from App.settings import envs
from App.views import init_view
from App.ext import init_ext


def create_app(env):
# def create_app():
    app = Flask(__name__)
    #  加载配置
    # app.config.from_object(envs.get('develop'))
    app.config.from_object(envs.get(envs.get(env)))
    #  初始化第三方扩展库
    init_ext(app)
    # 初始化路由
    init_view(app=app)

    return app




