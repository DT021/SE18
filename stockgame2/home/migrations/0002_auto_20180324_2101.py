# Generated by Django 2.0.2 on 2018-03-25 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='name',
            field=models.CharField(default='default_name', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='setting',
            name='startingBalance',
            field=models.DecimalField(decimal_places=2, max_digits=40),
        ),
    ]