# Generated by Django 4.2.6 on 2023-10-29 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_remove_message_created_at_remove_message_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='text',
            new_name='message',
        ),
    ]