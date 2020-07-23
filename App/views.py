from flask import Blueprint, redirect, url_for, request

blue=Blueprint('blue',__name__)

def init_view(app):
    app.register_blueprint(blue)

@blue.route('/',methods = ['POST','GET','DELETE'])
def index():
    return 'hello world'


@blue.route('/users/<int:id>/')
def users(id):
    print(id)
    print(type(id))
    return 'User API'

@blue.route('/getinfo/<string:token>/')
@blue.route('/gettoken/<int:token>/')
def get_info(token):
    print(token)
    print(type(token))
    return 'Get  Success'


@blue.route('/getpath/<path:address>/')
def get_path(address):
    print(address)
    print(type(address))
    return 'Get  path'

@blue.route('/getuuid/<uuid>/')
def get_uuid(uuid):
    print(uuid)
    print(type(uuid))
    return 'Get  uuid'


@blue.route('/getany/<any(a,b):an>/')
def get_any(an):
    print(an)
    print(type(an))
    return 'Get  an'



@blue.route('/redirect/')
def green():
    # return redirect('/')
    # 反向解析
    return redirect(url_for('blue.get_any',an ='a'))


@blue.route('/getrequest/',methods = ['POST','GET','PUT'])
def get_request():
    print(request.host)
    print(request.url)
    print(request)
    print(type(request))
    if request.method =='GET':
        return 'GET Success %S' % request.remote_addr
    elif request.method =='POST':
        return 'POST Success'
    else:

        return '%s Not Support ' % request.method


















