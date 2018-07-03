from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    mail = models.EmailField()
    password = models.CharField(max_length=200)

    def __unicode__(self):
        return self.username


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    status = models.CharField(max_length=20, default='todo')
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user.username
