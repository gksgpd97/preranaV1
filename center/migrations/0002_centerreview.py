# Generated by Django 3.0.2 on 2020-03-27 06:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CenterReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='center_review', to='center.Center', verbose_name='센터명')),
            ],
        ),
    ]