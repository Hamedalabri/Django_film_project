# Generated by Django 5.0.6 on 2024-05-11 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_nom_category_name_film_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='priority',
            field=models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=1),
        ),
        migrations.AlterField(
            model_name='film',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='film',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='film',
            name='year',
            field=models.IntegerField(default=2000),
        ),
    ]
