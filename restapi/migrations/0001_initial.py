# Generated by Django 2.2 on 2019-04-15 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('open', models.FloatField()),
                ('close', models.FloatField()),
                ('volume', models.IntegerField()),
            ],
        ),
    ]
