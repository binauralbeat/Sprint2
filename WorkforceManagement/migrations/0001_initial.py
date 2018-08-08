# Generated by Django 2.1 on 2018-08-08 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('decom_date', models.DateTimeField(auto_now=True)),
                ('manufacturer', models.CharField(max_length=50)),
                ('make', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Training_Prog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prog_name', models.CharField(max_length=50)),
                ('training_desc', models.CharField(max_length=100)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(auto_now=True)),
                ('max_attendance', models.CharField(max_length=50)),
            ],
        ),
    ]
