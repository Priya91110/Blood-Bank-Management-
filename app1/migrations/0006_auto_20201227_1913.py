# Generated by Django 3.1.4 on 2020-12-27 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_donor_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceptor',
            name='bloodgroup',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=2),
        ),
    ]