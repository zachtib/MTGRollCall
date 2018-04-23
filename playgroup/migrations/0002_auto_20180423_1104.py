# Generated by Django 2.0.4 on 2018-04-23 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playgroup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='playgroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='playgroup.PlayGroup'),
        ),
    ]
