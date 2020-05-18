
from django.db import models


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    goods_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart'

