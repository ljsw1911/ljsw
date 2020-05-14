# Generated by Django 2.2.12 on 2020-05-12 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addres',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('estate', models.CharField(blank=True, max_length=255, null=True)),
                ('building', models.CharField(blank=True, max_length=255, null=True)),
                ('identity', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'addres',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetailedPoints',
            fields=[
                ('data_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('point_type', models.CharField(blank=True, max_length=255, null=True)),
                ('points_time', models.DateTimeField(blank=True, null=True)),
                ('points_num', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'detailed_points',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_phone', models.CharField(max_length=32, unique=True)),
                ('avatar', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.IntegerField(blank=True, null=True)),
                ('nickname', models.CharField(max_length=16, unique=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('signature', models.CharField(blank=True, max_length=120, null=True)),
                ('position', models.IntegerField(blank=True, null=True)),
                ('now_integral', models.IntegerField(blank=True, null=True)),
                ('add_integral', models.IntegerField(blank=True, null=True)),
                ('recycle_num', models.IntegerField(blank=True, null=True)),
                ('qq', models.CharField(blank=True, max_length=32, null=True)),
                ('vx', models.CharField(blank=True, max_length=64, null=True)),
                ('zfb', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
