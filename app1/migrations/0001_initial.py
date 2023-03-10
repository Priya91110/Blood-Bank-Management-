# Generated by Django 3.1.4 on 2020-12-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('age', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('bloodgroup', models.CharField(choices=[('1', 'A'), ('2', 'B'), ('3', 'AB'), ('4', 'O')], max_length=1)),
                ('address', models.CharField(max_length=225)),
            ],
        ),
    ]
