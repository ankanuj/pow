# Generated by Django 2.2.6 on 2020-02-12 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_auto_20200211_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='profile_photo',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='upload_post',
        ),
        migrations.CreateModel(
            name='Profile_photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('upload_post', models.ImageField(blank=True, upload_to='post/%y/%m/%d/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
