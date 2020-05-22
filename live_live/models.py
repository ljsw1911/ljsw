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
    room = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addres'


class ArticlePub(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=255, blank=True, null=True)
    article_main = models.TextField(blank=True, null=True)
    article_datatime = models.DateTimeField(blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    article_pic = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_pub'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


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
    comment_user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'


class DetailedPoints(models.Model):
    data_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    point_type = models.CharField(max_length=255, blank=True, null=True)
    points_time = models.DateTimeField(blank=True, null=True)
    points_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detailed_points'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Focus(models.Model):
    focus_id = models.AutoField(primary_key=True)
    author_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'focus'


class Garbage(models.Model):
    gar_id = models.AutoField(primary_key=True)
    gar_img = models.CharField(max_length=200, blank=True, null=True)
    gar_name = models.CharField(max_length=200)
    gar_type = models.ForeignKey('GarbageType', models.DO_NOTHING, db_column='gar_type')
    gar_introduce = models.CharField(max_length=1000, blank=True, null=True)
    gar_define = models.CharField(max_length=1000, blank=True, null=True)
    gar_guide = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'garbage'


class GarbageType(models.Model):
    gar_type_id = models.AutoField(primary_key=True)
    gar_type_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'garbage_type'


class Goods(models.Model):
    goods_id = models.AutoField(primary_key=True)
    goods_name = models.CharField(max_length=255, blank=True, null=True)
    goods_pic = models.TextField(blank=True, null=True)
    goods_introduce = models.CharField(max_length=255, blank=True, null=True)
    goods_freight = models.FloatField(blank=True, null=True)
    goods_price = models.FloatField(blank=True, null=True)
    goods_num = models.IntegerField(blank=True, null=True)
    goods_sales = models.IntegerField(blank=True, null=True)
    goods_category = models.CharField(max_length=255, blank=True, null=True)
    goods_para = models.CharField(max_length=255, blank=True, null=True)

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
    or_num = models.IntegerField(blank=True, null=True)
    or_price = models.DecimalField(max_digits=65, decimal_places=2)
    or_freight = models.DecimalField(max_digits=65, decimal_places=2, blank=True, null=True)
    or_time = models.DateTimeField(blank=True, null=True)
    or_status = models.IntegerField(blank=True, null=True)
    or_note = models.CharField(max_length=255, blank=True, null=True)

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


class Recycling(models.Model):
    recycling_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    recycling_time = models.DateTimeField(blank=True, null=True)
    current_time = models.DateTimeField(blank=True, null=True)
    recycle_msg = models.CharField(max_length=255, blank=True, null=True)
    recycle_state = models.PositiveIntegerField(blank=True, null=True)
    addres_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recycling'


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
