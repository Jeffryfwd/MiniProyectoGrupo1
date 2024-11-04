# Generated by Django 5.1.2 on 2024-10-30 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_id',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='closedday',
            name='date',
            field=models.DateField(unique=True),
        ),
        migrations.AlterField(
            model_name='detailrequest',
            name='detail_request_type',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='editorial_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='typeclient',
            name='type_client',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.client')),
            ],
        ),
    ]
