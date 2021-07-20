# Generated by Django 3.1.2 on 2021-05-17 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210516_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complejo',
            name='equipamiento',
        ),
        migrations.AddField(
            model_name='equipamiento',
            name='complejo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='equipamiento', to='app.complejo'),
            preserve_default=False,
        ),
    ]