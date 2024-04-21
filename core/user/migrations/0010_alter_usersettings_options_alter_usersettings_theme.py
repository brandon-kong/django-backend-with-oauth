# Generated by Django 5.0.1 on 2024-02-25 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0009_alter_usersettings_theme'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usersettings',
            options={'verbose_name': 'User Settings', 'verbose_name_plural': 'User Settings'},
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='theme',
            field=models.CharField(choices=[('light', 'Light'), ('dark', 'Dark'), ('system', 'System')], default='system', max_length=64),
        ),
    ]