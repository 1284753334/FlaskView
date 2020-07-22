from.first_blue import blue
from.second_blue import second
# # 懒加载
# def  init_route(app):
#
#     @app.route('/')
#     def hello_world():
#         return 'Hello World!'
#
#     @app.route('/hello/')
#     def hello():
#         return 'Hello 123!'
#
#     @app.route('/hi/')
#     def hi():
#         return 'hi 123!'
from .third_blue import third



def init_view(app):
    app.register_blueprint(blue)
    app.register_blueprint(second)
    app.register_blueprint(third)



