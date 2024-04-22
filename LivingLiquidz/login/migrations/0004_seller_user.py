# Generated by Django 5.0.3 on 2024-04-02 11:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_customer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='seller_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(blank=True, default=None, max_length=250, null=True)),
                ('date_of_birth', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile_number', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('locality', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('company_address', models.CharField(blank=True, max_length=50, null=True)),
                ('company_name', models.CharField(blank=True, max_length=50, null=True)),
                ('is_seller', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_images/')),
                ('pan_card', models.ImageField(blank=True, null=True, upload_to='pan_cards/')),
                ('aadhar_card', models.ImageField(blank=True, null=True, upload_to='aadhar_cards/')),
                ('gst_document', models.ImageField(blank=True, null=True, upload_to='gst_documents/')),
                ('commision', models.CharField(blank=True, max_length=240, null=True)),
                ('seller_reject', models.BooleanField(default=False)),
                ('seller_approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]