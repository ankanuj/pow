# Generated by Django 2.2.6 on 2020-01-18 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200117_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]