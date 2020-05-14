
from django.db import models


class Recycling(models.Model):
    recycling_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True)
    recycling_time = models.DateTimeField(blank=True, null=True)
    current_time = models.DateTimeField(blank=True, null=True)
    recycle_msg = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recycling'

