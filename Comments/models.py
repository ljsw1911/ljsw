
from django.db import models


class Comments(models.Model):
    comm_id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    article_id = models.IntegerField(blank=True, null=True)
    comment_user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'


class ArticlePub(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=255, blank=True, null=True)
    article_main = models.TextField(blank=True, null=True)
    article_datatime = models.DateTimeField(blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_pub'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_phone = models.CharField(unique=True, max_length=32)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(unique=True, max_length=16)
    birthday = models.DateField(blank=True, null=True)
    signature = models.CharField(max_length=120, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    now_integral = models.IntegerField(blank=True, null=True)
    add_integral = models.IntegerField(blank=True, null=True)
    recycle_num = models.IntegerField(blank=True, null=True)
    qq = models.CharField(max_length=32, blank=True, null=True)
    vx = models.CharField(max_length=64, blank=True, null=True)
    zfb = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'