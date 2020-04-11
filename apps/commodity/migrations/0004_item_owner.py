# Generated by Django 2.0 on 2020-03-28 02:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commodity', '0003_auto_20200328_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]