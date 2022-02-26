# Generated by Django 4.0.2 on 2022-02-07 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_alter_car_options_alter_comments_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='com_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]