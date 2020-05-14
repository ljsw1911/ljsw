from django.db import models

# Create your models here.
class Garbage(models.Model):
    gar_id = models.AutoField(primary_key=True)
    gar_img = models.CharField(max_length=200, blank=True, null=True)
    gar_name = models.CharField(max_length=200)
    gar_type = models.ForeignKey('GarbageType', on_delete = models.DO_NOTHING,
                                  null = True, db_column = 'gar_type_id',related_name='type_id')
    gar_introduce = models.CharField(max_length=1000, blank=True, null=True)
    gar_define = models.CharField(max_length=1000, blank=True, null=True)
    gar_guide = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'garbage'

    # def __str__(self):
    #     return f''

class GarbageType(models.Model):
    gar_type_id = models.AutoField(primary_key=True)
    gar_type_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'garbage_type'
