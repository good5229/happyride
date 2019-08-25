# Generated by Django 2.2.4 on 2019-08-25 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='지역명')),
                ('frequency_value', models.FloatField(blank=True, null=True, verbose_name='운행횟수')),
            ],
            options={
                'verbose_name': '지역 운행횟수 데이터',
                'ordering': ['name'],
            },
        ),
    ]
