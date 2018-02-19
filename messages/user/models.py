from datetime import datetime
from django.db import models


class User(models.Model):
    createtime = models.DateField()
    username = models.CharField(max_length=30)
    passwd = models.CharField(max_length=128)
    label = models.CharField(max_length=255)

    def __str__(self):
        return "username: {} label: {} createtime: {}".format(self.username, self.label, self.createtime)


    @classmethod
    def get_all(cls):
        userDict = {}
        query = User.objects.all()
        userlist = []
        for q in query:
            userDict['username'] = q.username
            userDict['passwd'] = q.passwd
            userDict['label'] = q.label
            userDict['date'] = q.createtime
            userlist.append(userDict)
        return userlist

    @classmethod
    def get_user(cls, username):
        try:
            user = User.objects.filter(username=username)[0].username
            return user
        except Exception:
            return None

    @classmethod
    def add_user(cls, username, passwd, label):
        createtime = datetime.now()
        user = User(username=username, passwd=passwd, label=label, createtime=createtime)
        user.save()

    @classmethod
    def del_user(cls,username):
        User.objects.filter(username=username).delete()
