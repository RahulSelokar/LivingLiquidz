# Generated by Django 5.0.3 on 2024-04-18 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_seller_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_user',
            name='user',
        ),
    ]