# Generated by Django 2.1.15 on 2020-10-09 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('altitude', models.FloatField()),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
