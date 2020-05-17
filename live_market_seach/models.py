from django.db import models


class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    activity_name = models.CharField(max_length=255, blank=True, null=True)
    activity_type = models.CharField(max_length=255)
    discount = models.FloatField(blank=True, null=True)
    enough_price = models.FloatField(blank=True, null=True)
    points = models.CharField(max_length=255, blank=True, null=True)
    ending_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'activity'


class Discount(models.Model):
    discount_id = models.AutoField(primary_key=True)
    goods_id = models.ForeignKey('Goods',on_delete = models.CASCADE,
                                  null = False, db_column = 'goods_id',related_name='goods')
    activity_id = models.ForeignKey(Activity, on_delete = models.CASCADE,
                                  null = False, db_column = 'activity_id',related_name='activity')

    class Meta:
        managed = False
        db_table = 'discount'
        # unique_together = (('discount_id', 'goods', 'activity'),)


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