# Generated by Django 4.1.2 on 2022-10-28 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='wishing_list',
        ),
        migrations.AddField(
            model_name='book',
            name='wishing_list',
            field=models.ManyToManyField(related_name='wishing_list', to='web.user'),
        ),
    ]
