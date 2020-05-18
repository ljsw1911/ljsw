
from django.db import models


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    or_name = models.CharField(max_length=255, blank=True, null=True)
    or_address = models.CharField(max_length=255, blank=True, null=True)
    or_phone = models.CharField(max_length=255, blank=True, null=True)
    or_num = models.IntegerField(blank=True, null=True)
    or_price = models.DecimalField(max_digits=65, decimal_places=2)
    or_freight = models.DecimalField(max_digits=65, decimal_places=2)
    or_time = models.DateTimeField(blank=True, null=True)
    or_status = models.IntegerField(default=0)
    or_note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


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