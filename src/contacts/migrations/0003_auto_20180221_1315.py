# pylint: disable=C0103
# Generated by Django 2.0.2 on 2018-02-21 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20171120_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='user_social_auth',
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='friends',
                to='social_django.UserSocialAuth'),
        ),
    ]