from django.db import models
import logging
from datetime import datetime
logging.basicConfig(level=logging.INFO)


class Info(models.Model):
    username = models.CharField(max_length=30)
    title = models.CharField(max_length=255)
    content = models.TextField()
    time = models.FloatField()

    def __str__(self):
        return "username: {}  title: {} " .format(self.username, self.title)
    @classmethod
    def create_info(cls, username, title, content):
        info = Info(username=username, title=title, content=content, time=datetime.now().timestamp())
        info.save()

    @classmethod
    def delete_info(cls, id):
        try:
            Info.objects.filter(time=id)[0].delete()
        except Exception:
            print("wrong")
            pass

    @classmethod
    def get_infos(cls):
        infoDict = {}
        infoList = []
        query = Info.objects.all()
        for q in query:
            infoDict['username'] = q.username
            infoDict['title'] = q.title
            infoDict['content'] = q.content
            infoDict['id'] = q.time
            infoDict['time'] = datetime.fromtimestamp(q.time).strftime("%Y-%m-%d %H:%M:%S")
            infoList.append(infoDict)
        return infoList