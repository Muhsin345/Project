# Generated by Django 4.0 on 2021-12-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblsignup',
            name='Email',
            field=models.EmailField(max_length=50),
        ),
    ]