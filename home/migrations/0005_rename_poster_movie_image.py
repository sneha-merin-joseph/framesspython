# Generated by Django 5.0.6 on 2024-05-13 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_product_comment_movie_movie_director_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='poster',
            new_name='image',
        ),
    ]