# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ArticlePub(models.Model):
    artilce_id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=255, blank=True, null=True)
    article_main = models.TextField(blank=True, null=True)
    article_img = models.CharField(max_length=255, blank=True, null=True)
    article_datatime = models.DateTimeField(blank=True, null=True)
    article_video = models.IntegerField(blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_pub'


class Collection(models.Model):
    coll_id = models.AutoField(primary_key=True)
    article_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collection'


class Comments(models.Model):
    comm_id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    article_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'


class Focus(models.Model):
    focus_id = models.AutoField(primary_key=True)
    author_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'focus'


class Praise(models.Model):
    praise_id = models.AutoField(primary_key=True)
    article_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'praise'
