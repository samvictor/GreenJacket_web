# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-08 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('username', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_phone', models.CharField(blank=True, max_length=12, null=True)),
                ('branch_address', models.CharField(blank=True, max_length=200, null=True)),
                ('branch_city', models.CharField(blank=True, max_length=200, null=True)),
                ('branch_state', models.TextField(blank=True, null=True)),
                ('branch_zipcode', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Branch',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'Category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CategoryOption',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Category-Option',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=200)),
                ('main_phone', models.TextField(blank=True, null=True)),
                ('main_address', models.CharField(blank=True, max_length=200, null=True)),
                ('main_city', models.CharField(blank=True, max_length=200, null=True)),
                ('main_state', models.TextField(blank=True, null=True)),
                ('main_zipcode', models.TextField(blank=True, null=True)),
                ('credit_holder', models.TextField(blank=True, null=True)),
                ('credit_number', models.TextField(blank=True, null=True)),
                ('credit_expiration', models.TextField(blank=True, null=True)),
                ('credit_cvv', models.CharField(blank=True, max_length=4, null=True)),
                ('credit_zipcode', models.TextField(blank=True, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateField(blank=True, null=True)),
                ('is_active', models.NullBooleanField()),
            ],
            options={
                'db_table': 'Company',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('container_id', models.AutoField(primary_key=True, serialize=False)),
                ('container_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'Container',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
                ('action_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('options', models.CharField(blank=True, max_length=1000, null=True)),
                ('options_isFixed', models.CharField(blank=True, db_column='options_isFixed', max_length=1000, null=True)),
                ('options_price', models.CharField(blank=True, max_length=1000, null=True)),
                ('item_mealOptions', models.CharField(blank=True, db_column='item_mealOptions', max_length=1000, null=True)),
                ('item_mealPrice', models.CharField(blank=True, db_column='item_mealPrice', max_length=1000, null=True)),
            ],
            options={
                'db_table': 'Item',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ItemSize',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('itemSizePrice', models.IntegerField(db_column='itemSizePrice')),
            ],
            options={
                'db_table': 'Item-Size',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_nickname', models.CharField(max_length=200)),
                ('item_basePrice', models.IntegerField(db_column='item_basePrice')),
                ('item_isActive', models.NullBooleanField(db_column='item_isActive')),
                ('item_startDate', models.DateField(blank=True, db_column='item_startDate', null=True)),
                ('item_endDate', models.DateField(blank=True, db_column='item_endDate', null=True)),
                ('item_startTime', models.TimeField(blank=True, db_column='item_startTime', null=True)),
                ('item_endTime', models.TimeField(blank=True, db_column='item_endTime', null=True)),
            ],
            options={
                'db_table': 'Menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('option_id', models.AutoField(primary_key=True, serialize=False)),
                ('option_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'Option',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('size_id', models.AutoField(primary_key=True, serialize=False)),
                ('size_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'Size',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=1000)),
                ('QR_code', models.BinaryField(blank=True, db_column='QR_code', null=True)),
                ('is_admin', models.NullBooleanField()),
            ],
            options={
                'db_table': 'User',
                'managed': False,
            },
        ),
    ]
