# Generated by Django 3.1.4 on 2020-12-17 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201102_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]