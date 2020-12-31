# Generated by Django 3.1.2 on 2020-11-02 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('active', 'نشط'), ('disabled', 'معطل')], default='active', max_length=50),
        ),
    ]
