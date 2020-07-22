

from App.ext import models


class User(models.Model):
    id = models.Column(models.Integer,primary_key=True)
    username = models.Column(models.String(32))

    def save(self):
        models.session.add(self)
        models.session.commit()


class Student(models.Model):
    id = models.Column(models.Integer,primary_key=True)
    username = models.Column(models.String(32))




