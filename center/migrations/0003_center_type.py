# Generated by Django 3.0.2 on 2020-02-09 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0002_auto_20200210_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='type',
            field=models.CharField(choices=[('1', '요가'), ('2', '필라테스')], default='1', max_length=1, verbose_name='센터 종류'),
        ),
    ]
