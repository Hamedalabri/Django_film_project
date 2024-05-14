# Generated by Django 5.0.6 on 2024-05-11 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_book_film'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('priority', models.IntegerField(choices=[(1, 'Low'), (2, 'Meduim'), (3, 'High')], default=1)),
            ],
        ),
    ]
