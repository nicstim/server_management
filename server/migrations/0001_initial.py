# Generated by Django 4.1.2 on 2022-10-11 17:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VPS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UID сервера')),
                ('cpu', models.PositiveIntegerField(default=1, verbose_name='Количество ядер')),
                ('ram', models.PositiveIntegerField(default=1024, verbose_name='Объем ОЗУ')),
                ('hdd', models.PositiveIntegerField(default=1024, verbose_name='Объем HDD')),
                ('status', models.CharField(choices=[('Запущен', 'started'), ('Остановлен', 'blocked'), ('Заблокирован', 'stopped')], max_length=12, verbose_name='Статус сервера')),
            ],
            options={
                'verbose_name': 'Сервер',
                'verbose_name_plural': 'Сервера',
            },
        ),
    ]
