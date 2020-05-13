# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addres(models.Model):
    address_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    estate = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    identity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addres'


class DetailedPoints(models.Model):
    data_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    point_type = models.CharField(max_length=255, blank=True, null=True)
    points_time = models.DateTimeField(blank=True, null=True)
    points_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detailed_points'


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
