# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addres(models.Model):
    address_id = models.AutoField(primary_key=True, unique=True)
    user_id = models.IntegerField()
    estate = models.CharField(max_length=255, blank=True, null=True)
    building = models.CharField(max_length=255, blank=True, null=True)
    identity = models.IntegerField(blank=True, null=True)
    room = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addres'


class DetailedPoints(models.Model):
    data_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    point_type = models.CharField(max_length=255, blank=True, null=True)
    points_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    points_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detailed_points'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_phone = models.CharField(unique=True, max_length=32)
    avatar = models.ImageField(max_length=255, blank=True, null=True, upload_to='avatars')
    gender = models.IntegerField(blank=True, null=True, default=0)
    nickname = models.CharField(unique=True, max_length=16)
    birthday = models.DateField(blank=True, null=True)
    signature = models.CharField(max_length=120, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True, default=0)
    now_integral = models.IntegerField(blank=True, null=True, default=0)
    add_integral = models.IntegerField(blank=True, null=True, default=0)
    recycle_num = models.IntegerField(blank=True, null=True, default=0)
    qq = models.CharField(max_length=32, blank=True, null=True)
    vx = models.CharField(max_length=64, blank=True, null=True)
    zfb = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Recycling(models.Model):
    recycling_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True)
    recycling_time = models.DateTimeField(blank=True, null=True)
    current_time = models.DateTimeField(blank=True, null=True)
    recycle_msg = models.CharField(max_length=255, blank=True, null=True)
    recycle_state = models.IntegerField(default=0, blank=True, null=True)
    addres_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recycling'
