# Generated by Django 4.1.4 on 2022-12-22 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_rename_create_date_comments_created_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post", old_name="create_date", new_name="created_date",
        ),
    ]
