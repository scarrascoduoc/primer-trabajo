# Generated by Django 4.0.4 on 2022-07-03 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]