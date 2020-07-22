from flask import Blueprint, render_template

from App.models import models, User

blue = Blueprint('blue',__name__)

@blue.route('/')
def index():
    # return '你好呀'
    return render_template('index.html')


@blue.route('/createdb/')
def createdb():
    models.create_all()
    return '创建成功'

@blue.route('/adduser/')
def adduser():
    user = User()
    user.username = 'Tom'

    # models.session.add(user)
    # models.session.commit()
    user.save()
    return "保存成功"















