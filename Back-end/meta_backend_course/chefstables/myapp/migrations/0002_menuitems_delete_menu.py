# Generated by Django 5.1.2 on 2024-10-21 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menuitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=300)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
