# Generated by Django 4.1.1 on 2022-09-19 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cate_image',
            new_name='cat_image',
        ),
    ]
