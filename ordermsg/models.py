# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models





class Goods(models.Model):
    goods_id = models.AutoField(primary_key=True)
    goods_name = models.CharField(max_length=255, blank=True, null=True)
    goods_img = models.CharField(max_length=255, blank=True, null=True)
    goods_introduce = models.CharField(max_length=255, blank=True, null=True)
    goods_freight = models.CharField(max_length=255, blank=True, null=True)
    goods_price = models.FloatField(blank=True, null=True)
    goods_num = models.IntegerField(blank=True, null=True)
    goods_sales = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods'


class LjswCacheTable(models.Model):
    cache_key = models.CharField(primary_key=True, max_length=255)
    value = models.TextField()
    expires = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ljsw_cache_table'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    or_name = models.CharField(max_length=255, blank=True, null=True)
    or_address = models.CharField(max_length=255, blank=True, null=True)
    or_phone = models.CharField(max_length=255, blank=True, null=True)
    or_price = models.DecimalField(max_digits=10, decimal_places=2)
    or_time = models.DateTimeField(blank=True, null=True)
    or_status = models.IntegerField(blank=True, null=True)
    or_note = models.CharField(max_length=255, blank=True, null=True)
    or_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


class Picture(models.Model):
    picture_id = models.AutoField(primary_key=True)
    picture_path = models.CharField(max_length=255, blank=True, null=True)
    picture_type = models.CharField(max_length=255, blank=True, null=True)
    article_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'picture'


class Praise(models.Model):
    praise_id = models.AutoField(primary_key=True)
    article_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'praise'



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
