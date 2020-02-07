from django.db import models
from datetime import datetime

class User(models.Model):
    username = models.CharField(max_length=10,null=False)
    password = models.CharField(max_length=12,null=False)
    profile_photo = models.CharField(max_length=200, null=False)
    name = models.CharField(max_length=10,null=False)
    phone = models.IntegerField(null=False)
    create_date = models.DateTimeField(default=datetime.now)

class Board(models.Model):
    user = models.ForeignKey(User, null=True)
    content = models.TextField(blank=True)
    title = models.CharField(max_length=100, blank=True)
    photo = models.CharField(max_length=200, null=True)
    post_data = models.DateTimeField(default=datetime.now)
    board_like = models.IntegerField(null=False, default = 0)

class Comment(models.Model):
    user = models.ForeignKey(User, null=True)
    board = models.ForeignKey(Board, null=True)
    content = models.TextField(blank = True)
    post_data = models.DateTimeField(default = datetime.now)
    groud_id = models.IntegerField(null=False, default = 1)
    depth = models.IntegerField(null=False, default = 1)
    comment_like = models.IntegerField(null=False, default = 0)


class LikeBoard(models.Model):
    user = models.ForeignKey(User, null=True)
    board = models.ForeignKey(Board, null=True)
    like_date = models.DateTimeField(default = datetime.now)

class LikeComment(models.Model):
    user = models.ForeignKey(User, null=True)
    comment = models.ForeignKey(Comment, null=True)
    like_date = models.DateTimeField(default = datetime.now)
