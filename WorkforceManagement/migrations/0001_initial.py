<<<<<<< HEAD
# Generated by Django 2.1 on 2018-08-08 16:41
=======
# Generated by Django 2.1 on 2018-08-08 18:56
>>>>>>> 9d773dd499e0f07fad0c26a0a90067ecdbd15f06

from django.db import migrations, models
import django.db.models.deletion


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
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=50)),
                ('budget', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_supervisor', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkforceManagement.Computer')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkforceManagement.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Training_Prog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prog_name', models.CharField(max_length=50)),
                ('training_desc', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now=True)),
                ('max_attendance', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='training',
            field=models.ManyToManyField(to='WorkforceManagement.Training_Prog'),
        ),
    ]
