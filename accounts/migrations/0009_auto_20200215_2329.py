# Generated by Django 2.2.6 on 2020-02-15 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200215_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_photo',
            name='upload_post',
            field=models.ImageField(blank=True, upload_to='post/{{user.name}}/%y/%m/%d/'),
        ),
    ]
