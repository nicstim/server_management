# Generated by Django 4.1.2 on 2022-10-11 17:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_alter_vps_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vps',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='UID сервера'),
        ),
    ]
